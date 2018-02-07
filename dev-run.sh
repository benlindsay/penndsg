#!/bin/bash
#
# dev-run.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

# Create docker virtual machine 'penndsgdev' if not already created
if [ $(docker-machine ls -q | grep '^penndsgdev$') ]; then
  echo "'penndsgdev' already exists."
  echo "Skipping 'docker-machine create' and 'django-init.sh' commands."
  docker-machine start penndsgdev
  eval $(docker-machine env penndsgdev)
  docker-compose build
  docker-compose up -d
else
  if [ $(uname -s) == 'Darwin' ]; then
    # virtualbox driver for Macs
    docker-machine create --driver virtualbox penndsgdev
  else
    # hyperv driver for windows
    docker-machine create --driver hyperv penndsgdev
  fi
  eval $(docker-machine env penndsgdev)
  docker-compose build
  docker-compose up -d
  docker exec -it penndsg_web_1 bash django-init.sh
fi

echo "Navigate to $(docker-machine ip penndsgdev) in your browser."
