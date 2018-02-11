#!/bin/bash
#
# dev-start.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

# Create docker virtual machine 'penndsgdev' if not already created
if [ $(docker-machine ls -q | grep '^penndsgdev$') ]; then
  echo "Starting 'penndsgdev' machine:"
  docker-machine start penndsgdev
else
  echo "Creating and starting 'penndsgdev' machine:"
  if [ $(uname -s) == 'Darwin' ]; then
    # virtualbox driver for Macs
    docker-machine create --driver virtualbox penndsgdev
  else
    # hyperv driver for windows
    docker-machine create --driver hyperv penndsgdev
  fi
fi
