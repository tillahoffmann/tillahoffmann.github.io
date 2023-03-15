.PHONY : image serve
CMD = docker run --rm --volume=`pwd`:/srv/jekyll -p 4000:4000 -it

serve : Gemfile.lock
	${CMD} tillahoffmann jekyll serve

Gemfile.lock : Gemfile
	${CMD} jekyll/jekyll bundle update

image :
	docker build -t tillahoffmann .
