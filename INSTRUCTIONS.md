Assignment

Objective

The purpose of this assignment is to evaluate your ability to:

Write an Ansible automation script
Develop a basic web service application and containerise it

Automation

Write an Ansible playbook that installs a database of your choice (postgres, MySQL, MariaDB, etc) on a target VM/localhost with the following configuration:
Accepts connection from all IP addresses
Newly created user “db-user01“
 
Development

Using your programming language of choice, write a web service application that serves 1 REST endpoint
Calling the REST endpoint via GET request will return a JSON body containing a “hello world” message

Containerisation

Write a Dockerfile to containerise the developed web service application

Expectation

The Ansible script will install the database of choice and the user can use the newly created “db-user01” to connect with the database
The Dockerfile will build a Docker image with the application within it
Running the built Docker image will start a Docker container which serves the web service REST endpoint on port 5656
Accessing http://localhost:5656/<endpoint-name> on the laptop browser will return the JSON response containing “hello world“
 

Deliverables

Share the Ansible script, application project (code, Dockerfile, etc) via GitHub repository or zipped file
Give a brief write up (can be email or doc) to describe the steps taken to complete the assignment
 

Additional Note

Efforts taken to expand the assignment scope will be taken into account
