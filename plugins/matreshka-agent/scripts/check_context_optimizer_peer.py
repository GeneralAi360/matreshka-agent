#!/usr/bin/env python3
"""Self-test for Matreshka → Context Optimizer peer bridge."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path


def load_peer(plugin_root: Path):
    path = plugin_root / "scripts" / "context_optimizer_peer.py"
    spec = importlib.util.spec_from_file_location("context_optimizer_peer", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    plugin_root = Path(__file__).resolve().parents[1]
    peer = load_peer(plugin_root)

    with tempfile.TemporaryDirectory() as tmp:
        project = Path(tmp) / "project"
        skill = project / ".agents" / "skills" / "context-optimizer"
        scripts = skill / "scripts"
        scripts.mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: context-optimizer\n---\n", encoding="utf-8")
        (scripts / "context_optimizer.py").write_text(
            "import json\nprint(json.dumps({'message_ru':'Проверка контекста выполнена.','bridge':{'status':'READY'}}, ensure_ascii=False))\n",
            encoding="utf-8",
        )

        resolved = peer.resolve(project)
        assert resolved["status"] == "READY"
        assert resolved["source"] == "PROJECT_CODEX"

        planned = peer.invoke(
            project,
            "start",
            execute=False,
            provider="none",
            trigger_mode="NEW_PROJECT_BASELINE",
            trigger_reason="Новый проект",
            automatic=True,
        )
        assert planned["status"] == "READY_TO_RUN"
        assert "--execute" not in planned["argv"]

        executed = peer.invoke(
            project,
            "start",
            execute=True,
            provider="none",
            trigger_mode="NEW_PROJECT_BASELINE",
            trigger_reason="Новый проект",
            automatic=True,
        )
        assert executed["status"] == "COMPLETED"
        assert executed["message_ru"] == "Проверка контекста выполнена."

    print("PASS: Context Optimizer peer bridge")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
