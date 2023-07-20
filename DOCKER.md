# Docker Usage Guide

This guide provides instructions on how to build and run Docker containers for production and testing.

- Dockerfile: Used for production
- Dockerfile.test: Used for testing

Make sure you have Docker installed on your machine.

## Setting Up Environment Variables

The application expects certain environment variables to be set. These variables are loaded from .env files.

- .env.prod for production
- .env.dev for development and testing

For more information about environmental variables, look at [this guide](ENV_VARS.md).


## Building Docker Images

To build Docker images for each environment, you can use the `docker build` command.

### Production

```bash
docker build -t lms .
```

### Testing

```bash
docker build -f Dockerfile.test -t lms-test .
```

## Running Docker Containers

To run Docker containers for each environment, you can use the `docker run` command. The `--env-file` option is used to load the environment variables from the .env files. 

### Production

```bash
docker run -d --env-file .env.prod lms
```

### Testing

```bash
docker run --env-file .env.test lms-test
```

## Running Docker Containers in Interactive Mode

If you want to run your Docker container in interactive mode, which allows you to interact with the running container, you can add the `-it` option to the `docker run` command:

```bash
docker run -it --env-file .env.prod lms
```

Or if you want to be able to move inside a shell:
```bash
docker run -it --env-file .env.prod lms /bin/bash
```
