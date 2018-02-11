#!/bin/bash
#
# dev-populate-events.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env penndsgdev)
docker exec -it penndsg_web_1 ./manage.py populate_events
exit 0
