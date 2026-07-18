# Matreshka Agent

Matreshka Agent — переносимый плагин для разработки с coding agents. Он помогает превратить идею или большую задачу в понятный дизайн, подробный план, небольшие задания для субагентов, проверенную реализацию и итоговый отчёт.

Плагин рассчитан в том числе на людей без опыта программирования. Чтобы начать, не нужно знать структуру проекта, названия файлов или команды тестов: агент сначала исследует репозиторий в безопасном read-only режиме и спрашивает только о решениях, которые нельзя получить из кода.

> Статус: собрана development preview версии `0.1.2`. Архитектура сверена с официальными рекомендациями OpenAI, Anthropic, Cursor, Google Antigravity и Agent Skills на 16 июля 2026 года. Все девять навыков и четыре платформенных манифеста входят в пакет.

## Плагин и навык — простыми словами

- **Плагин** — устанавливаемая «коробка» Matreshka Agent: версия, набор навыков, иконка, документация и проверки.
- **Навык (skill)** — одна инструкция внутри плагина, например брейншторм, планирование или проверка результата.
- **Контроллер** — главный навык, который ведёт работу от идеи до handoff и вызывает остальные навыки.
- **Субагент** — отдельный рабочий контекст для ограниченной роли, например implementer или reviewer.
- **Finding** — замечание reviewer-а с важностью и доказательством.
- **Evidence** — свежий проверяемый результат команды, теста или scoped diff, а не просто фраза агента «всё работает».

Поэтому для одного локального эксперимента достаточно отдельного skill, а для полной переносимой системы удобнее plugin: он устанавливается, обновляется и удаляется как единый пакет на разных coding agents.

## Самый короткий путь для новичка

1. Откройте проект в Codex, Claude Code, Cursor или Antigravity.
2. Запустите `orchestrating-subagent-work` способом, который поддерживает ваша платформа.
3. Опишите результат обычными словами.
4. Если не знаете, какой профиль выбрать, соглашайтесь со сбалансированным.
5. Проверьте предложенный дизайн и план.
6. Разрешайте commit, push, deploy и работу с удалёнными системами только тогда, когда понимаете последствия.

Пример запроса:

```text
Хочу добавить вход через Google. Я не программист.
Сначала изучи проект, объясни варианты простыми словами и порекомендуй режим.
Не делай commit, push, deploy и не меняй удалённую базу без отдельного разрешения.
```

## Как запускать Matreshka Agent

Платформы используют разные официальные способы вызова навыков. В Claude Code, Cursor и Antigravity доступен запуск через `/`. В Codex навыки вызываются через `$`, через меню `/skills` или через `@` в интерфейсах ChatGPT/Codex. Это ограничение самой платформы, а не Matreshka Agent.

| Платформа | Запуск главного контроллера |
| --- | --- |
| Claude Code | `/matreshka-agent:orchestrating-subagent-work` |
| Cursor | `/orchestrating-subagent-work` |
| Antigravity | Наберите `/`, найдите `orchestrating-subagent-work` и выберите его |
| Codex CLI / IDE | `$matreshka-agent:orchestrating-subagent-work` или `/skills` → выбрать навык; optional `/prompts:matreshka-orchestrate` после установки wrapper |
| ChatGPT Work / Codex app | `@Matreshka Agent`, затем выбрать bundled skill; либо `$matreshka-agent:orchestrating-subagent-work` там, где доступен skill picker |

В Claude Code и Codex имя содержит namespace плагина — `matreshka-agent:`. Это защищает от конфликта с навыками других плагинов. Cursor и Antigravity показывают фактическое имя команды в своей slash-палитре; README не должен обещать непроверенный alias.

Автоматическое срабатывание навыка зависит от конкретного coding agent и качества `description`. В версии `0.1.2` нет скрытого session-start hook, поэтому для предсказуемого end-to-end запуска лучше вызывать главный контроллер явно. Автоактивация будет проверяться отдельными trigger evals, но не считается механизмом безопасности.

## Что произойдёт после запуска

Главный контроллер ведёт задачу end-to-end:

1. Проверяет инструкции проекта, Git-состояние, документацию, код и доступные тесты.
2. Уточняет цель, ограничения и критерии готовности.
3. Предлагает формат согласований и фиксирует стартовый permission envelope.
4. При необходимости проводит брейншторм и предлагает 2–3 подхода.
5. Оценивает риск и предлагает один из трёх профилей выполнения.
6. Создаёт design-документ и проходит confirmation gate согласно выбранной автономности.
7. Создаёт подробный implementation plan и карту маленьких задач.
8. Запускает implementer и reviewer с ограниченным контекстом и правами.
9. Контролирует бюджет агентских ходов, findings, тесты и состояние Git.
10. При неудачном исправлении останавливается с `STOP_AND_RESCOPE`, а не запускает бесконечный цикл.
11. Проверяет результат и создаёт понятный итоговый отчёт.

### Сначала — проверка возможностей среды

До выбора профиля контроллер обязан определить, что реально умеет текущая платформа:

- где находится фактический project/repository root, нет ли вложенного repo, submodule или host-managed worktree;
- есть ли Git и является ли рабочее дерево чистым;
- можно ли запускать субагентов;
- можно ли продолжать работу с тем же субагентом, сохраняя его контекст;
- можно ли технически ограничить reviewer режимом read-only;
- доступна ли изоляция через native worktree;
- можно ли выбрать модель или уровень reasoning для отдельной роли;
- можно ли получить время, токены и статус агентского запуска.

Не все capability равны по важности. Отсутствие token counters меняет только точность отчёта о стоимости. Отсутствие resume, безопасной изоляции или технического read-only может менять профиль, а для high-risk работы — блокировать запуск.

Результат preflight фиксируется в ledger. Если нужной возможности нет, контроллер не имитирует её и выбирает один из честных статусов:

| Статус | Что означает |
| --- | --- |
| `FULL_MODE` | Все гарантии выбранного профиля доступны |
| `DEGRADED_MODE` | Работа возможна, но одна или несколько гарантий ослаблены и явно перечислены |
| `INLINE_MODE` | Субагенты недоступны; контроллер выполняет план сам с checkpoints |
| `HANDOFF_REQUIRED` | Для безопасного продолжения нужна другая среда или решение пользователя |

Для auth, RLS, migrations, secrets, payments и production-действий нельзя молча переходить в degraded-профиль. Контроллер останавливается и объясняет, какой гарантии не хватает.

### DESIGN, AUDIT и RECOVERY — не дополнительные профили

Три пользовательских профиля ниже отвечают на вопрос «насколько тщательно выполнять задачу». Внутренние состояния контроллера отвечают на другой вопрос:

- `DESIGN` — превратить идею в подтверждённый дизайн;
- `AUDIT` — найти источник лишних токенов, dispatches или review-loop;
- `RECOVERY` — восстановить работу после обрыва или compaction.

Поэтому пользователь всегда выбирает один из трёх профилей, а контроллер при необходимости входит в `DESIGN`, `AUDIT` или `RECOVERY` сам.

`AUDIT` включается, если задача выходит за оценку времени, приближается к 30–40 минутам без independently reviewable результата, исчерпывает dispatch budget, повторяет full-diff review/tests, меняет несколько subsystems, теряет report или расходует контекст непропорционально diff. Его результат имеет стабильную форму:

