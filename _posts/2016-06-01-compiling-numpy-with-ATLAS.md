---
layout: post
published: True
---

[Numpy](http://www.numpy.org/) is a great python package for scientific computing. Although it comes with many [performant functions](https://docs.scipy.org/doc/numpy-dev/reference/ufuncs.html) and the ability to [vectorise](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.vectorize.html#numpy.vectorize) your own functions, it is sometimes necessary to distribute your code across multiple cores.

Unfortunately, python dies ungracefully with a segmentation fault when you are trying to use numpy in combination with the [multiprocessing](https://docs.python.org/2/library/multiprocessing.html) package. The problem is caused by [Apple's Accelerate Framework](https://developer.apple.com/library/tvos/documentation/Accelerate/Reference/AccelerateFWRef/index.html) which [does not support forking](https://mail.scipy.org/pipermail/numpy-discussion/2012-August/063589.html). Some [workarounds](http://stackoverflow.com/questions/19705200/multiprocessing-with-numpy-makes-python-quit-unexpectedly-on-osx) have been found, but they are not satisfactory.

The best solution I have come across is linking numpy to the open source library [ATLAS](http://math-atlas.sourceforge.net/) rather than the Accelerate Framework provided by Apple. The rest of the post will discuss how to install ATLAS with LAPACK and link numpy.

## Installing ATLAS with LAPACK

Grab the latest versions of [ATLAS](http://math-atlas.sourceforge.net/) and [LAPACK](http://www.netlib.org/lapack/) from their respective websites, fire up a terminal, and `cd` to your download directory, which should contain `atlas3.10.2.tar.bz2` and `lapack-3.6.0.tgz`. Extract the ATLAS repository and change into the `ATLAS` directory.

```bash
tar -xvzf atlas3.10.2.tar.bz2`
cd ATLAS
```

ATLAS requires a dedicated directory to be able to configure the build.

```bash
mkdir _build
cd build
../configure -b 64 --shared --with-netlib-lapack-tarfile=../../lapack-3.6.0.tgz
```

The flags indicate that you are building on a [64 bit system](http://math-atlas.sourceforge.net/atlas_install/node35.html), would like to build [shared libraries](http://math-atlas.sourceforge.net/atlas_install/node22.html), and [where to find the LAPACK sources](http://math-atlas.sourceforge.net/atlas_install/node8.html). 

You can build and install ATLAS by running 

```bash
make
sudo make install
```

which will take a few minutes and install the library in `/usr/local/atlas/` (unless you set a [prefix](http://www.gnu.org/software/libc/manual/html_node/Configuring-and-compiling.html)).

## Linking numpy

Get the numpy source by downloading or cloning the [repository](https://github.com/numpy/numpy). After `cd`ing into the repository, make a copy of the `site.cfg` which defines the build options for numpy.

```bash
cp site.cfg.example site.cfg
```

Open the file and remove the comment characters from the `[atlas]` section such that the file looks like

```
[atlas]
library_dirs = /usr/local/atlas/lib
include_dirs = /usr/local/atlas/include
```

Finally, let's install numpy by running

```bash
pip install .
```

You can check whether everything worked out ok by starting a python shell and running

```python
import numpy as np
np.__config__.show()
```

which should look something like

```
atlas_3_10_blas_threads_info:
    libraries = ['tatlas', 'tatlas']
    library_dirs = ['/usr/local/atlas/lib']
    define_macros = [('HAVE_CBLAS', None), ('NO_ATLAS_INFO', -1)]
    language = c
    include_dirs = ['/usr/local/atlas/include']
lapack_opt_info:
    libraries = ['tatlas', 'tatlas', 'tatlas', 'tatlas']
    library_dirs = ['/usr/local/atlas/lib']
    define_macros = [('NO_ATLAS_INFO', -1)]
    language = f77
    include_dirs = ['/usr/local/atlas/include']
blas_opt_info:
    libraries = ['tatlas', 'tatlas']
    library_dirs = ['/usr/local/atlas/lib']
    define_macros = [('HAVE_CBLAS', None), ('NO_ATLAS_INFO', -1)]
    language = c
    include_dirs = ['/usr/local/atlas/include']
openblas_info:
  NOT AVAILABLE
blis_info:
  NOT AVAILABLE
openblas_lapack_info:
  NOT AVAILABLE
atlas_3_10_threads_info:
    libraries = ['tatlas', 'tatlas', 'tatlas', 'tatlas']
    library_dirs = ['/usr/local/atlas/lib']
    define_macros = [('NO_ATLAS_INFO', -1)]
    language = f77
    include_dirs = ['/usr/local/atlas/include']
lapack_mkl_info:
  NOT AVAILABLE
blas_mkl_info:
  NOT AVAILABLE
mkl_info:
  NOT AVAILABLE
```