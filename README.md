# Библиотека API

Спецификация REST API библиотеки в формате OpenAPI 3.1: `openapi.yml`.

Ресурсы:

- `/books` — книги
- `/readers` — читатели
- `/loans` — выдачи книг, возврат через `POST /loans/{id}/return`

Базовый URL: `https://library.api.com/v1`.

Правила проектирования API — в `STYLE.md`, проверка по чеклисту — в `REVIEW.md`.
