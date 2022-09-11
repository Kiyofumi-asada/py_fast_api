FROM mariadb:10.9

RUN apt update \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

RUN touch /var/log/mysql/mysqld.log