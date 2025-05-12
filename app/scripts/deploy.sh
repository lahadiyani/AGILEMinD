#!/bin/bash

# Pull the latest Docker image
docker-compose pull

# Build and run the container
docker-compose up --build -d

echo "App deployed successfully!"
