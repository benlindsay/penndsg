#!/bin/bash
#
# restore_compose_db.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

# See https://stackoverflow.com/questions/39210274/how-do-i-backup-a-database-in-docker

if [ $# -gt 0 ]; then
  DUMP_FILE=$1
fi

# Drop DB
docker exec penndsg_postgres_1 dropdb -U postgres postgres

# Recreate DB
docker exec penndsg_postgres_1 createdb -U postgres postgres

# Restore backup to DB
docker exec -i -u postgres penndsg_postgres_1 pg_restore -C -d postgres < $DUMP_FILE
