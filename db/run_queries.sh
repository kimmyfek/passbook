#!/bin/bash
docker run -it --link passbook_db:mysql -v $PWD:/tmp --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD" < /tmp/create.sql'
docker run -it --link passbook_db:mysql -v $PWD:/tmp --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD" DenverPassbook < /tmp/business_insert.sql'
docker run -it --link passbook_db:mysql -v $PWD:/tmp --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD" DenverPassbook < /tmp/location_insert.sql'
docker run -it --link passbook_db:mysql -v $PWD:/tmp --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD" DenverPassbook < /tmp/coup_insert.sql'
docker run -it --link passbook_db:mysql -v $PWD:/tmp --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD" DenverPassbook < /tmp/hours_insert.sql'
