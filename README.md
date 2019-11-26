# Scalability in Software Architecture
This repository has the needed code and files for use and deploy microservices at kubernetes or at serveless services

It contains three folders with the following things:

- k8s: Script with basic commands for :
    - set the zone
    - create cluster
    - get credentials
    - run docker image 
    - expose the deployment
    - get the service
    - delete cluster

- cloud functions
    - cloud function source code developed with NodeJS
    - This cloud function is triggered with a HTTP event and when data is inserted into a collection at firestore.
    - Configuration files for Firebase Cloud Function
    
- service cloud run
    - source code developed with Python
    - DockerFile for deploy at Google Cloud Run