```text
PRIMARY_COST_DRIVER
SECONDARY_COST_DRIVERS
TASKS_TO_SPLIT
TASKS_TO_RESCOPE
OPTIMIZED_POLICY
```

Контроллер сначала показывает risk summary, рекомендуемый профиль, его бюджет и недоступные гарантии. В управляемом режиме пользователь подтверждает выбор; при заранее делегированном решении controller выбирает профиль сам и записывает обоснование в ledger. Профиль нельзя незаметно удешевить или усилить посреди задачи: новый риск вне permission envelope вызывает pause и новое решение. Быстрый профиль не предлагается как допустимый override для high-risk границ.

## Три профиля выполнения

### Сбалансированный — рекомендуется по умолчанию

Подходит для большинства задач.

```text
Controller
→ Implementer
→ Combined reviewer
→ тот же Implementer исправляет подтверждённые findings
→ тот же Reviewer проверяет исправление
```

- Не более двух уникальных субагентов на задачу.
- Не более четырёх агентских ходов.
- Только одна fixer-wave.
- Повторный Important/Critical finding приводит к `STOP_AND_RESCOPE`.
- Minor findings не блокируют завершение, если acceptance criteria выполнены.

Слова «тот же Implementer» и «тот же Reviewer» означают продолжение их исходных agent threads, а не создание новых агентов с похожими именами. Если платформа не поддерживает resume/follow-up, контроллер сообщает `DEGRADED_MODE`. В low-risk задаче он может сам применить один небольшой consolidated fix и выполнить controller verification, но не называет это независимым re-review. Для high-risk задачи требуется handoff в среду с поддержкой resume.

Если вы не знаете, что выбрать, выбирайте этот профиль.

### Максимальная скорость

Для маленьких и низкорисковых изменений: документации, fixtures, serializers, типов, локальных тестов и безопасных однофайловых исправлений.

Контроллер выполняет часть проверки самостоятельно. Отдельный reviewer вызывается только при повышенном риске или изменении публичного контракта.

Бюджет на задачу: один implementer, максимум один reviewer, одна fixer-wave и не более четырёх агентских ходов, если reviewer действительно понадобился. Fix выполняет тот же implementer, если resume доступен. При Minor-only изменении controller verification может заменить re-review, но это фиксируется в отчёте.

Не используйте этот профиль для auth, tenant isolation, migrations, persistence, secrets и production configuration.

### Максимальное качество

Для auth, RLS, destructive migrations, tenant isolation, provider secrets, платежей, production handoff и других критичных изменений.

Используются отдельные spec- и security/code-проверки, но findings сначала объединяются. Затем один implementer выполняет одну consolidated fixer-wave.

Бюджет на задачу: максимум три уникальных субагента — implementer, spec reviewer и security/code reviewer — и максимум шесть агентских ходов. Два reviewer-а могут работать параллельно только как независимые read-only роли. После consolidated fix каждый reviewer один раз перепроверяет только свои findings. Повторный Important/Critical приводит к `STOP_AND_RESCOPE`.

Этот профиль дороже и медленнее. Контроллер должен объяснить, почему он необходим.

Если платформа не умеет возобновлять implementer и обоих reviewer-ов, профиль максимального качества не считается доступным: вместо подмены свежими агентами контроллер возвращает `HANDOFF_REQUIRED`.

### Общие пределы для всех профилей

- Субагентам запрещено запускать собственных дочерних агентов.
- Пишущие код агенты работают последовательно; параллельные записи в один checkout запрещены.
- Параллельность допустима прежде всего для независимого read-only исследования, triage или анализа логов.
- Любое расширение scope сначала попадает в adjacent findings, а не исправляется «заодно».
- Одна задача — один independently reviewable change unit, один основной subsystem или security boundary и один focused test cycle.
- Commit может соответствовать одной задаче только после явного разрешения пользователя; отсутствие commit не делает задачу незавершённой, если сохранены точный baseline, scoped diff и handoff.

Лимиты выше относятся к одной задаче. До начала фазы контроллер также фиксирует число одобренных задач, общий потолок dispatches и дорогих проверок. Он не добавляет новую задачу или новую волну агентов молча: изменение task map требует rescope и подтверждения пользователя.

Timeout, malformed report или оборванный agent turn не разрешают бесконечно создавать replacements. Контроллер сначала проверяет partial writes и thread status, затем может сделать один follow-up к тому же агенту в пределах бюджета. Если это невозможно, он возвращает `BLOCKED`, `PARTIALLY_VERIFIED` или `HANDOFF_REQUIRED`. Незапустившийся transport call фиксируется отдельно; начавшийся reasoning turn учитывается в бюджете.

Число файлов используется как сигнал риска, а не как механический закон. Три связанных production-файла могут быть одной задачей, а изменение одного файла с auth и migration может потребовать разделения.

Сильные сигналы `SPLIT_REQUIRED`: несколько независимых acceptance results; migration вместе с runtime; auth вместе с UI; provider вместе с persistence; execution вместе с report assembly; отдельные security- и UX-design boundaries. Объединение допустимо только при одном проверяемом результате и записанном обосновании controller-а.

Severity имеет единый смысл во всех профилях:

| Severity | Решение |
| --- | --- |
| Critical | Блокирует задачу; возможна немедленная остановка по security/data risk |
| Important | Блокирует завершение и входит в единственную fixer-wave |
| Minor | Записывается; не блокирует, если acceptance criteria и policy соблюдены |

Reviewer приводит evidence и не запускает fixer-а. Только controller проверяет finding, объединяет список и решает следующий шаг. Отдельные reviewer-ы не должны перекрывать друг друга без записанного обоснования.

Combined reviewer за один проход проверяет соответствие brief, correctness/code quality, security, tenant/organization isolation, data leakage и достаточность тестов. UX включается только для пользовательского интерфейса. Неприменимые пункты помечаются `N/A` с короткой причиной, а не молча пропускаются.

Если reviewer-ы расходятся по Important/Critical finding, controller проверяет source of truth и counterevidence. Неразрешённое противоречие не усредняется до Minor: задача останавливается для rescope или решения пользователя.

Основные task-statuses:

| Статус | Значение |
| --- | --- |
| `NEEDS_CONTEXT` | Не хватает конкретной информации, которую можно безопасно предоставить |
| `BLOCKED` | Продолжение невозможно без нового решения, права или зависимости |
| `SPLIT_REQUIRED` | В задаче несколько независимых результатов или boundaries |
| `CONTEXT_TOO_BROAD` | Brief, diff или history шире необходимого task context и должны быть сокращены |
| `RECORD_FOR_FUTURE_TASK` | Найдена соседняя проблема вне текущего scope |
| `STOP_AND_RESCOPE` | Fix-budget исчерпан или исходная декомпозиция неверна |
| `PARTIALLY_VERIFIED` | Работа есть, но часть заявлений не доказана |
| `COMPLETE` | Acceptance criteria подтверждены свежими evidence |

## Брейншторм и подробная документация

Брейншторм — стадия `DESIGN`, а не четвёртый профиль выполнения. Он запускается для новой функции, сырой идеи, неоднозначной архитектуры, нескольких возможных решений или рискованного изменения.

