#!/bin/bash
#
# dev-web.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

eval $(docker-machine env penndsgdev)
docker exec -it penndsg_web_1 bash
