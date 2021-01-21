#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@swarm-master:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@swarm-master << EOF
    export SECRET_KEY=${SECRET_KEY}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml movie-gen
EOF