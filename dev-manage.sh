#!/bin/bash
#
# dev-manage.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env penndsgdev)
docker-compose run --service-ports -v $(pwd)/web:/usr/src/app web ./manage.py $@
