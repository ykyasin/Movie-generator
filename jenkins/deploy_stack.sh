#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@swarm-manager << EOF
    export DATABASE_URI=${DATABASE_URI} SECRET_KEY=${SECRET_KEY} API_LOCATION=${API_LOCATION} API_WEATHER=${API_WEATHER}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml movie-gen
EOF