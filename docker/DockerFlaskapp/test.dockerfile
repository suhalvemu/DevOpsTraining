FROM ubuntu:24.04

# Install python3 and pip3
RUN apt-get update -y && apt-get install -y python3-pip python3-dev

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory
WORKDIR /app  






