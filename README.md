Welcome to Reserva! This repository is for a web-based room booking system built with microservices. If you're new to the project, here's a guide to getting started.

# Clone the Repository
To get started, you'll need to clone the repository. You can do this using your preferred Git client or by running the following command in your terminal:

```
git clone https://github.com/ehharvey/Reserva.git
```

# Set up your Environment
We have included a `devcontainer` configuration JSON for VS Code or GitHub Codespaces. This configuration will set up a development environment with all the necessary tools and dependencies.

To use the `devcontainer` configuration, you'll need to have Docker and Visual Studio Code (or GitHub Codespaces) installed. Once you have these tools installed, open the cloned repository in VS Code. You can find information about using Devcontainers [here](https://code.visualstudio.com/docs/devcontainers/containers#_quick-start-open-a-git-repository-or-github-pr-in-an-isolated-container-volume). Basically, when you open this code, press control + shift + p and type in "Dev" and look for an option to open the folder inside a Devcontainer.

# Running the project
## Frontend
To run the Frontend, you first want to ensure that a .env file exists inside `microservices/webapp/vite-react` that containing the required key-value pairs. If this file does not exist, or if the frontend isn't working, please contact Emil Harvey for assistance.

Afterwards, open a terminal (in VS Code) to `microservices/webapp/vite-react` and run `yarn` followed by `yarn dev`. The first command will install dependencies and the second command will run the frontend. VS Code (with Dev Containers) should automatically port forward port 3000 from the development container to your host OS, meaning that you can open a browser to localhost:3000 to access the frontend. If the VS Code does not automatically port forward, open terminal and then view the ports tab to add port 3000.

## Backend
Similarly, to run the Backend, you want to ensure that an appropriate .env file exists inside `microservices/backend`. If this file does not exist, or if the backend isn't working, please contact Emil Harvey for assistance.

Afterwards open a terminal to `microservices/backend`, set up a Python venv and install the requirements listed there. Then, from this directory, you can run `python -m openapi_server` to launch the backend. The backend runs on port 8080, which should automatically port forward from the dev container to your host OS.

## MongoDB
To run MongoDB, make sure that Docker is available from the devcontainer. You can do so by opening a terminal and running `docker ps`.

Afterwards, navigate to `microservices` and run `docker-compose up`.
