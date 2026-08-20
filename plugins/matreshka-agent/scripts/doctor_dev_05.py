#!/usr/bin/env python3
"""Run the read-only Matreshka doctor against the unreleased 0.5 package inventory."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

sys.dont_write_bytecode = True

DESIGN_SKILL = "designing-product-experience"
DESIGN_WRAPPER = "matreshka-design.md"


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_dev_validator(plugin_root: Path) -> ModuleType:
    validator = load_module(
        "matreshka_validate_package_04_for_dev_doctor",
        plugin_root / "scripts" / "validate_package.py",
    )
    skills = tuple(validator.REQUIRED_SKILLS)
    if DESIGN_SKILL not in skills:
        pivot = skills.index("specifying-software-work") if "specifying-software-work" in skills else 2
        skills = skills[:pivot] + (DESIGN_SKILL,) + skills[pivot:]
    validator.REQUIRED_SKILLS = skills
    wrappers = dict(validator.CODEX_PROMPT_WRAPPERS)
    wrappers[DESIGN_WRAPPER] = DESIGN_SKILL
    validator.CODEX_PROMPT_WRAPPERS = wrappers
    return validator


if __name__ == "__main__":
    doctor_path = Path(__file__).with_name("doctor.py")
    doctor = load_module("matreshka_doctor_04_for_dev", doctor_path)
    doctor.load_validator = load_dev_validator
    raise SystemExit(doctor.main())
