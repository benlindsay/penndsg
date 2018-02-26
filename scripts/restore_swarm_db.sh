#!/bin/bash
#
# restore_swarm_db.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

# See https://stackoverflow.com/questions/39210274/how-do-i-backup-a-database-in-docker

STACK_NAME=penndsg
SWARM_MANAGER=myvm1
echo "Connecting to machine $SWARM_MANAGER"
eval $(docker-machine env $SWARM_MANAGER)
POSTGRES_MACHINE=$(docker service ps "$STACK_NAME"_postgres | tail -1 | awk '{print $4}')
echo "Connecting to machine $POSTGRES_MACHINE"
eval $(docker-machine env $POSTGRES_MACHINE)
POSTGRES_ID=$(docker ps | grep postgres | awk '{print $1}')
echo "postgres container id is $POSTGRES_ID"

# Drop DB
docker exec $POSTGRES_ID dropdb -U postgres postgres

# Recreate DB
docker exec $POSTGRES_ID createdb -U postgres postgres

# Restore backup to DB
docker exec -i -u postgres $POSTGRES_ID pg_restore -C -d postgres < db.dump
