#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3-venv python3-pip
export TEST_DATABASE_URI=${TEST_DATABASE_URI}

# Test service 1
echo "----------------------------Testing Service 1----------------------------"
cd service_1
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
echo "----------------------------Finished Testing Service 1----------------------------"

# Test service 2
echo "----------------------------Testing Service 2----------------------------"
cd service_2
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
echo "----------------------------Finished Testing Service 2----------------------------"
