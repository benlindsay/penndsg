#!/bin/bash
#
# dev-swarm-init.sh
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

ip=$(docker-machine ip myvm1)
echo "Adding myvm1 as swarm manager:"
echo
output=$(docker-machine ssh myvm1 "docker swarm init --advertise-addr $ip")
sleep 2
echo "$output"
join_cmd=$(echo "$output" | grep "docker swarm join --token")
echo
echo "Adding myvm2 as swarm worker:"
echo
echo "Running the following command:"
echo "docker-machine ssh myvm2 $join_cmd"

docker-machine ssh myvm2 "$join_cmd"
