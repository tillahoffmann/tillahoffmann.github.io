# Personal website of Till Hoffmann [![pages-build-deployment](https://github.com/tillahoffmann/tillahoffmann.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/tillahoffmann/tillahoffmann.github.io/actions/workflows/pages/pages-build-deployment)

Run a local development server in two steps:

1. Run `make image` to build a docker image containing all dependencies.
2. Run `make serve` to serve the website on port 4000.

Requirements can be updated by running `make Gemfile.lock` and `make bash` will open an interactive terminal in the container.
