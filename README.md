# fast_api_project

[https://github.com/mahenzon/ri-sdk-python-wrapper/blob/master/ri_sdk_codegen/utils/case_converter.py](https://github.com/mahenzon/ri-sdk-python-wrapper/blob/master/ri_sdk_codegen/utils/case_converter.py) - скрипт конвертирования camel_case в snake_case (название класса модели в название таблицы)


Для запуска контейнера Postqresql(c нашей базой) создайте файл .env в том же каталоге что и файл  development.docker-compose.yaml 
следующего содержания:

```
# PostgreSQL
_POSTGRES_CONTAINER_NAME=postgres_container_my_app
_POSTGRES_DB=my_database
_POSTGRES_USER=my_user
_POSTGRES_PASSWORD=my_password
_POSTGRES_PORT=5432
# PGAdmin
_PGADMIN_DEFAULT_EMAIL=admin@example.com
_PGADMIN_DEFAULT_PASSWORD=admin_password
_PGADMIN_LISTEN_PORT=8080
```
