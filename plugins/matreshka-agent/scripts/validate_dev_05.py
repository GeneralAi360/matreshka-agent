#!/usr/bin/env python3
"""Validate the unreleased Matreshka Agent 0.5 package using the proven 0.4 validator core.

The versioned manifests intentionally remain 0.4.0 until release gates pass. This
wrapper extends only the development-track package inventory (11th design skill
and its optional Codex wrapper) while preserving every existing validator check
and negative self-test.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

sys.dont_write_bytecode = True

DESIGN_SKILL = "designing-product-experience"
DESIGN_WRAPPER = "matreshka-design.md"


def load_base() -> ModuleType:
    path = Path(__file__).with_name("validate_package.py")
    spec = importlib.util.spec_from_file_location("matreshka_validate_package_04", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load scripts/validate_package.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def configure_dev_05(module: ModuleType) -> None:
    skills = tuple(module.REQUIRED_SKILLS)
    if DESIGN_SKILL not in skills:
        # Keep Build End-to-End first for existing negative self-test behavior;
        # insert the design skill next to specification/planning responsibilities.
        pivot = skills.index("specifying-software-work") if "specifying-software-work" in skills else 2
        skills = skills[:pivot] + (DESIGN_SKILL,) + skills[pivot:]
    module.REQUIRED_SKILLS = skills

    wrappers = dict(module.CODEX_PROMPT_WRAPPERS)
    wrappers[DESIGN_WRAPPER] = DESIGN_SKILL
    module.CODEX_PROMPT_WRAPPERS = wrappers


if __name__ == "__main__":
    base = load_base()
    configure_dev_05(base)
    raise SystemExit(base.main())
