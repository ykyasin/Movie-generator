#!/bin/bash

# Build and push images
docker-compose build
docker-compose push
docker rmi -f $(docker images -q)