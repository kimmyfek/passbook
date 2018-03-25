#!/bin/bash
#mysql -h localhost -u root -ppassword -e "show databases"
docker run -it --link passbook_db:mysql -v insert.sql:/tmp --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD" DenverPassbook < /tmp/insert.sql'
