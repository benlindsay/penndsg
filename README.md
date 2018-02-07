# Dockerized Penn Data Science Group Website Source

## Startup

First, install [Docker](https://docs.docker.com/install/) and [Oracle VirtualBox](https://www.virtualbox.org/). Then simply type `./dev-run.sh`, which will do the following:

1. Create a virtual machine called `penndsgdev` if not already created
2. Build the required images if not built
3. Start up the development server
4. Initialize the Postgres database, including allowing you to create a superuser, if not already done
5. Tell you where to navigate to in your browser to see the development website

This will take a long time (~10 minutes) the first time you run it, but will be much quicker every time after that.

## Update Source

After making any updates to any part of this repo, just run `./dev-update.sh` to see those changes reflected locally in the website.

## Stop Server

When you're done with your development session, just run `./dev-stop.sh` to shut down the server.

## Acknowledgments
A lot of inspiration for the dockerization of this website came from [this blog post](https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/)
