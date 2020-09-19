# Instructions

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


