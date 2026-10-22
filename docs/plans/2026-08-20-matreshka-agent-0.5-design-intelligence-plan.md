# Проектирование интерфейса

Это техническая карта компонентов и проверок, а не история разработки или свидетельство выполненной проверки. Идентификаторы сохранены для совместимости с валидатором пакета.

## Условия готовности

`IMPLEMENTED_PENDING_NATIVE_VALIDATION` обозначает, что статической реализации недостаточно для заявления о готовности: требуется свежая native-проверка в целевой среде. `PENDING_NATIVE` означает отсутствие такой проверки. `STATIC_HARDENING_IMPLEMENTED` описывает только статический слой, не фактическую приёмку. Ни одна строка ниже не заменяет актуальные результаты запуска.

## Карта технических требований

| Task | Result | Main files | Status |
| --- | --- | --- | --- |
| `D1` | UI/design relevance + recon | design skill/reference, Build/controller | `IMPLEMENTED` |
| `D2` | Apple-inspired core + UI craft/motion baseline | `design-core.md` | `IMPLEMENTED` |
| `D3` | root `DESIGN.md` + design identity | template, controller, ledger/permissions | `IMPLEMENTED` |
| `D4` | prototype divergence + picker workflow | prototype contract, design skill | `IMPLEMENTED` |
| `D5` | `DESIGN_CONTEXT_SET` + existing-first primitives | spec/planner/task/implement/Project Intelligence | `IMPLEMENTED` |
| `D6` | independent Design Review | review package/skill/report + controller/budget routing | `IMPLEMENTED` |
| `D7` | Visual Design Check separate from E2E/G4 | verifier/report + browser/design contracts | `IMPLEMENTED` |
| `D8` | design drift + finish/recovery/dashboard | controller/finish/ledger/dashboard | `IMPLEMENTED` |
| `D9` | package + static/behavioral hardening as 11th skill | manifests/wrappers/readmes/CI/checkers | `IMPLEMENTED` |
| `D10` | native acceptance | disposable full-stack UI fixture | `PENDING_NATIVE` |


## Проверка перед использованием

- Проверить наличие и связи перечисленных компонентов в текущей версии.
- Выполнить штатные валидаторы и сохранить фактические результаты.
- Не объявлять успешную native-проверку без воспроизводимых свидетельств.
- Сохранять разделение полномочий, безопасности, независимого review и верификации.

[Руководство](../../README.md)
