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
  * To deactivate the environment use 'exit` command.

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
- ```
  python -m pytest
  ```

## Deployment

### Application deployment


Everytime `git push` is run a new image is deployed to docker hub.
This is automatically handled by the CI pipeline.

### Infrastructure deployment

AWS CDK is used to define and deploy infrastructure as code (IaC). The output is included in `infra/cloudformation.yml`.


The steps below outline an example deployment scenario:

- First install [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
- Ensure you have your AWS credentials configured as cdk will use those settings: `aws configure`
- Install the aws cdk python dependencies and activate infra environment:
  ```
  $ cd infra
  $ PIPENV_NO_INHERIT=1 pipenv install
  $ PIPENV_NO_INHERIT=1 pipenv shell
  ```
- Generate a Cloud formation template:
  ```
  $ cdk synth > cloudformation.yml
  ```
- Compare local changes against deployed stack (optional):
  ```
  $ cdk diff
  ```
- When ready to deploy:
  ```
  $ cdk deploy
  ```
  * This will deploy the stack to AWS
  * `vpcid` will be output to the console use this to inspect the deployed vpc on AWS console 
  * `cdk.out` will be created/updated - keep this tracked
- Go to AWS console and manually change the outbound rules for the created internet gateway.


