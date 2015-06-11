---
layout: post
published: true
---

Writing documentation for a project with consistent formatting is tedious and not particularly stimulating. I wrote an IPython `magic` to generate `docstring` stubs in line with [this `numpy` example](https://github.com/numpy/numpy/blob/master/doc/example.py). You can find a working notebook on [nbviewer](http://nbviewer.ipython.org/gist/tillahoffmann/1c0b07889d07c8904cd5).

To use the `magic`, simply drop the following file into your profile startup folder. On Linux or Mac OSX, the default startup directory is `~/.ipython/profile_default/startup/`, where `~` denotes your user directory.

{ % gist 3da7abb296ca00c98d5a % }
