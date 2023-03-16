.PHONY : bash image serve
CMD = docker run --rm --volume=`pwd`:/srv/jekyll -p 4000:4000 -it

serve : Gemfile.lock
	${CMD} tillahoffmann jekyll serve

bash : Gemfile.lock
	${CMD} tillahoffmann bash

Gemfile.lock : Gemfile
	${CMD} jekyll/jekyll bundle update

image :
	docker build -t tillahoffmann .
