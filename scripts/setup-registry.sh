#!/bin/bash
#
# setup-registry.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

# see https://docs.docker.com/engine/swarm/stack-deploy/

docker service create --name registry --publish published=5000,target=5000 registry:2
