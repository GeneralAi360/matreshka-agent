# Интеграция Context Optimizer

Используй этот контракт для вызова отдельного peer skill `$context-optimizer` и для проекции его компактного состояния в Matreshka Agent.

## Источник

Канонический peer skill: `GeneralAi360/Matreshk-context-optimizer` (репозиторий может быть переименован позже). Matreshka не копирует runtime-код optimizer внутрь controller context и не устанавливает его молча.

## Обнаружение peer skill

Предпочтительный порядок:

1. `MATRESHKA_CONTEXT_OPTIMIZER_HOME`;
2. project-local `.agents/skills/context-optimizer`;
3. project-local `.claude/skills/context-optimizer`;
4. project-local `.gemini/skills/context-optimizer`;
5. package-local `skills/context-optimizer`;
6. пользовательские skill directories;
7. sibling development checkout.

Нативный resolver:

~~~bash
python3 -B <plugin-root>/scripts/context_optimizer_peer.py --project <project-root>
~~~

Он не использует сеть, не устанавливает dependencies и не меняет Git.

Если peer skill отсутствует: `contextOptimizer.status=UNAVAILABLE`, dashboard сообщает по-русски, а Matreshka продолжает работу без выдуманных данных.

## Команды

Matreshka вызывает тот же интерфейс, что и пользователь:

~~~text
start     — baseline нового проекта
adopt     — первичный аудит готового проекта
resume    — перепроверка после паузы
check     — событийная проверка перегрузки
status    — текущее состояние
optimize  — план оптимизации без mutation
~~~

Через resolver:

~~~bash
python3 -B <plugin-root>/scripts/context_optimizer_peer.py \
  --project <project-root> \
  --execute \
  --trigger-mode <mode> \
  --trigger-reason "<причина>" \
  --automatic \
  <command>
~~~

`--execute` допустим только когда local-process authority уже существует. Если её нет, resolver возвращает `READY_TO_RUN` с точной командой; это не разрешение выполнить её.

## Автоматический алгоритм

### Новый проект

После определения project root и первичной структуры, но до массового implementation fan-out:

~~~text
NEW_PROJECT + baseline отсутствует → start
~~~

### Готовый проект

После bounded read-only orientation и до архитектурных/массовых изменений:

~~~text
EXISTING_PROJECT + baseline отсутствует → adopt
~~~

### Продолжение

При восстановлении run:

~~~text
resume + (baseline отсутствует OR audit старше 24 ч) → resume
~~~

### Событие перегрузки

`check` запускается только при evidence:

- `CONTEXT_TOO_BROAD`;
- 3+ повторных чтения одного файла;
- 2+ compaction;
- tool results >= 64 КБ и >= 35% отслеживаемого ingress;
- рост static instructions >= 16 КБ;
- изменился набор skills;
- изменилась MCP/tool конфигурация;
- структура проекта изменилась минимум на 100 файлов.

Без нового evidence полный аудит не запускается. Не вызывать optimizer на каждом сообщении или каждом tool call.

## Compact state

~~~text
contextOptimizer.status
contextOptimizer.health
contextOptimizer.healthBasis
contextOptimizer.runtimeMeasurement.*
contextOptimizer.staticContext.*
contextOptimizer.staticRisk
contextOptimizer.projectMap.state
contextOptimizer.projectMap.pressure
contextOptimizer.projectMap.files
contextOptimizer.projectMap.areas
contextOptimizer.topFindings[]
contextOptimizer.recommendations[]
contextOptimizer.ledger.pendingVerification
contextOptimizer.ledger.rollbackRecommended
contextOptimizer.trigger.mode
contextOptimizer.trigger.reason
contextOptimizer.trigger.automatic
contextOptimizer.approvalRequired
~~~

## Инварианты

1. Runtime tokens и static bytes — разные измерения.
2. `CURRENT_CONTEXT` показывается только при доказанной семантике.
3. `UNKNOWN` не превращается в число из bytes, времени, turn count или context-window size.
4. `contextOptimizer.runtimeMeasurement` не прибавляется к Matreshka `usage.totalTokens`.
5. Bridge/dashboard — projection only; они не дают права на mutation.
6. Raw telemetry и большие отчёты остаются вне always-on controller context.
7. `approvalRequired=true` означает, что изменение ещё не разрешено.
8. Pending verification не считается успешной оптимизацией.

## Dashboard

Показывать отдельный раздел/навигационную вкладку **«Контекст»** с понятными русскими формулировками: состояние, измеренный runtime context, статические инструкции, карта проекта, главные проблемы, причина последней проверки, ожидающая проверка, откат и необходимость подтверждения.
