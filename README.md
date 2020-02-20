---
<!---
This is MD file so it needs the front matter or the build will fail
-->
---

# Local development

The site needs to be built and served by a web browser. To do both of those things at the same time
use the following command, in the root of your project:

```bash
bundle exec jekyll serve
```

This command will also watch for changes in the site and rebuild it automatically.
However, this does not apply to your `_config.yml` file. If you make any changes to this file you will
have to stop the server (with `CTRL-C`) and start it again.

If you prefer not to use the server provided by Jekyll you need to first build the site
with

```bash
bundle exec jekyll build
```

And then use a web server to serve the site, like for example the PHP built-in one

```bash
php -S localhost:8080 -t _site
```

P.S. For some reason using the PHP built-in server does not work well when rebulding the
site because of some style changes. I would recommend using Jekyll to serve the site.

## Docker

If you prefer you could use docker to create a container which will build and serve your project.

```bash
docker run --rm \
--volume="$PWD:/srv/jekyll" \
-p 4000:4000 \
-it jekyll/jekyll:4.0 \
jekyll serve
```

Your site will then be available at [http://0.0.0.0:4000](http://0.0.0.0:4000).
Note that changes to `_config.yml` will not be picked up and the site will not be automatically
rebuilt. You will have to stop the container and start it again.

You can also use the docker compose file provided to create two containers: one for Jekyll and 
one for Ngrok. Why? Because this will allow your local Jekyll site to be visible from outside.
This is particularly useful when updating the CV and you want to create the PDF before merging
the changes into the master branch.

So, run the following command:

```bash
docker-compose up
```

As I said this will create two containers. To find out the external URL you can use fro your
local Jekyll site you have two options:

- you can run the command `curl $(docker port ngrok 4040)/api/tunnels` and look for the
`public_url` key

or

- you can go to http://localhost:4040/

## Resumé to PDF

No need to use any online service. I have written a CSS for printing, so you just need to print the
page and save is as PDF, and Bob's your uncle.
