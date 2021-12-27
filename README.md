# [KBSS Website](https://kbss.felk.cvut.cz/)

This repository contains the website of the Knowledge-based and Software Systems group of the Faculty of Electrical Engineering,
Czech Technical University in Prague.

It is based on the [Minimal Mistakes Jekyll theme](https://mmistakes.github.io/minimal-mistakes/).

## Deploy

There are two ways of deploying the website.

### Docker

There is a Dockerfile to simplify deployment. So the steps to get the website working are:

1. Build the Docker image (using the name `kbss-website`)

`docker build -t kbss-website`

2. Run the container. The following command also allows dynamic reloading of the website when the content is changed.

`docker run --volume="$PWD:/srv/jekyll" -p 4000:4000 -t kbss-website`

3. The website is now available at `http://localhost:4000`

### Without Docker

Assuming Jekyll is installed on the system, the following commands can be used to run the site.

1. Install the dependencies

`bundle install`

2. Run Jekyll with the website

`jekyll serve`

3. The website is now available at `http://localhost:4000`

