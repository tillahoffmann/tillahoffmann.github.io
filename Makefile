.PHONY : bash image serve notebook-posts

# Docker targets to serve the website.

CMD = docker run --platform=linux/amd64 --rm --volume=`pwd`:/srv/jekyll -p 4000:4000 -it
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

# Notebooks. We convert from markdown notebooks to ipynb, execute, and convert back to
# markdown for publication.

NOTEBOOKS_MD = $(wildcard _notebooks/*.md)
NOTEBOOKS_IPYNB_RAW = ${NOTEBOOKS_MD:.md=.raw.ipynb}
NOTEBOOKS_IPYNB = ${NOTEBOOKS_MD:.md=.ipynb}
NOTEBOOK_POSTS = $(addprefix _posts/,$(notdir ${NOTEBOOKS_MD}))

notebook-posts : ${NOTEBOOK_POSTS}

${NOTEBOOKS_IPYNB_RAW} : _notebooks/%.raw.ipynb : _notebooks/%.md
	jupytext --output $@ $<

${NOTEBOOKS_IPYNB} : _notebooks/%.ipynb : _notebooks/%.raw.ipynb
	jupyter nbconvert --to ipynb --output $(notdir $@) --execute $<

${NOTEBOOK_POSTS} : _posts/%.md : _notebooks/%.ipynb
	python _notebooks/convert.py $<
