# movie-generator
## Introduction 
### Objective
This is an individual project in order to meet the SFIA requirements. The objective of this project is to create a web application based on the microservice architecture. Which allows us to split up the application into more manageble bits as opposed to one monolithic application.

The services are to create an “object” which will either be used or displayed by the other services. Service 1 will be the core service, i.e. the front-end that the user will see. Here will contain the relevant html files. Also, this service will communicate with the other services. Service 2 and 3 will each generate a random object that will be sent to service 1. Service 4 will generate an object based on the response from service 2 and 3. 

The constraints are as follows: 
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

### My Project Proposal 
The idea I went with is a website that produces a movie based on a location and weather. The user will first connect to service 1 which will display the webpage, but before displaying the page, a GET request is made to service 2 and service 3. Service 2 will return a random location, and service 3 a random weather. Then a POST request is made to service 4 sending the location and weather information obtained from the previous GET requests. Service 4 will then choose a film based on that information.

## Software Architecture 
### Project tracking
For project tracking, I decided to use Trello board. Trello board is a nice lightweight tool to help organise what tasks need to be done. I have set it up such that there is several lists each containing cards related to that list. Each card may contain colour coded labels which represent what that particular card is related to. I have also decided to use the MoSCow approach, which are also shown on the cards as labels. The lists I've made are as follows:
* Project Resources - Containing relevant links
* User Stories - Each card has the format "As a [User]..., I want... [Feature], so that... [Details]"
* Backlog - Tasks needed to be done
* In-Progress - Tasks currently being worked on
* Testing - Features that need to be tested
* Complete - All completed tasks
* Issues - Any issues that came up


### Risk assessment

### Entity Relationship Diagram
For the sake of this project, only one ERD is needed. The image below shows the "Movie" ERD which contains the id, name, location and weather. This table will help us create data that persists in the database after each refresh.

## Software Infrastructure
### Jenkins 
Jenkins is an open source automation server that automates many parts of the project, including testing and deployment. This helps facilitate continous integration and deployment. For this project, the stages of the Jenkins pipeline is as follows: 
* Testing - Which produces coverage reports on the console
* Build and push images - Docker-compose is used to build the images and push them to Docker-Hub
* Ansible configuration - Allows us to configure several servers at once, including
* * Installing necessary dependencies
* * Initializing the swarm and connecting to worker nodes
* * Configuring the NGINX server for load-balancing
* Deploy stack - Configures the web-applcation on the manager and worker nodes

Details on the stages used in the Jenkins pipeline can be found in the jenkinsfile. 

### Swarm configuration

### The services 

## Testing
For this project, I have decided to implement unit testing in the application. Unit testing allows us to test whether each functions returns an expected response. The images below show information on how many tests have passed and how many lines have been covered, these have posted on coverage reports for easy viewing.

The command used to produce the report is:
```py
python3 -m pytest --cov --cov-config=code/.coveragerc --cov-report term-missing --cov-report xml --junitxml junit.xml
 ```
A junit.xml is also produced which allows us to make use of a Jenkins plugin called Junit. This gives us a graphical view of the test results, making it easier to debug if any errors arise. 