# Контекст проекта

Это техническая карта компонентов и проверок, а не история разработки или свидетельство выполненной проверки. Идентификаторы сохранены для совместимости с валидатором пакета.

## Условия готовности

`IMPLEMENTED_PENDING_NATIVE_VALIDATION` обозначает, что статической реализации недостаточно для заявления о готовности: требуется свежая native-проверка в целевой среде. `PENDING_NATIVE` означает отсутствие такой проверки. `STATIC_HARDENING_IMPLEMENTED` описывает только статический слой, не фактическую приёмку. Ни одна строка ниже не заменяет актуальные результаты запуска.

## Карта технических требований

| Task | Status | Result | Main files | Remaining gate |
| --- | --- | --- | --- | --- |
| `P1` | `IMPLEMENTED` | `PROJECT_TOPOLOGY` and reusable profile shape | project-intelligence reference, project-profile reference/template | native full-stack topology proof |
| `P2` | `IMPLEMENTED` | `AREA_CONTEXT_SET` routing into task briefs/dispatch | controller, task brief, dispatch/report templates | native context-isolation proof |
| `P3` | `IMPLEMENTED` | Controller-owned/frozen `IC-xx` contracts for cross-area seams | interface-contract template, planner/controller/reviewer | native producer/consumer proof |
| `P4` | `IMPLEMENTED` | Safe `RUNTIME_MAP` with ownership/permission separation | project-intelligence, controller, permission/ledger | native runtime ownership proof |
| `P5` | `IMPLEMENTED` | Documentation impact/drift gate after verified behavior | project-intelligence, finish, ledger/handoff | native docs-drift proof |
| `P6` | `IMPLEMENTED` | Specialist role archetypes without authority/budget inflation | controller/planner/task/dispatch/review | native routing proof |
| `P7` | `IMPLEMENTED` | Project Intelligence observable/recoverable | ledger, dashboard state/html, recovery | native projection/recovery proof |
| `P8` | `STATIC_HARDENING_IMPLEMENTED` | deterministic integrity check + CI wiring + docs/evals | `scripts/check_dev_05.py`, workflow, README, eval suite | CI evidence + native acceptance |


## Проверка перед использованием

- Проверить наличие и связи перечисленных компонентов в текущей версии.
- Выполнить штатные валидаторы и сохранить фактические результаты.
- Не объявлять успешную native-проверку без воспроизводимых свидетельств.
- Сохранять разделение полномочий, безопасности, независимого review и верификации.

[Руководство](../../README.md)
