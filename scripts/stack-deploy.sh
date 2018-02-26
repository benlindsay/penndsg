#!/bin/bash
#
# stack-deploy.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env myvm1)
docker stack deploy -c docker-compose.yml penndsg
