from os import getenv

# These will be injected at ci deploy stage
CONTAINER_URL = getenv('CONTAINER_URL')
PROJECT_URL = getenv('PROJECT_URL')