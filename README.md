# fast api

Python,FastAPI,Docker,Mysql,MariaDB

## local start

```
$ docker-compose up
```

http://localhost:8888

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

## DB access

```
$ docker-compose run api bash
# cd /usr/src/app/db
# mysql -u root -p
> password
```

## setting env

```
$ vi .env.development
```

```
# .env.development
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=password
MYSQL_HOST=db
MYSQL_DATABASE=python_fastapi
PYTHONPATH=/usr/src/app/app
```
