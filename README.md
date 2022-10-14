# fast api

## local start

```
$ docker-compose up
```

http://localhost:8888

- if you want to start with Swagger

http://localhost:8888/docs#

## create migration file

```
$ docker-compose run api bash
# cd /usr/src/app/db
# alembic revision --autogenerate -m 'xxxxx'
```

## run migration

```
# alembic upgrade head
```

## other

create envfile as root

```
.env.development

MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=password
MYSQL_HOST=db
MYSQL_DATABASE=python_fastapi
PYTHONPATH=/usr/src/app/app
```
