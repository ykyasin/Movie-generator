#!/bin/bash

# Installing dependencies 
sudo apt-get update
sudo apt-get install -y python3-venv python3-pip

# Exporting test database uri
export TEST_DATABASE_URI=${TEST_DATABASE_URI}

# Activating virtual environment and installing requirements
python3 -m venv venv
source venv/bin/activate
pip3 install -r test_requirements.txt

# Testing by looping through all services
for service in service_1 service_2 service_3 service_4; do 
  cd $service
  python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
  cd ..
done

deactivate