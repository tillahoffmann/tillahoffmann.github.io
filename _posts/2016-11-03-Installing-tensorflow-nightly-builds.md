---
layout: post
published: True
---

[`tensorflow`](https://github.com/tensorflow/tensorflow) is a fast-evolving machine learning library. Often, I want to have access to the latest features but want to avoid the pain of [compiling tensorflow from source](https://www.tensorflow.org/get_started/os_setup.html#installing-from-sources) or waiting for the next release.

Fortunately, the continuous integration service that is used to run tests on tensorflow produces nightly builds. The resulting [python wheels](http://pythonwheels.com/) can be installed easily using [`pip`](https://pypi.python.org/pypi/pip). For example, to install tensorflow on a Mac without a GPU using python3, you can run the following command.

```
pip install http://ci.tensorflow.org/view/Nightly/job/nightly-matrix-cpu/TF_BUILD_IS_OPT=OPT,TF_BUILD_IS_PIP=PIP,TF_BUILD_PYTHON_VERSION=PYTHON3,label=mac-slave/lastSuccessfulBuild/artifact/pip_test/whl/tensorflow-0.11.0rc1-py3-none-any.whl
```

To explore the python wheels for other operating systems or configurations, have a browse through [the nightly builds](http://ci.tensorflow.org/view/Nightly/). Note that the CPU only builds are grouped under the tag `nightly-matrix-cpu` for both Linux and Mac OS X, but the GPU builds can be found under separate tags: `nightly-matrix-mac-gpu` for Mac OS X and `nightly-matrix-linux-gpu` for Linux.