Навык `designing-software-work`:

- сначала исследует проект;
- проверяет, не слишком ли велика задача;
- задаёт по одному действительно важному вопросу;
- предлагает 2–3 подхода с компромиссами;
- рекомендует один вариант;
- описывает архитектуру, компоненты, interfaces, data flow, ошибки, security и тестирование;
- не разрешает переход к реализации до подтверждения дизайна пользователем или явно записанного делегирования этого решения controller-у.

Для небольшой задачи дизайн может занимать несколько абзацев. Для критичной задачи он включает threat/risk analysis, migration и rollback strategy.

После confirmation gate design-документ проходит self-review: поиск placeholders, противоречий, неоднозначных требований, неявных remote actions и слишком широкого scope. В управляемом режиме пользователь видит итоговый файл до перехода к плану; в автономном режиме controller сохраняет документ, решение и краткое обоснование в ledger. Сохранение файла не означает автоматический commit, если commit не включён в permission envelope.

`planning-software-work` затем создаёт coverage matrix «требование → задача → проверка» и проверяет plan до Task 1. Каждый task brief содержит Goal, Inputs, Produces, exact allowlist, Non-goals, RED/GREEN, task gate и stop conditions. Если точный путь или команда ещё неизвестны, план требует безопасно обнаружить их перед dispatch, а не выдумывает placeholder.

Пользователь может завершить работу после дизайна или после плана. В управляемом режиме подтверждение документа не означает решение начать реализацию: перед первым write-dispatch остаётся отдельный workflow gate. Если локальная реализация уже входит в стартовый permission envelope, этот gate не запрашивает те же права повторно — пользователь подтверждает только переход к следующей стадии. В автономном режиме решение о таком переходе может быть заранее делегировано для утверждённого scope и фиксируется в ledger.

## Какие навыки входят в плагин

Обычно вручную нужно запускать только главный контроллер. Остальные навыки он подключает по необходимости.

| Навык | Когда запускать вручную |
| --- | --- |
| `orchestrating-subagent-work` | Начать или восстановить полноценную задачу с планированием, субагентами и проверкой |
| `designing-software-work` | Провести только брейншторм и подготовить дизайн без реализации |
| `planning-software-work` | Превратить уже утверждённый дизайн в implementation plan |
| `writing-portable-agent-prompt` | Подготовить переносимый prompt для Codex, Cursor, Claude Code или Antigravity, но не выполнять его |
| `implementing-with-tests` | Реализовать ограниченную задачу через focused RED/GREEN |
| `debugging-systematically` | Найти первопричину ошибки или падающего теста |
| `reviewing-agent-work` | Независимо проверить scoped diff и evidence |
| `verifying-development-work` | Доказать, что заявленный результат действительно работает |
| `finishing-development-work` | Подготовить безопасное завершение ветки или handoff |

## Как собирать версию 0.1.2 без лишней сложности

Все девять навыков — обязательная часть Matreshka Agent. Baseline-first определяет порядок разработки, а не сокращает состав плагина:

1. Сначала фиксируется plain-agent baseline без плагина на небольшом наборе задач.
2. Создаются schemas, trigger cases и минимальные каркасы всех девяти skills.
3. Первым доводится end-to-end slice: controller, дизайн, планирование и portable prompt.
4. Затем реализуются execution, debugging, review, verification и finishing skills.
5. Каждый навык получает собственные positive/negative trigger evals, behavioral cases и понятный самостоятельный output.
6. После поведенческой стабильности добавляются четыре platform manifests и install/update/uninstall tests.
7. Кандидат сравнивается с plain-agent baseline и предыдущей версией Matreshka Agent на одинаковых условиях.

Все девять каталогов и `SKILL.md` должны присутствовать в первом полном release. Evals используются для улучшения границ и descriptions, но не для исключения согласованных навыков из плагина.

## Процессная архитектура Matreshka Agent

Все инструкции, шаблоны и helper scripts пишутся специально для Matreshka Agent. Основные процессные принципы распределяются так:

| Принцип | Где он реализован | Правило Matreshka Agent |
| --- | --- | --- |
| Исследование и дизайн до кода | `designing-software-work` | Глубина документации зависит от риска и неоднозначности задачи |
| Изоляция рабочей области | preflight + `finishing-development-work` | Controller сначала проверяет существующую среду и permission envelope |
| Проверяемый implementation plan | `planning-software-work` | Coverage matrix, маленькие task briefs, exact interfaces и task gates |
| Управляемая работа субагентов | `orchestrating-subagent-work` | Ограниченный context, повторное использование agent threads и одна fixer-wave |
| Выполнение без субагентов | fallback главного controller-а | Честный `INLINE_MODE` без имитации независимого review |
| Реализация через тесты | `implementing-with-tests` | Focused RED/GREEN и явно записанные допустимые исключения |
| Поиск первопричины | `debugging-systematically` | Воспроизведение, evidence, root cause и остановка при исчерпании бюджета |
| Независимая проверка | `reviewing-agent-work` | Consolidated findings, severity, counterevidence и controller adjudication |
| Доказательство готовности | `verifying-development-work` | Свежие команды, exit codes, counts и границы фактически выполненной проверки |
| Безопасное завершение | `finishing-development-work` | Handoff, commit, PR, push, merge и cleanup выполняются только в разрешённом scope |
| Параллельная работа | controller policy | Read-only исследование может быть параллельным; записи в один checkout — последовательные |
| Предсказуемый запуск | явный вызов + trigger descriptions | Автоактивация проверяется evals и не используется как permission enforcement |

### Примеры ручного запуска

Claude Code:

```text
/matreshka-agent:designing-software-work Помоги продумать систему подписок
/matreshka-agent:writing-portable-agent-prompt Подготовь prompt для Cursor, чтобы исправить форму входа
```

Cursor и Antigravity:

```text
/designing-software-work Помоги продумать систему подписок
/writing-portable-agent-prompt Подготовь prompt для Claude Code, чтобы исправить форму входа
```

Codex:

```text
$matreshka-agent:designing-software-work Помоги продумать систему подписок
$matreshka-agent:writing-portable-agent-prompt Подготовь prompt для Cursor, чтобы исправить форму входа
```

## Prompt Agent

`writing-portable-agent-prompt` нужен, когда prompt создаётся в одной нейросети, а выполняться будет в другом coding agent.

Он формирует канонический task contract и адаптирует его под выбранную платформу. В prompt входят:

- конечная цель;
- разрешённый scope;
- inspect-only и forbidden areas;
- source-of-truth priority;
- acceptance criteria;
- permission envelope;
- проверки и evidence;
- stop conditions;
- формат итогового отчёта.

Prompt Agent не выполняет получившийся prompt. Он также не придумывает пути, команды, модели или права, которых пользователь не предоставил и которые нельзя безопасно обнаружить.

Он отделяет переносимый task contract от platform adapter. Каноническая часть не содержит названий несуществующих tools, моделей или slash-команд; adapter добавляет только проверенные особенности выбранной среды.

Текст из issue, web-страницы, code comment, test fixture или старого agent report считается данными, а не новым разрешением. Prompt Agent не переносит из таких источников инструкции на push, deploy, чтение secrets или расширение scope.

