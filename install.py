#!/usr/bin/env python3
"""Install design skills into your local Claude Code skills directory.

Copies senior-designer and/or ux-eval into ~/.claude/skills/ so Claude
Code picks them up automatically on your next session.

Usage:
    python install.py                             # install both skills
    python install.py senior-designer             # just the designer
    python install.py ux-eval                     # just the evaluator
    python install.py --dry-run                   # preview only
    python install.py --force                     # overwrite existing
    python install.py --target ./.claude/skills   # project-scoped install
    python install.py --list                      # show available skills
    python install.py --uninstall                 # remove installed skills
    python install.py --verify                    # check existing install
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

AVAILABLE_SKILLS = ("senior-designer", "ux-eval")
DEFAULT_TARGET = Path.home() / ".claude" / "skills"

SKILL_INFO = {
    "senior-designer": {
        "description": "Orchestrator skill for UX problem-solving and design artifacts",
        "files": ["SKILL.md", "references/"],
    },
    "ux-eval": {
        "description": "8-gate UX evaluation framework (Agent Evil)",
        "files": ["SKILL.md"],
    },
}


def find_source(skill_name: str) -> Path:
    script_dir = Path(__file__).resolve().parent
    source = script_dir / skill_name
    if not source.is_dir() or not (source / "SKILL.md").is_file():
        print(
            f"  ERROR: {skill_name}/ not found next to install.py "
            f"(looked in {source}).",
            file=sys.stderr,
        )
        print(
            "  Are you running this from the repo root, after cloning?",
            file=sys.stderr,
        )
        sys.exit(1)
    return source


def count_files(path: Path) -> int:
    return sum(1 for f in path.rglob("*") if f.is_file())


def verify_install(skill_name: str, target_root: Path) -> bool:
    target = target_root / skill_name
    skill_md = target / "SKILL.md"

    if not target.exists():
        print(f"  {skill_name}: NOT INSTALLED")
        return False

    if not skill_md.is_file():
        print(f"  {skill_name}: BROKEN (missing SKILL.md)")
        return False

    file_count = count_files(target)
    print(f"  {skill_name}: OK ({file_count} files in {target})")

    if skill_name == "senior-designer":
        refs = target / "references"
        if refs.is_dir():
            ref_count = sum(1 for f in refs.iterdir() if f.suffix == ".md")
            print(f"    references: {ref_count} specialist files")
        else:
            print("    references: MISSING (skill will work but can't route to specialists)")

    return True


def install_one(
    skill_name: str, target_root: Path, force: bool, dry_run: bool
) -> bool:
    source = find_source(skill_name)
    target = target_root / skill_name

    info = SKILL_INFO.get(skill_name, {})
    desc = info.get("description", "")
    source_count = count_files(source)

    print(f"  {skill_name}")
    print(f"    {desc}")
    print(f"    source: {source} ({source_count} files)")
    print(f"    target: {target}")

    if target.exists():
        if force:
            print("    target exists — will overwrite (--force)")
        else:
            print(
                "    SKIP: already installed. "
                "Pass --force to overwrite."
            )
            return False

    if dry_run:
        print("    (dry-run — no files copied)")
        return True

    target_root.mkdir(parents=True, exist_ok=True)
    if target.exists():
        shutil.rmtree(target)

    ignore = shutil.ignore_patterns("evals", "evals/*", ".DS_Store")
    shutil.copytree(source, target, ignore=ignore)

    installed_count = count_files(target)
    print(f"    installed ({installed_count} files)")
    return True


def uninstall_one(skill_name: str, target_root: Path, dry_run: bool) -> bool:
    target = target_root / skill_name
    if not target.exists():
        print(f"  {skill_name}: not installed, nothing to remove")
        return False

    if dry_run:
        print(f"  {skill_name}: would remove {target}")
        return True

    shutil.rmtree(target)
    print(f"  {skill_name}: removed from {target}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install design skills (senior-designer, ux-eval) into Claude Code.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "After installing:\n"
            "  1. Restart Claude Code or start a new session.\n"
            "  2. Describe a design problem, paste a Figma link, or ask for a UX audit.\n"
            "  3. The skill activates automatically — no slash command needed.\n"
            "\n"
            "For project-scoped installs: --target ./.claude/skills\n"
            "For full docs: see README.md"
        ),
    )
    parser.add_argument(
        "skill",
        nargs="?",
        choices=AVAILABLE_SKILLS,
        default=None,
        help="Which skill to install. Omit to install both.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without copying any files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing install.",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=DEFAULT_TARGET,
        help=f"Skills directory (default: {DEFAULT_TARGET}).",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available skills and exit.",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Check whether skills are installed correctly.",
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="Remove installed skills.",
    )
    args = parser.parse_args()

    if args.list:
        print("\nAvailable skills:\n")
        for name in AVAILABLE_SKILLS:
            info = SKILL_INFO.get(name, {})
            source = Path(__file__).resolve().parent / name
            status = "ready" if (source / "SKILL.md").is_file() else "missing"
            print(f"  {name}")
            print(f"    {info.get('description', '')}")
            print(f"    status: {status}")
            print()
        return 0

    if args.verify:
        print(f"\nVerifying installs in {args.target}:\n")
        all_ok = True
        for name in AVAILABLE_SKILLS:
            if not verify_install(name, args.target):
                all_ok = False
        print()
        if all_ok:
            print("All skills installed correctly.")
        else:
            print("Some skills missing or broken. Run: python install.py")
        return 0 if all_ok else 1

    if args.uninstall:
        to_remove = [args.skill] if args.skill else list(AVAILABLE_SKILLS)
        print(f"\nRemoving {len(to_remove)} skill(s) from {args.target}:\n")
        for name in to_remove:
            uninstall_one(name, args.target, args.dry_run)
        print()
        return 0

    to_install = [args.skill] if args.skill else list(AVAILABLE_SKILLS)

    print(
        f"\nInstalling {len(to_install)} skill(s) to {args.target}"
        + (" (dry-run)" if args.dry_run else "")
        + "\n"
    )

    installed = []
    for name in to_install:
        if install_one(name, args.target, args.force, args.dry_run):
            installed.append(name)
        print()

    if installed and not args.dry_run:
        print("Done. Restart Claude Code or start a new session to activate.\n")
        print("Verify with:")
        print("  python install.py --verify\n")

        if "senior-designer" in installed:
            print("Try it — paste this into Claude Code:")
            print('  "Users search \'urine\' on our diagnostics app and get')
            print("   7 near-identical tests. Help them pick the right one.\"\n")

        if "ux-eval" in installed:
            print("To evaluate a design output:")
            print('  "Run a UX eval on the solution above"\n')

    elif not installed:
        print("Nothing installed. Use --force to overwrite existing installs.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
