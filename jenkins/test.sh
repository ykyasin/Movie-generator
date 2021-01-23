#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3-venv python3-pip
export TEST_DATABASE_URI=${TEST_DATABASE_URI}

# Test service 1
echo "--------------------------------------------------------Testing Service 1-------------------------------------------------------"
cd service_1
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
echo "--------------------------------------------------------Finished Testing Service 1--------------------------------------------------------"

# Test service 2
echo "--------------------------------------------------------Testing Service 2--------------------------------------------------------"
cd service_2
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
echo "--------------------------------------------------------Finished Testing Service 2--------------------------------------------------------"

# Test service 3
echo "--------------------------------------------------------Testing Service 3--------------------------------------------------------"
cd service_3
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
echo "--------------------------------------------------------Finished Testing Service 3--------------------------------------------------------"

# Test service 4
echo "--------------------------------------------------------Testing Service 4--------------------------------------------------------"
cd service_4
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
echo "--------------------------------------------------------Finished Testing Service 4--------------------------------------------------------"