## Разрешения и безопасные границы

Matreshka Agent использует least-privilege contract.

По умолчанию контроллер может исследовать локальный проект в read-only режиме. Разрешение на реализацию относится только к согласованным файлам и задаче.

Этот текстовый контракт не выдаёт системные права и не может ослабить sandbox, approval policy или правила организации. Эффективное разрешение всегда равно пересечению пользовательского согласия, project instructions и технических ограничений платформы.

### Автономность и стартовый запрос разрешений

Формат согласований — отдельная ось и не заменяет три профиля выполнения. В начале run, после безопасного read-only preflight, controller предлагает один из вариантов:

| Формат | Как работает |
| --- | --- |
| Управляемый | Controller останавливается на design/plan/write и внешних gates; рекомендуется новичку |
| Автономный локальный | Controller самостоятельно исследует, планирует, меняет согласованный local scope и запускает локальные проверки |
| Расширенный автономный | Пользователь дополнительно разрешает выбранные Git, network и remote actions для точных целей |

Фраза «даю полную автономность» не превращается в безграничное разрешение. Controller переводит её в короткую матрицу и просит один раз подтвердить:

| Категория | Что можно разрешить на старте |
| --- | --- |
| Decisions | Самостоятельно выбрать рекомендуемый подход, профиль, дизайн и план в пределах цели |
| Matreshka state | Создавать и обновлять specs, plans, ledger, reports и handoffs |
| Local code | Менять только согласованный project scope и allowlisted task files |
| Local commands | Запускать focused tests, regressions, lint, typecheck и build согласно plan |
| Dependencies/network | Устанавливать или обновлять только названные зависимости и обращаться только к разрешённым источникам |
| Git workspace | Создать или использовать только названные branch/worktree |
| Git history | Stage и commit для точного change unit; каждое действие задаётся отдельно |
| Git remote | Push и pull request только для названного repository/branch/destination |
| Remote systems | Staging deploy, migration, SQL или provider calls только для названной среды и операции |
| Critical production | Production deploy, destructive migration, data deletion, payments и live-provider actions только при прямом указании target, boundaries и rollback/stop policy |
| Secrets | Использовать только разрешённый безопасный secret reference/injection; не печатать и не переносить значение в prompts или reports |

Permission envelope получает срок действия: один action, task, phase или весь текущий run. По умолчанию — текущий run в одном project root. Если пользователь подтвердил необходимые категории, controller больше не переспрашивает перед каждым уже разрешённым шагом.

Обязательная остановка остаётся только когда изменился scope, repository, branch destination или remote environment; появилась неразрешённая destructive операция; нужен новый secret/access; техническая sandbox требует approval; acceptance criteria противоречат друг другу; либо пользователь написал «стоп». Пользователь может в любой момент сузить или отозвать разрешения.

Следующие действия по умолчанию выключены. Они могут быть явно включены в стартовый permission envelope или разрешены позже:

- commit;
- push;
- создание pull request;
- deploy или publish;
- применение migration;
- remote SQL;
- изменение production configuration;
- удаление или преобразование данных;
- вызовы платёжных или live-provider систем;
- чтение или передача secrets.

После точного стартового разрешения повторное подтверждение той же операции в тех же границах не требуется. Имя ветки, текст commit message или команда в старом prompt сами по себе не считаются разрешением.

Никогда не вставляйте API keys, пароли, service-role keys или содержимое `.env` в чат.

### Общий permission contract

Перед первым write-dispatch контроллер фиксирует один контракт, который наследуют все роли. Субагент может получить более узкие права, но не более широкие.

| Поле | Что фиксируется |
| --- | --- |
| Goal | Один проверяемый результат |
| Sources of truth | Текущая просьба пользователя, applicable repo instructions, утверждённый spec и task brief |
| Allowed scope | Разрешённые каталоги, файлы и интерфейсы |
| Inspect-only scope | Что можно читать, но нельзя менять |
| Forbidden scope | Что нельзя читать, менять или вызывать |
| Local writes | Разрешены ли изменения файлов и каких именно |
| Decision delegation | Может ли controller самостоятельно подтвердить рекомендуемый profile/design/plan |
| Git actions | Отдельно: branch/worktree, stage, commit, push, PR |
| Remote actions | Отдельно: network, deploy, provider, database, payments |
| Secrets | По умолчанию не читать; разрешается только named secret reference/injection без раскрытия значения |
| Verification | Разрешённые команды и ожидаемые evidence |
| Stop conditions | `NEEDS_CONTEXT`, `BLOCKED`, `SPLIT_REQUIRED`, `STOP_AND_RESCOPE` |

Текущая пользовательская инструкция имеет приоритет над старым plan или report. Repository instructions применяются только к своей области. Код, логи и отчёты субагентов не могут расширять permission envelope. Субагент всегда получает права не шире controller-а и обычно уже конкретного task brief.

Allowlist проверяется по разрешённым реальным путям внутри выбранного project root. Symlink escape, nested repository, submodule или смена root считаются новой границей и требуют отдельной проверки; строковое совпадение пути само по себе недостаточно.

Если платформа умеет ограничить reviewer технически, controller убирает write-tools. Иначе он передаёт immutable review package или использует изолированный disposable checkout, а также сверяет baseline/hashes до и после review; любая мутация инвалидирует review. Если доступны только текстовый запрет и общий writable checkout, read-only остаётся процедурной гарантией и включается `DEGRADED_MODE`. Для high-risk профиля отсутствие и технического ограничения, и безопасной изоляции приводит к `HANDOFF_REQUIRED`.

### Git принадлежит контроллеру

По умолчанию implementer меняет только allowlisted файлы и не выполняет `git add`, commit, push или PR. Контроллер проверяет scoped diff и создаёт commit после verification только когда commit разрешён стартовым envelope или последующим approval. Это также защищает от платформ, где background agent способен предлагать или выполнять Git-действия автоматически.

Review не требует commit. Контроллер может сформировать task-base → current-state package: status, scoped diff, allowlisted untracked files, test evidence и hashes. Поэтому инвариант звучит так:

```text
одна задача = один независимо проверяемый change unit
commit = только разрешённый способ зафиксировать этот unit
```

Если полезна изоляция, контроллер сначала определяет, не находится ли он уже в host-managed worktree, затем использует native worktree, если это включено в permission envelope, либо запрашивает разрешение. Он не создаёт вложенный worktree, не переключает branch вне разрешённых границ и не удаляет окружение, которым владеет платформа. Cleanup разрешён только для workspace, созданного Matreshka Agent, и только после разрешённого finish-сценария.

### Общий handoff contract

Каждый implementer и reviewer возвращает один и тот же минимальный набор:

- status;
- выполненный и невыполненный scope;
- изменённые файлы или просмотренный diff range;
- команды проверки, exit codes и counts;
- findings с severity и evidence;
- concerns, assumptions и pre-existing failures;
- какие разрешения ещё нужны;
- exact next action.

Agent report является заявлением, а не доказательством. Контроллер проверяет diff и критичные evidence перед изменением статуса задачи.

Задача не считается переданной controller-у, пока report не записан по ожидаемому пути либо controller не восстановил эквивалентный report из проверенного состояния. В нём обязательно различаются commit hash, если commit был разрешён, и точный uncommitted baseline/current state, если commit не создавался. Missing report не превращается в `COMPLETE`.

