# Итог и передача — <задача, этап или ветка>

## Итоговый статус

- Результат: `<FINISHED_LOCAL | FINISHED_COMMITTED | FINISHED_REMOTE | HANDOFF_REQUIRED | PARTIALLY_VERIFIED | BLOCKED>`
- Корень проекта: `<resolved root или NO_GIT_MODE>`
- Базовое/текущее состояние: `<refs, commit или hashes>`
- Проверенное состояние совпадает с текущим: `<да/нет + доказательство>`
- Использованный permission envelope: `<scope и срок действия>`
- Пользовательский режим: `<INTERVIEW | ASSISTED | FULL_AUTO | NOT_APPLICABLE>`
- Профиль выполнения: `<выбранный профиль и источник решения>`
- Эффективные полномочия: `<точные local / Git / browser / runtime / remote / secret / destructive capabilities>`
- Последняя подтверждённая точка: `<путь отчёта, identity состояния и время при наличии>`
- Progress / ledger identity: `<пути и совпадающие идентификаторы>`

## Что доставлено

- Выполнено: `<результаты acceptance>`
- Не выполнено: `<оставшиеся результаты>`
- Файлы задачи: `<точные пути>`
- Сохранённые исходные dirty-файлы: `<пути или нет>`
- Сгенерированные/неизвестные файлы оставлены без изменений: `<пути или нет>`
- Context / ADR / progress: `<точные пути или не создавались>`
- Project Intelligence: `<topology status, areas, IC IDs, runtime/docs state или not applicable>`
- Делегированные решения: `<решение, обоснование, обратимость или нет>`
- Допущения: `<допущение, источник/статус или нет>`
- Неразрешённые placeholders: `<элемент, влияние на acceptance, владелец решения или нет>`
- Остаточные риски: `<риск, доказательство, владелец или нет>`

## Доказательства качества

- Решение review: `<решение и blocking findings>`
- Technical/security verification: `<вердикт>`
- Browser/E2E, если применимо: `<framework/mode, counts, Browser G4, evidence refs>`
- G4 blind acceptance, если применимо: `<PASS/PARTIAL/FAIL/BLOCKED/HANDOFF_REQUIRED>`
- Documentation drift gate: `<DOCS_NOT_REQUIRED | DOCS_CURRENT | DOCS_UPDATE_REQUIRED | DOCS_BLOCKED | DOCS_CONFLICT>`
- Ключевые свежие проверки: `<command/interaction / exit/signal / counts / note>`
- Непроверенные критерии: `<список или нет>`

## Наблюдаемость

- Общее время: `<точное wall-clock elapsed или Недоступно>`
- Время implementation/fix/reverify: `<точное/частичное или Недоступно>`
- Токены: `<EXACT total | PARTIAL observed | Недоступно>`
- Агентные/controller ходы: `<count>`
- Ограничения метрик: `<source/semantics или нет>`

Не оценивай недоступные токены или время по длине текста, количеству сообщений или памяти агента.

## Выполненные действия

| Действие | Точная цель | Доказательство |
| --- | --- | --- |
| `<stage/commit/push/PR/merge/deploy/none>` | `<paths/repository/branch/environment>` | `<result/ref/status>` |

## Внешняя передача, если нужна

- Локальный оператор: `<operator>`
- Удалённый оператор: `<operator>`
- Удалённая система: `<system + exact environment>`
- Разрешённая подготовка: `<artifacts/commands prepared>`
- Не выполнено из-за границ полномочий: `<actions not performed>`
- Шаги проверки: `<exact steps + expected result>`
- Rollback/stop policy: `<policy>`

## Продолжение

- Minor findings: `<список или нет>`
- Соседние будущие задачи: `<список или нет>`
- Допущения/опасения: `<список или нет>`
- Pre-existing failures: `<список или нет>`
- Ещё требуемые разрешения: `<список или нет>`
- Выполненная cleanup: `<owned targets + evidence или нет>`
- Точное следующее действие: `<один следующий шаг или нет>`
