.PHONY : bash image serve notebook-posts

# Docker targets to serve the website.

CMD = docker run --rm --volume=`pwd`:/srv/jekyll -p 4000:4000 -it

serve : Gemfile.lock
	${CMD} tillahoffmann jekyll serve

bash : Gemfile.lock
	${CMD} tillahoffmann bash

Gemfile.lock : Gemfile
	${CMD} jekyll/jekyll bundle update

image :
	docker build -t tillahoffmann .

# Python dependencies and targets for preparing content.

requirements.txt : requirements.in
	pip-compile --resolver=backtracking -v

NOTEBOOKS = $(wildcard _notebooks/*.ipynb)
NOTEBOOK_POSTS = $(addprefix _posts/,$(notdir ${NOTEBOOKS:.ipynb=.md}))

notebook-posts : ${NOTEBOOK_POSTS}

${NOTEBOOK_POSTS} : _posts/%.md : _notebooks/%.ipynb
	python _notebooks/convert.py $<
