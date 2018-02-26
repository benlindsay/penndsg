#!/bin/bash
#
# dev-collectstatic.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

# Run this if the css style sheets weren't collected properly and the admin
# pages look like crap

eval $(docker-machine env penndsgdev)
docker exec -it penndsg_web_1 python manage.py collectstatic
