# Django Celery File Processing Template

### Запуск проекта
    sudo docker-compose up --build -d
    sudo docker-compose up

### Информация о проекте
    - Проект запускается на порту 8000.
    - На порту 5555 запускается Flower для мониторинга Celery http://127.0.0.1:5555/.
    - Эндпойнты задокументированны в Swagger. Можно посмотреть по адресу http://127.0.0.1:8000/swagger/
    - Добавлены эндпойнт для получения списка файлов с пагинацией http://127.0.0.1:8000/api/v1/files/paginated_files/
    - Для просмотра отдельного объекта по id можно использовать http://127.0.0.1:8000/api/v1/files/file/1/
    - При обработке в текстовые файлы с расширением TXT добавляется строка текста, а картинки с расширением JPG уменьшаются до 128х128 пикселей.