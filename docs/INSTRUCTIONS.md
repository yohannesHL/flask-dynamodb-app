# Instructions

## Prerequisites

- Docker
- Docker Compose
- `.env` file (see environment.template)

## Installation


### With docker compose

To build the image on your local machine :

```
docker-compose build
```

### Locally

It's also possible to run the app without docker (not recomended).


- install [pipenv](https://pypi.org/project/pipenv/) on your machine: `pip install pipenv`.

- `cd` to the root folder where `Pipefile` is located.

- install the package on virtual environemnt:
  ```
  pipenv install
  ```
- You'll need to activate the virtual environement before you can run any project specific comands like `python` or `flask` :

```
pipenv shell
```

## Running

Running the app will start up the flask server on `http://localhost:5000`.
The app requires `.env ` to be present. See `environment.template` for detail on what it should contain.

### With docker compose (dev)

```
docker-compose up --build
```

### Locally

```
FLASK_APP=app/main.py flask run
```

## Testing

- Ensure the environement is activated first: `pipenv shell`.

- `cd` to in the project root.
- 
  ```
  python -m pytest
  ```


## Deployment

### Application deployment
The application is currently deployed to docker hub.

This is automatically handled by the CI pipeline everytime `git push` is run.


### Infrastructure deployment
AWS CDK is used to define and deploy infrastructure as code (IaC).
- First install [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
- Ensure you have your AWS credentials configured as cdk will use those settings: `aws configure`
- Install the aws cdk python dependencies: `pipenv install`
- Generate a Cloud formation template(this will also catch any issues with the definitions):
  ```
  cdk synth
  ```
- Compare current stack against local changes :
  ```
  cdk diff
  ```
- When ready to deploy:
  ```
  cdk deploy
  ```