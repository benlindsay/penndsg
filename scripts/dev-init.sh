#!/bin/bash
#
# dev-init.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env penndsgdev)
docker-compose build
docker-compose run --service-ports -v $(pwd)/web:/usr/src/app web bash django-init.sh