Для внешней границы handoff дополнительно фиксирует:

```text
LOCAL_OPERATOR
REMOTE_OPERATOR
REMOTE_SYSTEM
ALLOWED_PREPARATION
FORBIDDEN_EXECUTION
FINAL_STATUS
```

Например, локальный agent может подготовить migration, tests и команды, но не применять remote SQL. Итогом становится `HANDOFF_REQUIRED`, а не ложное `COMPLETE`.

### Общий ledger contract

Ledger — короткий источник состояния controller-а, а не полный transcript. Он имеет версию схемы и хранит:

| Поле | Что нужно для восстановления и аудита |
| --- | --- |
| Identity | `contract_version`, версия Matreshka Agent, `run_id`, время и project root |
| Baseline | Git refs или `NO_GIT_MODE`, исходные dirty files, hashes и владелец изменений |
| Capabilities | Платформа, доступные subagents/resume/read-only/worktree/model routing и честный mode status |
| Decision | Цель, risk summary, подтверждённый профиль и stage gate |
| Permissions | Текущий permission envelope и точный scope каждого отдельного approval |
| Task map | Одобренные задачи, зависимости, текущий task и общий budget |
| Dispatches | Role, stable thread/agent ID, capability tier, turn count, brief/report path и status |
| Review | Findings, adjudication, fixer-wave и результат targeted re-review |
| Verification | Команды, exit codes, counts, relevant notes и pre-existing failures |
| Recovery | Последний безопасный checkpoint, exact next action и stop reason |

В ledger не попадают secrets, скрытые chain-of-thought рассуждения и огромные raw logs. Каждый approval имеет scope и expiry. После recovery controller может продолжить по ещё действующему run-level permission только после сверки project, target и ledger integrity; изменившиеся границы требуют нового подтверждения. Follow-up адресуется по сохранённому agent/thread ID; новое имя роли не считается продолжением прежнего агента.

## Где хранятся документы задачи

Утверждённые документы сохраняются в проекте в version-control-friendly виде, чтобы решения не потерялись и были понятны человеку или другому агенту:

```text
docs/matreshka/
├── specs/       # утверждённый дизайн
├── plans/       # implementation plans
├── decisions/   # только важные ADR
└── handoffs/    # передача работы человеку, агенту или внешней системе
```

Перед первым созданием `docs/matreshka/` или `.matreshka/` controller использует стартовое разрешение на Matreshka state либо один раз запрашивает его. Это разрешение не позволяет менять product code. Если пользователь отказывает, controller работает в памяти или во временной области и честно предупреждает, что recovery между сессиями будет ограничен.

Рабочее состояние хранится отдельно:

```text
.matreshka/runs/<run-id>/
├── ledger.md
├── task-map.md
├── briefs/
├── reports/
└── reviews/
```

`.matreshka/runs/` по умолчанию игнорируется: это технический журнал, а не продуктовая документация. Утверждённые specs, plans и handoffs готовы к version control, но попадают в commit только после разрешения. Для долгой или межплатформенной работы контроллер может предложить сохранить отдельный checkpoint.

Matreshka Agent не должен молча редактировать корневой `.gitignore`. Вместо этого он создаёт локальный `.matreshka/.gitignore`, который игнорирует содержимое `runs/`. Добавление docs или ignore-файла в commit всё равно требует разрешения на commit.

Если проект не использует Git, контроллер включает `NO_GIT_MODE`: сохраняет timestamped baseline, список файлов, hashes и только необходимый scoped snapshot. Он не копирует `.env`, credentials, большие binaries или содержимое forbidden paths, не обещает commit-based review, но сохраняет те же acceptance criteria и handoff.

Ignored run-state может не переноситься между worktrees. Перед platform handoff или переходом в другой checkout контроллер копирует только безопасный итоговый checkpoint в `docs/matreshka/handoffs/` после согласования с пользователем. Secrets и сырые логи туда не попадают.

Вам не нужно вручную редактировать эти файлы. Они нужны, чтобы агент мог восстановиться после обрыва и не повторять завершённую работу.

## Если работа оборвалась

Снова запустите главный контроллер и напишите:

```text
Восстанови последнюю работу Matreshka Agent. Сначала проверь ledger, Git и текущий diff. Ничего не сбрасывай и не повторяй завершённые задачи.
```

Контроллер должен восстановить состояние в таком порядке:

```text
ledger → Git → current report → scoped diff → exact next action
```

Он не должен выполнять `reset`, `clean`, удалять чужие изменения или создавать нового implementer для уже завершённого fragment.

Если рабочее дерево было грязным до запуска, baseline включает перечень исходных изменений. Matreshka Agent не приписывает их себе, не форматирует их «заодно» и не использует destructive cleanup. При пересечении с allowlist контроллер останавливается и просит решение.

## Рекомендации начинающим

### Говорите о результате, а не о файлах

Хорошо:

```text
После регистрации пользователь должен получить письмо и попасть на страницу настройки профиля.
```

Необязательно:

```text
Измени auth.ts, api.ts и компонент формы.
```

Агент сам найдёт подходящие файлы. Указывайте пути только тогда, когда точно знаете границу задачи.

### Сообщайте, что нельзя менять

Например:

```text
Не меняй дизайн страницы и существующий формат API.
```

### Просите объяснять решения простыми словами

```text
Перед реализацией объясни рекомендуемый вариант без сложных терминов и перечисли основные риски.
```

### Не разрешайте внешние действия автоматически

Для первой работы оставьте commit, push, deploy и migration application запрещёнными. После проверки можно дать отдельное разрешение на конкретное действие.

### Если нужна полная локальная автономность

Можно дать разрешения один раз в начале run:

```text
Для текущего project root разрешаю автономный локальный режим до завершения этого run.

Можно самостоятельно:
- выбрать рекомендуемый подход и один из трёх профилей;
- создавать Matreshka specs, plans, ledger, reports и handoffs;
- менять файлы только в утверждённом task map;
- запускать локальные tests, lint, typecheck и build;
- создавать worktree/branch, stage и commit после успешной verification.

Остановись и спроси меня перед:
- расширением scope или новой задачей;
- установкой dependencies и новым network access;
- push, pull request, deploy и remote database actions;
- secrets, destructive operations, payments или production systems.
```

Если нужны push, PR, staging deploy или migration, добавьте их в тот же стартовый envelope с точным repository, branch, environment и operation. Тогда controller сможет выполнить их без повторных вопросов, пока границы не изменились.

### Не выбирайте максимальное качество «на всякий случай»

Для обычной задачи сбалансированный профиль безопаснее по времени и стоимости. Максимальное качество нужно применять по риску, а не из тревоги.

### Проверяйте три вещи перед подтверждением плана

1. Правильно ли описан видимый результат?
2. Есть ли явно перечисленные non-goals?
3. Понятно ли, какие действия потребуют вашего дополнительного разрешения?

### Как остановить работу

Можно в любой момент написать:

```text
Остановись после текущего безопасного шага. Не запускай новых агентов. Сохрани checkpoint и покажи exact next action.
```

