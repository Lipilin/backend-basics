# Ревью openapi.yml

1. Path — существительные, множественное число, kebab-case.
2. Нет глагольных URL, кроме POST /loans/{id}/return.
3. id ресурса в path, фильтры в query.
4. Версия API указана в servers: /v1.
5. POST создания возвращает 201 + Location — исправлено.
6. DELETE возвращает 204 без тела.
7. Пустой список — 200 + пустой data, не 404.
8. Все ошибки используют один ErrorResponse.
9. Для 422 есть example с details — исправлено.
10. На коллекциях есть фильтры, сортировка и пагинация.
11. limit имеет default и maximum — исправлено: default 20, maximum 100.
12. Общие схемы подключены через $ref.
13. Файл валидируется без ошибок.
14. loaned_at, returned_at, registered_at помечены readOnly.
15. У POST /loans тело запроса обязательно.
16. POST /loans/{id}/return возвращает обновлённую выдачу.
