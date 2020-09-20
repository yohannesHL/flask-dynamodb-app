# Outline

This project runs a flask-dynamodb app in docker container.

## Instructions

- [Instructions](docs/INSTRUCTIONS.md)

## Quick start
```
docker-compose up
```

This will build and start the container.
The service will be available on `http://localhost:5000`

### Endpoints
- **/health** 
    ```
    {
        "container": "https://hub.docker.com/r/yohanhl/flask-dynamodb-app",
        "project": "https://github.com/yohannesHL/flask-dynamodb-app",
        "status": "healthy"
    }
    ```
- **/secret**
    Example response:
    ```
    {
        "secret_code": {
            "code_name": "thedoctor"
            "secret_code": "j37ACF8aHLb38JN3"
        }
    }
    ```

## Development process

1. `git pull` the latest changes from remote
1. work on your changes making iterative commits as you go
    * `git add .`
    * `git commit`
1. `git pull --rebase` rebase your branch to get the latest remote changes
1. `git push` push your changes

## CI/CD

We are using github actions to run CI/CD tasks. The task definitions are defined in `.github/workflows/` folder.

- `docker-image.yml` - Build docker image and Push to Docker Hub