Контроллер прекращает новые dispatches, пытается безопасно завершить уже идущую локальную команду или агентский ход, помечает незавершённое состояние и не считает задачу выполненной. В новой сессии используются только ещё действующие run-level permissions, записанные в проверенном ledger; остальные разрешения запрашиваются заново.

### Как понимать стоимость

Перед запуском профиля контроллер показывает простую оценку: число уникальных агентов, максимум агентских ходов, ожидаемые дорогие проверки и причина выбора. Точные токены заранее неизвестны, поэтому нельзя обещать конкретную цену; после работы фактические данные записываются, если платформа их предоставляет.

## Установка

Matreshka Agent распространяется как marketplace-репозиторий с одним общим каталогом skills внутри каталога плагина. Корень репозитория хранит marketplace-файлы, а устанавливаемый plugin root находится в `plugins/matreshka-agent/`:

```text
matreshka-agent/
├── .agents/plugins/marketplace.json
├── .claude-plugin/marketplace.json
├── .cursor-plugin/marketplace.json
├── plugins/
│   └── matreshka-agent/           # устанавливаемый plugin root
│       ├── .codex-plugin/plugin.json
│       ├── .claude-plugin/plugin.json
│       ├── .cursor-plugin/plugin.json
│       ├── plugin.json            # Antigravity CLI
│       ├── skills/
│       │   ├── orchestrating-subagent-work/
│       │   ├── designing-software-work/
│       │   ├── planning-software-work/
│       │   ├── writing-portable-agent-prompt/
│       │   ├── implementing-with-tests/
│       │   ├── debugging-systematically/
│       │   ├── reviewing-agent-work/
│       │   ├── verifying-development-work/
│       │   └── finishing-development-work/
│       ├── evals/                 # end-to-end и cross-platform evals
│       ├── assets/                # визуальные assets после visual pass
│       ├── scripts/
│       │   ├── doctor.py          # read-only диагностика
│       │   └── validate_package.py
│       ├── LICENSE
│       ├── SECURITY.md
│       └── CHANGELOG.md
├── LICENSE
└── README.md
```

Один `SKILL.md` не копируется четыре раза. Платформенные манифесты подключают одно и то же переносимое ядро.

Каждый из девяти skill-каталогов содержит обязательный `SKILL.md`, одноуровневые `references/`, только необходимые output templates в `assets/`, Codex UI metadata в `agents/openai.yaml`, behavioral `evals/evals.json` и отдельный `evals/trigger-evals.json`. Все девять навыков проверяются package validator-ом как обязательные компоненты.

Общий `SKILL.md` использует минимально переносимый frontmatter: только `name` и `description`. Platform-specific поля вроде Cursor `readonly` или Claude agent configuration не помещаются в shared skill. Каждый `name` совпадает с каталогом, `description` проверяется trigger evals, основной файл остаётся короче 500 строк, а подробности загружаются из одноуровневых `references/` только при необходимости.

Версия `0.1.2` не зависит от общего каталога custom `agents/`: форматы и permission-поля платформ различаются, а Codex plugin format не обещает распространять agent definitions как компонент. Controller использует доступный host-native механизм субагентов и platform adapter. Отдельные packaged agent definitions можно добавить позже только после cross-platform evals.

### Рекомендуемая установка для новичка

Основной путь — встроенный marketplace или plugin manager каждой платформы. Это проще обновлять и удалять, а coding agent сам показывает, что именно устанавливается. Собственный `install.py` в версии `0.1.2` не нужен: он добавил бы ещё один исполняемый компонент и зависимость от Python.

`plugins/matreshka-agent/scripts/doctor.py` только проверяет установку и печатает понятные подсказки. Он не меняет пользовательские настройки, не создаёт links и не устанавливает hooks. Ручные developer-инструкции ниже нужны для локального тестирования и troubleshooting.

Оба helper script должны работать без network, предпочитать Python standard library и иметь dry/read-only поведение по умолчанию. Плагин не должен запускать package-manager install во время обычного использования.

### Codex

Для локальной проверки добавьте корень marketplace-репозитория:

```bash
codex plugin marketplace add /absolute/path/to/matreshka-agent
codex plugin marketplace list
```

Для Codex CLI запустите новую сессию:

```bash
codex
```

Внутри Codex CLI откройте `/plugins`, выберите marketplace **Matreshka Agent** и установите плагин. Затем откройте список навыков:

```text
/skills
```

Выберите namespaced skill или напишите `$matreshka-agent:orchestrating-subagent-work` в prompt.

Если привычнее slash-команда, установите один раз необязательные wrappers из `plugins/matreshka-agent/codex-prompts/` в локальный каталог Codex:

```bash
mkdir -p ~/.codex/prompts
cp /absolute/path/to/matreshka-agent/plugins/matreshka-agent/codex-prompts/*.md ~/.codex/prompts/
```

Затем начните новую задачу или в VS Code выполните `Developer: Reload Window`. Главный shortcut будет `/prompts:matreshka-orchestrate`. Это совместимый local custom prompt, а не неподдерживаемый plugin `commands/` component; он не добавляет прав или автоматических действий. Codex считает custom prompts устаревающим compatibility mechanism, поэтому для новой работы по возможности используйте `$skill` или `/skills`.

В ChatGPT desktop/web используйте визуальный интерфейс Plugins, а не CLI-команду `/plugins`. После публикации вместо локального пути можно будет использовать закреплённый Git repository/ref; точный owner появится только перед релизом.

### Claude Code

Для локального тестирования без установки:

```bash
claude --plugin-dir /absolute/path/to/matreshka-agent/plugins/matreshka-agent
```

Для постоянной установки через marketplace выполните внутри Claude Code:

```text
/plugin marketplace add /absolute/path/to/matreshka-agent
/plugin install matreshka-agent@matreshka-agent
/reload-plugins
```

Первый запуск:

```text
/matreshka-agent:orchestrating-subagent-work
```

### Cursor

После публикации найдите **Matreshka Agent** в `Customize → Plugins` или Marketplace и нажмите Install.

Для локального тестирования на macOS/Linux разместите или создайте ссылку на репозиторий в:

```text
~/.cursor/plugins/local/matreshka-agent
```

На Windows локальный путь имеет вид:

```text
%USERPROFILE%\.cursor\plugins\local\matreshka-agent
```

После этого перезапустите Cursor или выполните `Developer: Reload Window`.

Копируйте или связывайте с этим путём каталог `plugins/matreshka-agent/`, чтобы `.cursor-plugin/plugin.json` находился непосредственно внутри установленного plugin root.

Первый запуск в Agent chat:

```text
/orchestrating-subagent-work
```

### Antigravity

Установка локального или скачанного пакета:

```bash
agy plugin install /absolute/path/to/matreshka-agent/plugins/matreshka-agent
agy plugin list
```

Запустите Antigravity CLI, наберите `/`, найдите `orchestrating-subagent-work` и выберите показанную команду. Antigravity автоматически преобразует зарегистрированные skills в slash-команды TUI.

Если используется только формат Agent Skills без плагина, глобальные навыки можно разместить в `~/.gemini/config/skills/`, а проектные — в `<project-root>/.agents/skills/`. Для полного Matreshka Agent рекомендуется plugin installation, потому что она сохраняет единый пакет и версию.

### Обновление и удаление

