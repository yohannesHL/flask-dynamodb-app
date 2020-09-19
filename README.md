
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

* install package on virtual environemnt: 
    ```
    pipenv install
    ```
    on the root folder.
* You'll need to activate the virtual environement before you can run any project specific comands like `python` or `flask` :
 ``` 
 pipenv shell
 ```

## Running
It's best to use the supplied docker compose config.

Run `docker-compose up`

### With docker compose (dev)

 * `docker-compose up --build`

### Locally
```
flask run main:app
```

## Testing
Ensure the environement is activated first.

```
python -m pytest
```
in the project root.

# CI/CD 

We are using github actions to run CI/CD tasks. The task definitions are defined in `.github/workflows/` folder. Definitions consist of a yml configuration outlining build steps. 
Currently there is a task that deploys the docker image to docker hub.

* `docker-image.yml` - Build docker image and Push to Docker Hub


