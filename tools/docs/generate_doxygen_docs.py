#!/usr/bin/env python3
"""Generate profile-canonical API pages and configured C4 code views from Doxygen XML."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

if __package__:
    from .doxygen_markdown import DocumentationError, load_config, run_doxygen, synchronize
else:
    from doxygen_markdown import DocumentationError, load_config, run_doxygen, synchronize


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True, help="Project documentation configuration JSON")
    parser.add_argument("--check", action="store_true", help="Fail if generated output is stale or orphaned")
    parser.add_argument(
        "--run-doxygen",
        action="store_true",
        help="Run the configured Doxyfile before reading XML",
    )
    parser.add_argument(
        "--doxygen",
        default="doxygen",
        help="Doxygen executable used with --run-doxygen (default: doxygen)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        config = load_config(args.config)
        if config.schema_version == 1:
            print(
                "warning: documentation schema_version 1 is deprecated; migrate to the "
                "profile-canonical schema_version 2 publication model",
                file=sys.stderr,
            )
        if args.run_doxygen:
            run_doxygen(config, args.doxygen)
        messages = synchronize(config, args.check)
    except DocumentationError as exc:
        print(f"documentation generation failed: {exc}", file=sys.stderr)
        return 2
    for message in messages:
        print(message)
    if args.check and messages:
        return 1
    if args.check:
        print("Doxygen Markdown outputs are current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
