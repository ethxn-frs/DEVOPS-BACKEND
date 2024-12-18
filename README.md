# Example backend project for CI-CD

## Requirements

To run this project locally, you will need : 
 - docker
 - python 3.12

## Create a virtual env

Create a virtual environment to install dependencies : 

```shell
python -m venv venv
source venv/bin/activate # For Linux/Mac
.\venv\Scripts\Activate.ps1 # For Windows
```

You should see the virtual env appear in your terminal.

## Install dependencies

There are two requirement files : 
 - requirements/requirements.txt: Contains all the dependencies necessary to run the project in a production environment
 - requirements/dev.txt: Contains additional dev dependencies (Debug, linter, tests etc..)

```shell
pip install -r requirements/requirements.txt # For production builds
pip install -r requirements/dev.txt # For CI environments or local development
```

## Run the database

There is a docker-compose file provided in this project to set up a local postgres database.
Simply run :

```shell
docker compose up -d ./docker-compose.yml
```

The postgres database should be available on port `5432`.

## Run migrations and load data

Once your database is up and running, you can run the migrations to create the tables as well as load testing data.

### Run the migrations 

```shell
python ./manage.py migrate
```

### Load testing data

``` shell
python ./manage.py loaddata --format json ./fixtures/dev-fixtures.json
```

## Run the local development server

```shell
python ./manage.py runserver
```

## Run unit tests

```shell
python manage.py test
```

## Run the linter

```shell
ruff check # Checks if there are any linting issues
ruff check --fix # Fixes potential issues 
```

## Run the code formatter

```shell
ruff format --check # Checks if there are any formatting issues
ruff format # Formats the code
```

## Available environment variables

Configuration for this project is loaded through environment variables. If variables are not present,
this project uses default values to connect to the local development database. When building for production, you can override the following
variables :
 - `DB_HOST`: The hostname for the database
 - `DB_PORT`: The port to connect to the database
 - `DB_NAME`: The name of the database
 - `DB_USER`: The user to connect to the database
 - `DB_PASSWORD`: The user's password
