# healthjoy-forker

Simple web application written in Python that utilizes Github OAuth authentication to fork this repo as part of your personal repository.

## Pre-requisites

The simplest and preferred method to run this solution locally is with [Docker](https://www.docker.com/products/docker-desktop), which would require your local environment to have Docker installed. This method abstracts away the a lot of the variables between each local setup (i.e., OS, dependency versions). Proceed to Docker Setup section below after successful installation of Docker on your local machine.

Alternatively, if you prefer not to install Docker, we can perform the project build manually with the instructions in the below section Manual Setup.

## Docker Setup

1. Replace the values of `replace_me_with_id` and `replace_me_with_secret` inside the `docker-compose.yml` file with client ID and secret, respectively, of the Github OAuth application. (Reach out to project owner for those values.)

1. From the root directory of the project run the following command:

```bash
docker-compose up
```

1. Open browser to `http://localhost:5000` to access the application.

## Manual Setup

1. Set the necessary environment variables for local development. Reach out to project owner for values of `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET`.

```bash
export FLASK_APP=forker
export SECRET_KEY=development
export GITHUB_CLIENT_ID=value_from_owner
export GITHUB_CLIENT_SECRET=value_from_owner
```

1. Compile the web component to static files for the web app with the following command in root project directory:

```bash
npm run --prefix=web build && cp web/build forker/static
```

1. Run following command to install the local forker package:

```bash
pip install .
```

1. Start the Flask server:

```bash
flask run
```

1. Open browser to `http://localhost:5000` to access the application.
