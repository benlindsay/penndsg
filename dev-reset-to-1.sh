#!/bin/bash
#
# dev-reset-to-1.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env penndsgdev)
# docker cp reset-to-1.sql penndsg_postgres_1:/reset-to-1.sql
docker exec -it penndsg_postgres_1 psql -U postgres -e postgres -c "ALTER SEQUENCE events_event_id_seq RESTART WITH 1;"
