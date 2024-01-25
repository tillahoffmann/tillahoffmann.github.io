.PHONY : bash image serve notebook-posts

# Docker targets to serve the website.

CMD = docker run  --platform=linux/amd64 --rm --volume=`pwd`:/srv/jekyll -p 4000:4000 -it
IMAGE = tillahoffmann

serve : Gemfile.lock
	${CMD} ${IMAGE} jekyll serve

bash : Gemfile.lock
	${CMD} ${IMAGE} bash

Gemfile.lock : Gemfile
	${CMD} jekyll/jekyll bundle update

image : Gemfile.lock
	docker build --platform=linux/amd64 -t ${IMAGE} .

# Python dependencies and targets for preparing content.

requirements.txt : requirements.in
	pip-compile --resolver=backtracking -v

NOTEBOOKS = $(wildcard _notebooks/*.ipynb)
NOTEBOOK_POSTS = $(addprefix _posts/,$(notdir ${NOTEBOOKS:.ipynb=.md}))

notebook-posts : ${NOTEBOOK_POSTS}

${NOTEBOOK_POSTS} : _posts/%.md : _notebooks/%.ipynb
	python _notebooks/convert.py $<
