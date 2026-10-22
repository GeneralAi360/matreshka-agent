# Трассируемость и наблюдаемость

Это техническая карта компонентов и проверок, а не история разработки или свидетельство выполненной проверки. Идентификаторы сохранены для совместимости с валидатором пакета.

## Условия готовности

`IMPLEMENTED_PENDING_NATIVE_RELEASE_VALIDATION` обозначает, что статической реализации недостаточно для заявления о готовности: требуется свежая native-проверка в целевой среде. `PENDING_NATIVE` означает отсутствие такой проверки. `STATIC_HARDENING_IMPLEMENTED` описывает только статический слой, не фактическую приёмку. Ни одна строка ниже не заменяет актуальные результаты запуска.

## Карта технических требований

| Task | Status | Result | Remaining external evidence |
| --- | --- | --- | --- |
| `T1` | `IMPLEMENTED` | Source brief, `U-` manifest, G1–G4, observability contracts/assets | latest native regression |
| `T2` | `IMPLEMENTED` | Build End-to-End → namespaced controller, public modes/scenarios | latest native launch UX |
| `T3` | `IMPLEMENTED` | state machine/ledger/recovery/permissions | latest recovery acceptance |
| `T4` | `IMPLEMENTED` | planner/reviewer/verifier consume U/S and blind G4 independently | latest native role isolation |
| `T5` | `IMPLEMENTED` | T0–T3 complexity + evidence-scoped cross-area `IC-xx` contracts | full-stack native proof |
| `T6` | `STATIC_HARDENING_IMPLEMENTED` | CI, deterministic validators, current package docs, dev integrity check | observable CI + native host acceptance + version/publisher release step |


## Проверка перед использованием

- Проверить наличие и связи перечисленных компонентов в текущей версии.
- Выполнить штатные валидаторы и сохранить фактические результаты.
- Не объявлять успешную native-проверку без воспроизводимых свидетельств.
- Сохранять разделение полномочий, безопасности, независимого review и верификации.

[Руководство](../../README.md)
