#!/bin/bash
#
# dev-stop.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env penndsgdev)
docker-compose down --volumes
docker-machine stop penndsgdev
