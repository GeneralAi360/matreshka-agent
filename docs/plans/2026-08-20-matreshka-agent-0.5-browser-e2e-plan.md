# Проверка браузера и E2E

Это техническая карта компонентов и проверок, а не история разработки или свидетельство выполненной проверки. Идентификаторы сохранены для совместимости с валидатором пакета.

## Условия готовности

`IMPLEMENTED_PENDING_NATIVE_VALIDATION` обозначает, что статической реализации недостаточно для заявления о готовности: требуется свежая native-проверка в целевой среде. `PENDING_NATIVE` означает отсутствие такой проверки. `STATIC_HARDENING_IMPLEMENTED` описывает только статический слой, не фактическую приёмку. Ни одна строка ниже не заменяет актуальные результаты запуска.

## Карта технических требований

| Task | Status | Result | Remaining external evidence |
| --- | --- | --- | --- |
| `B1` | `IMPLEMENTED` | Browser/E2E capability + safety contract | native capability discovery |
| `B2` | `IMPLEMENTED` | browser/process/port/install/test-data permissions separated | native permission adversarial case |
| `B3` | `IMPLEMENTED` | technical verifier supports repository-native browser E2E | native E2E command |
| `B4` | `IMPLEMENTED` | independent Browser G4 with restricted inputs | native browser G4 |
| `B5` | `IMPLEMENTED` | host-neutral adapters/fallback | active-host evidence |
| `B6` | `IMPLEMENTED` | browser evidence in ledger/dashboard | native projection check |
| `B7` | `IMPLEMENTED` | adversarial evals/docs/static 0.5 integrity wiring | CI observation |
| `B8` | `PENDING_NATIVE` | disposable full-stack web acceptance | required before release claim |


## Проверка перед использованием

- Проверить наличие и связи перечисленных компонентов в текущей версии.
- Выполнить штатные валидаторы и сохранить фактические результаты.
- Не объявлять успешную native-проверку без воспроизводимых свидетельств.
- Сохранять разделение полномочий, безопасности, независимого review и верификации.

[Руководство](../../README.md)
