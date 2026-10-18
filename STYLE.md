# Правила API

1. Версия API всегда в URL: `/v1`.
2. Эндпоинты — существительные во множественном числе в kebab-case: `/books/{id}`; действия вне CRUD — `POST /loans/{id}/return`.
3. Поля JSON и query-параметры — snake_case: `due_date`.
4. `operationId` — camelCase, глагол + ресурс: `getBook`, `listLoans`, `createReader`.
5. Все ошибки возвращаются в едином формате `ErrorResponse` с `code` и `message`.
6. `POST /loans` требует заголовок `Idempotency-Key`, ключ хранится 24 часа.
7. Списки поддерживают фильтры, `sort` по возрастанию и пагинацию `limit`/`offset`.
