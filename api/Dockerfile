# syntax=docker/dockerfile:1

FROM --platform=linux/amd64 python:3.10

WORKDIR /app/api

# Install app's dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Add app code
COPY . ./

# Move entry script to directory in container's path
COPY entrypoint.sh /usr/local/bin

# Install Linux package(s) for Chromedriver
RUN apt update
RUN apt-get --assume-yes install libnss3
RUN apt-get install chromium -y
RUN apt install chromium-driver

# Add an entrypoint. This set of executable params are appended to the 
# CLI run params (set either in the CLI call itself, or by the "CMD" 
# directive in the Dockerfile
ENTRYPOINT ["entrypoint.sh"]
