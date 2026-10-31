# Учёт заказов кофейни

Сервис на FastAPI для создания и управления заказами в памяти процесса.

Документация API: http://127.0.0.1:8000/docs

## Настройки

Переменные в `.env` (шаблон — `.env.example`):

- `APP_NAME`, `DESCRIPTION`, `VERSION` — метаданные приложения
- `CONTACT_NAME`, `CONTACT_EMAIL` — контакт в OpenAPI и `/info`
- `DEFAULT_PAGE_SIZE`, `MAX_PAGE_SIZE` — пагинация для `GET /orders`

## Правки
В новой версии добавлено разбиение на слои