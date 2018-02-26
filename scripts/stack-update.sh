#!/bin/bash
#
# stack-update.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env myvm1)
docker-compose build && docker-compose push
docker stack deploy -c docker-compose.yml penndsg
