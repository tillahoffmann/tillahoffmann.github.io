IMAGE = jekyll/jekyll
CMD = docker run --rm --volume=`pwd`:/srv/jekyll -p 4000:4000 -it ${IMAGE}

serve : Gemfile.lock
	${CMD} jekyll serve

Gemfile.lock : Gemfile
	${CMD} bundle update