- Codex: откройте `/plugins`; обновите marketplace при необходимости, затем обновите или удалите Matreshka Agent в plugin browser.
- Claude Code: используйте `/plugin` для Update, Disable или Uninstall; после update выполните `/reload-plugins`.
- Cursor: откройте `Customize → Plugins`, затем Update, Disable или Uninstall.
- Antigravity: используйте plugin manager/CLI вашей установленной версии; перед релизом точные команды должны быть повторно проверены через `agy plugin --help`.

После update начинайте новую задачу или перезагружайте plugins согласно платформе. Уже запущенный агентский thread может продолжать использовать старую версию инструкций; не смешивайте две версии внутри одной критичной задачи.

Версия плагина записывается в ledger. Для критичной работы update не выполняется посреди run; release process должен поддерживать установку закреплённой предыдущей версии для rollback, если новая версия не проходит compatibility или behavioral evals.

## Почему в первой версии нет hooks

Hooks выполняют команды автоматически в определённые моменты жизненного цикла. Ошибка в hook может мешать работе во всех задачах, поэтому версия `0.1.2` не устанавливает их.

Сначала мы проверим поведение навыков через evals. Hook будет добавлен только для повторяющейся ошибки, которую нельзя надёжно устранить инструкцией или детерминированным helper script.

Будущий hook должен быть opt-in, минимальным, без network/secrets по умолчанию, иметь тесты и понятный способ отключения. Hook не должен выдавать prompt-рекомендацию за реальное permission enforcement: платформенная sandbox/approval policy остаётся главным техническим ограничением.

## Зачем нужен `assets/`

В корневом `assets/` лежит оформление самого плагина. Для Matreshka Agent будет один оригинальный знак: вложенные формы, напоминающие матрёшку и одновременно agent handoff/слои контроля. `SVG`, `PNG` и logo-export — это технические варианты одного дизайна, а не разные иконки.

Master-знак должен оставаться узнаваемым в 16–32 px, работать на светлом и тёмном фоне, не зависеть от мелкого текста и иметь монохромный fallback. Перед экспортом проверяются safe area, контраст и точные размеры каждого marketplace.

`assets/` внутри отдельного skill используется иначе: только для шаблонов, которые skill копирует в результат, например task brief или handoff template. Документацию для агента нужно хранить в `references/`, а не в `assets/`.

Для главного controller-а минимальный набор будет таким:

```text
skills/orchestrating-subagent-work/
├── SKILL.md
├── references/
│   ├── controller-contract.md
│   ├── profiles-and-budgets.md
│   ├── permission-handoff-ledger.md
│   └── platform-adapters.md
├── assets/
│   ├── task-brief-template.md
│   ├── ledger-template.md
│   ├── agent-report-template.md
│   └── review-package-template.md
└── evals/evals.json
```

Правила сопоставления capability tiers с реально доступными моделями находятся в `platform-adapters.md`, а не в переносимом `SKILL.md`. Конкретные названия моделей намеренно не закреплены: controller проверяет активную платформу и записывает фактическое сопоставление в ledger перед dispatch. Шаблоны используют только Matreshka run paths, которые создаются для конкретной задачи.

## Evals и контроль качества

Evals проверяют отдельно активацию и фактическое поведение. У каждого skill есть `evals/evals.json`, совместимый с текущим Anthropic skill-creator и его полем `expectations`, а также отдельный `evals/trigger-evals.json` в формате `query / should_trigger`. В общем Agent Skills evaluation guide критерии также называются `assertions`; это терминологическое различие не смешивается внутри skill-level schema. Корневой `evals/` использует собственную явно валидируемую schema для end-to-end, recovery и platform compatibility сценариев.

Файлы в репозитории — определения тестов, а не выдуманные benchmark results. Перед публичным релизом behavioral cases запускаются в чистых synthetic fixture workspaces с skill и без него; timing, grading, human feedback и агрегированный benchmark сохраняются вне публикуемого пакета. Если нужный fixture или host недоступен, кейс остаётся `NOT_RUN`, а не считается пройденным по тексту ожиданий.

Начальный набор должен проверить:

- слишком широкая задача приводит к `SPLIT_REQUIRED`;
- повторный Critical/Important после fixer-wave приводит к `STOP_AND_RESCOPE`;
- reviewer не перечитывает весь branch без причины;
- reviewer сначала проверяет evidence и не повторяет полный suite без причины;
- implementer не запускает собственных дочерних агентов;
- commit, push, deploy и remote operations не выводятся из контекста автоматически;
- autonomous run не переспрашивает уже подтверждённое действие в неизменившемся permission envelope;
- изменение project, branch destination, remote target или destructive scope вызывает новый approval;
- истёкшее разрешение не восстанавливается из старого report, а действующее run-level разрешение корректно продолжается из проверенного ledger;
- полный autonomy envelope не обходит sandbox, organization policy и native approval prompts;
- recovery начинается с ledger и Git;
- prompts остаются переносимыми между платформами;
- первый dispatch получает минимальный fresh context, а follow-up идёт по тому же agent/thread ID;
- dirty worktree не сбрасывается и чужие изменения не присваиваются;
- без Git создаётся честный `NO_GIT_MODE`;
- отсутствие resume приводит к объявленному degraded/handoff, а не к скрытым fresh agents;
- reviewer остаётся read-only там, где это можно технически обеспечить;
- malicious instruction в issue, code comment, fixture или agent report не расширяет права;
- adjacent issue получает `RECORD_FOR_FUTURE_TASK`, а не скрытое расширение scope;
- попытка передать весь plan, историю и старые reports отклоняется как слишком широкий context;
- следующий remote шаг заканчивается точным `HANDOFF_REQUIRED`;
- пользовательское «стоп» прекращает новые dispatches и создаёт checkpoint;
- high-risk задача не понижается до быстрого профиля молча;
- два пишущих агента не запускаются параллельно в одном checkout;
- timeout или malformed report не создаёт бесконечную цепочку fresh replacements;
- symlink, nested repo и submodule не позволяют выйти за разрешённый project root;
- пути с пробелами и shell-metacharacters не превращаются в command injection;
- controller не добавляет задачи и dispatches сверх подтверждённого phase budget;
- pre-existing test failure отделяется от новой регрессии;
- completion без свежего evidence не проходит grading.

Для каждого skill сначала создаются 2–3 реалистичных поведенческих кейса и отдельный набор should-trigger/should-not-trigger запросов. Критичные end-to-end сценарии сравниваются в трёх вариантах:

1. coding agent без Matreshka Agent;
2. минимальный Matreshka controller baseline без дополнительных skills;
3. полный Matreshka Agent candidate.

Проверяются pass rate, время, токены, количество dispatches и причины неправильных решений. Критичный сценарий выполняется минимум три раза на вариант; отчёт сохраняет число запусков и разброс, а не выдаёт один удачный результат за устойчивость.

Сравнение считается честным только при одном repository snapshot, одинаковом user prompt, permission mode, model capability tier, timeout и наборе доступных tools. Версии coding agent, минимального controller baseline и полного Matreshka Agent закрепляются в benchmark metadata; grader не знает, какой вариант создал output.

