FROM python:3.8


ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN pip install pipenv 

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN PIPENV_VENV_IN_PROJECT=true pipenv install --deploy --system

COPY app /app/

EXPOSE 5000

WORKDIR /

ENTRYPOINT gunicorn -b :5000 app.main:app
