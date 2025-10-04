FROM mysql:8.4

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=appdb
ENV MYSQL_USER=appuser
ENV MYSQL_PASSWORD=apppass

COPY init.sql /docker-entrypoint-initdb.d/
