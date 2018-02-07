#!/bin/bash
#
# dev-update.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env penndsgdev)
docker-compose down --volumes
docker-compose build
docker-compose up --force-recreate -d

echo "Navigate to $(docker-machine ip penndsgdev) in your browser."