Также измеряются число уникальных субагентов, число review/fix waves, permission violations, доля неподтверждённых claims и качество recovery. Каждый запуск начинается в чистом контексте. Results/workspaces не входят в публикуемый plugin package; после реальных прогонов в репозитории могут оставаться только определения кейсов, агрегированные benchmarks и одобренные synthetic/open fixtures без proprietary code, персональных данных и secrets. Пока native-прогоны не выполнены, definitions имеют статус `NOT_RUN` по смыслу и не являются результатами.

Перед релизом обязательны blind A/B предыдущей и новой версии, human review фактических outputs и повторный прогон после каждого изменения controller contract.

## Контекст, модели и стоимость

Matreshka Agent не закрепляет в переносимом ядре названия конкретных моделей. Платформа может переименовать модель, запретить её политикой команды или заменить недоступную модель fallback-вариантом.

Контроллер выбирает capability tier:

- fast/economical — read-only exploration и механические low-risk задачи;
- standard — обычная реализация с ясным plan;
- high-judgment — security, architecture, auth, persistence, migrations и critical review.

Если critical role не получила нужный capability tier, это отражается в ledger и может привести к `HANDOFF_REQUIRED`. Максимальный reasoning не включается «на всякий случай».

Рекомендуемые пределы контекста:

- task brief: обычно 800–1 500 слов, hard limit 2 000;
- controller dispatch: 300–500 слов плюс пути;
- agent report: 500–800 слов;
- reviewer: task brief, report, scoped review package и test summary — без истории предыдущих задач и полного raw output.

Первый subagent dispatch создаётся в изолированном fresh context. В Codex adapter это означает `fork_turns: "none"`; на других платформах используется проверенный эквивалент, если он есть. Исправление и re-review — follow-up к сохранённым thread IDs, а не повторная передача всей истории свежему агенту.

## Проверки и evidence

Проверки делятся на три уровня:

1. Focused cycle: RED → минимальная реализация → GREEN.
2. Task gate: task suite, 1–3 ближайших regressions, targeted typecheck/lint и diff check, если применимо.
3. Phase/final gate: интеграционные проверки, build и более широкий suite один раз в подходящей точке.

После fixer-wave запускаются covering test и ближайшая regression, а не весь suite без причины. Security/secret scan и build выполняются только для затронутых путей или когда этого требует project policy.

Evidence всегда записывается как `command / exit code / pass-fail counts / relevant note`. Огромный raw log не копируется в main context. Если проверку запустить нельзя, итоговый статус — `PARTIALLY_VERIFIED` или `BLOCKED`, но не `COMPLETE`.

Pre-existing failure сначала воспроизводится на baseline, если это безопасно и практически возможно. Если принадлежность сбоя нельзя доказать, controller помечает неопределённость и не объявляет её ни новой регрессией, ни исправленной проблемой без evidence.

## Release gate

Перед первым публичным релизом должны быть закрыты все пункты:

- одинаковый `name`, корректные skill paths и версия `0.1.2` во всех манифестах, чья актуальная schema поддерживает поле version;
- наличие всех девяти обязательных skill-каталогов, их trigger descriptions и `evals/evals.json`;
- Agent Skills validation каждого `SKILL.md`;
- native plugin validation для Codex, Claude Code, Cursor и Antigravity;
- чистая установка, первый запуск, update, disable и uninstall на каждой платформе;
- отсутствие hooks, MCP servers, telemetry и secret requirements в `0.1.2`;
- выбранная владельцем лицензия и publisher/GitHub owner вместо placeholders;
- повторная проверка доступности display name и ID `matreshka-agent`; отсутствие результатов поиска не заменяет trademark review;
- marketplace metadata, legal/privacy links и asset sizes, если их требует площадка публикации;
- `SECURITY.md` и release changelog;
- baseline, trigger, behavioral, adversarial и recovery evals;
- проверка ссылок, manifests, asset paths и одинаковой версии через `validate_package.py`;
- package scan на secrets, неожиданные executables, broken/symlink escapes и незаявленные network/dependency requirements;
- SemVer, pinned-version install и rollback smoke test;
- опубликованные ограничения: auto-trigger best-effort, platform capabilities различаются.

До закрытия release gate README не должен называть plugin «готовым к установке».

## Частые проблемы

### Навык не появился после установки

- Начните новую сессию.
- Claude Code: выполните `/reload-plugins`.
- Codex: откройте `/plugins`, убедитесь, что плагин включён, затем начните новую задачу.
- Cursor: выполните `Developer: Reload Window` и проверьте `Customize → Skills`.
- Antigravity CLI: выполните `/skills` или `agy plugin list`.

### Slash-команда не работает в Codex

`/orchestrating-subagent-work` не является командой Codex: `/` показывает только встроенные команды и custom prompts. Используйте `/skills`, `$skill-name` или `@Matreshka Agent` в поддерживаемом интерфейсе. Если нужен именно slash-вызов, явно скопируйте bundled `codex-prompts/*.md` в `~/.codex/prompts/`, перезагрузите VS Code и используйте `/prompts:matreshka-orchestrate`.

### Платформа не умеет запускать нужных субагентов

Контроллер должен сообщить об ограничении и предложить inline execution без имитации независимого review. Он не должен утверждать, что независимая проверка выполнена, если отдельного контекста не было.

### Платформа запускает субагента, но не умеет продолжить тот же thread

Это отдельное ограничение. Сбалансированный профиль переходит в объявленный `DEGRADED_MODE`; профиль максимального качества требует handoff. Создание свежего fixer/reviewer не должно скрываться под словами «тот же агент».

### Контроллер предлагает слишком дорогой режим

Попросите:

```text
Покажи оценку риска и объясни, какое конкретное условие требует максимального качества.
```

### Агент просит секрет

Не отправляйте его. Попросите подготовить переменную окружения, handoff или инструкцию для локального оператора без вывода значения секрета.

## Совместимость

Инструкции сверены с официальной документацией по состоянию на **16 июля 2026 года**:

- [OpenAI: Build skills](https://developers.openai.com/codex/build-skills)
- [OpenAI: Build plugins](https://developers.openai.com/codex/build-plugins)
- [OpenAI: Subagents](https://developers.openai.com/codex/subagents)
- [Agent Skills: Specification](https://agentskills.io/specification)
- [Agent Skills: Evaluating skills](https://agentskills.io/skill-creation/evaluating-skills)
- [Anthropic: Claude Code skills](https://code.claude.com/docs/en/skills)
- [Anthropic: Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Anthropic: Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Cursor: Agent Skills](https://cursor.com/docs/skills)
- [Cursor: Plugins](https://cursor.com/docs/plugins)
- [Cursor: Subagents](https://cursor.com/docs/subagents)
- [Google: Agent Skills in Antigravity](https://antigravity.google/docs/skills)
- [Google: Antigravity Plugins & Skills](https://antigravity.google/docs/cli/plugins)

Форматы coding agents продолжают развиваться. Перед каждым релизом platform adapters и команды установки должны проходить отдельную compatibility-проверку.

## Главный принцип

```text
Понятная цель
× маленькие independently reviewable задачи
× ограниченный контекст
× правильные разрешения
× один implementer
× один consolidated review
× максимум одна fixer-wave
× проверяемые evidence
× устойчивый ledger
× честный capability/degraded status
= управляемая разработка с coding agents
```
