#!/bin/bash
#
# swarm-down.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

docker service rm registry
eval $(docker-machine env myvm1)
docker stack rm penndsg
eval $(docker-machine env myvm2)
docker swarm leave
eval $(docker-machine env myvm1)
docker swarm leave --force
