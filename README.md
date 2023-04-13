Welcome to Reserva! This repository is for a web-based room booking system built with microservices. If you're new to the project, here's a guide to getting started.

# Clone the Repository
To get started, you'll need to clone the repository. You can do this using your preferred Git client or by running the following command in your terminal:

```
git clone https://github.com/ehharvey/Reserva.git
```

# Set up your Environment
We have included a `devcontainer` configuration JSON for VS Code or GitHub Codespaces. This configuration will set up a development environment with all the necessary tools and dependencies.

To use the `devcontainer` configuration, you'll need to have Docker and Visual Studio Code (or GitHub Codespaces) installed. Once you have these tools installed, open the cloned repository in VS Code and follow the prompts to build the container.

# Current Status
We are currently working on implementing our microservices. 

## Backend
Our backend microservices are being built with `FastAPI` and are located under `./microservices`

## Frontend
We are also working on the frontend. The microservice that will deliver the frontend is located at `./microservices/webapp`, with the React code itself located at `./microservices/webapp/vite-react`. We are currently transitioning the frontend away from `Create-React-App` to `Vite`.
