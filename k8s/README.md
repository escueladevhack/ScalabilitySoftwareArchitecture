# k8s commands
This folder contains the script with basic commands for :

    - set the zone
    - create cluster
    - get credentials
    - run docker image 
    - expose the deployment
    - get the service
    - delete cluster

### COMMANDS

- gcloud config set compute/zone us-central1-a
- gcloud container clusters create io
- gcloud container clusters get-credentials [CLUSTER-NAME]
- kubectl run hello-server --image=gcr.io/google-samples/hello-app:1.0 --port 8080
- kubectl expose deployment hello-server --type="LoadBalancer"
- kubectl get service hello-server
- load the next link http://34.67.148.185:8080 at the browser
- gcloud container clusters delete io