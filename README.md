
# Getting started

This project runs a flask-dynamodb app in docker container.

## Requirements
* Docker
* Docker Compose
* `.env` file (see environment.template)

## Installation

### With docker compose
To build the image on you local machine :
 `docker-compose build`

### Locally
Alternativly it is possible to run the app without docker (not recomended).
You'll need `pipenv` installed on your machine.

Then install package via: `pipenv install` on the root folder.

## Running
Its best to use the supplied docker compose config.

Run `docker-compose up`

### With docker compose (dev)

 * `docker-compose up --build`

### Locally
* `flask run main:app`

## Testing
* `pytest` in the project root.

# CI/CD 

We are using github actions to run CI/CD tasks. The task definitions are defined in `.github/workflows/` folder. Definitions consist of a yml configuration outlining build steps. 
Currently there is a task that deploys the docker image to docker hub.

Currently there is on task which is run on each push to the repo: 
* `docker-image.yml` - Build docker image and Push to Docker Hub


