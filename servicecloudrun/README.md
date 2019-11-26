# Backend Service Hello World
This repository is a simple API that returns "Hello World"

## Usage
Install the dependencies with pipenv

    pip install pipenv 
    pipenv install

run the API

    pipenv run python src/api.py

This will make the service available at [http://localhost:8080/apis/gethello/1.0.0](http://localhost:8080/apis/gethello/1.0.0) using the http GET method

## Deploy at Google Cloud Run
Activate the Google Cloud Shell, clone the repository and execute the following commands:

	gcloud builds submit --tag gcr.io/{PROJECT_ID}/helloworldpython
	
	gcloud beta run deploy helloworldpython --image gcr.io/{PROJECT_ID}/helloworldpython --platform managed --region=us-central1
