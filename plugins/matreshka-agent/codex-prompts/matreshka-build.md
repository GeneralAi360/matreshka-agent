---
description: Разработка нового или существующего проекта через безопасный end-to-end workflow Matreshka Agent
argument-hint: "[TASK]"
---

Используй $$matreshka-agent:building-end-to-end для этой задачи.

Запрос: $ARGUMENTS

Режимы:
- `interview` — сначала подробно опросить по продукту, по одному важному вопросу за раз;
- `assisted` — задавать только важные вопросы; режим по умолчанию;
- `full-auto` — самостоятельно принимать безопасные обратимые локальные технические решения.

Сценарии существующего проекта:
- `continue-project` — продолжить проект, который уже разрабатывался с Matreshka;
- `existing-project` — подключить Matreshka к существующему проекту, который раньше разрабатывался без неё.

Можно написать, например: `full-auto Создай локальную CRM`, `continue-project Добавь Telegram` или просто описать задачу — сценарий будет определён по read-only анализу репозитория.

Если пользователь не указал сценарий, определи его по read-only анализу репозитория. Не смешивай сценарий запуска, пользовательский режим, execution profile, внутреннюю автономность controller и permissions. Ни один режим или сценарий не даёт автоматически Git, network, secrets, provider, deploy, destructive или remote authority. Реальный workflow передавай только namespaced controller Matreshka Agent; сохраняй source-intent traceability, security, review, technical verification и G4 blind acceptance. Если одну надёжную specification для задачи построить нельзя, остановись с `DECISION_MAP_REQUIRED`.
