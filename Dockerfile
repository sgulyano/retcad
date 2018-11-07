# install nvidia-docker2 from https://github.com/NVIDIA/nvidia-docker

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM pytorch/pytorch:latest
RUN apt-get update && apt-get install libgtk2.0-dev -y --no-install-recommends

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /retcad

# Set the working directory to /music_service
WORKDIR /retcad

# Copy the current directory contents into the container at /music_service
ADD . /retcad/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt