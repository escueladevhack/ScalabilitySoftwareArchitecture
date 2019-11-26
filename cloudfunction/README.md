# Firebase Cloud Function
This repository contains cloud functions source code developed with NodeJS. 

Cloud function is triggered with a HTTP event and when data is inserted into a collection at firestore.

## Usage
Install the dependencies with npm

    npm install

## Deploy at Firebase Cloud Functions
Install the Firebase Tools from npm

	npm i firebase-tools

Log in at Firebase	

	firebase login

Install dependencies

	npm install

Change the default project id at firebaseserc file

	{
	  "projects": {
	    "default": "project-id"
	  }
	}

Deploy functions

	firebase deploy --only functions