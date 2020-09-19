# Outline

This project runs a flask-dynamodb app in docker container.

## Instructions

- [Instructions](docs/INSTRUCTIONS.md)

## Development process

1. `git pull` the latest changes from remote
1. work on your changes making iterative commits as you go
1. `git pull --rebase` rebase your branch to get the latest remote changes
1. `git push` push your changes

## CI/CD

We are using github actions to run CI/CD tasks. The task definitions are defined in `.github/workflows/` folder.

- `docker-image.yml` - Build docker image and Push to Docker Hub
