#!/bin/bash
#
# dev-psql.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env penndsgdev)
docker cp reset_to_1.sql penndsg_postgres_1:/reset_to_1.sql
docker exec -it penndsg_postgres_1 psql -U postgres -e postgres -f /reset_to_1.sql
