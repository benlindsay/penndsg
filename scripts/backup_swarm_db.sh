#!/bin/bash
#
# backup_swarm_db.sh
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

DATE=$(date '+%Y-%m-%d_%H%M%S')
mkdir -p db-backups
BACKUP_NAME=db-backups/$DATE.dump
echo "Backing up to $BACKUP_NAME"

# Backup
docker exec -u postgres $POSTGRES_ID pg_dump -Fc postgres > $BACKUP_NAME
