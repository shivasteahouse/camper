
# The Camper Project #
[![Build Status](https://travis-ci.org/shivasteahouse/camper.svg)](https://travis-ci.org/shivasteahouse/camper)

## About ##

Describe your project here.

## Prerequisites ##

- Python 2.7, 3.4 recommended
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)

## Installation ##

### Prerequisites ###
This required *docker*, *docker-machine* and *docker-compose* installed on your local machine. More informations on [Docker's website](https://docs.docker.com/installation/mac/)

### Local ###
```
# creates a local host for docker containers, only do once
docker-machine create -d virtualbox local

# create your config secrets
cp secrets.env.sample secrets.env

# load the docker env
eval "$(docker-machine env local)"

# build web image
docker-compose build

docker-compose up -d
```

### Digital Ocean ###
```
# creates the droplet, only do once
docker-machine create --driver digitalocean --digitalocean-size "512mb" --digvitalocean-backups --digitalocean-region "sgp1" --digitalocean-access-token ACC_TOKEN camper

# create your config secrets
cp secrets.env.sample secrets.env

eval "$(docker-machine env camper)"
docker-compose build
docker-compose up -d
```


License
-------
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[BSD]: http://opensource.org/licenses/BSD-3-Clause
