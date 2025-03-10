# Docker Stack!

Docker stack files are used to handling the docker image deployment and service creation to the docker engine. The stack file will used to manage the our service configuration and their dependencies. 


# Initial Setup

For to deploy our docker images via stack file, we need to have docker-cli setup in our host machine.
Check the [docker documentation]([https://docs.docker.com/install/linux/docker-ce/debian/](https://docs.docker.com/install/linux/docker-ce/debian/)) for basic knowledge about the docker-cli.

## Docker Swarm 

A swarm is a group of machines that are running Docker and joined into a cluster. After that has happened, you continue to run the Docker commands you’re used to, but now they are executed on a cluster by a **swarm manager**. The machines in a swarm can be physical or virtual. After joining a swarm, they are referred to as **nodes**.

We need to initial swarm in our host machine for our stack deployment.
**docker swarm init**