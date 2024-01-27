---
layout: publication
title: Scalable Gaussian process inference with Stan
type: article
venue: arXiv
doi: 10.48550/arXiv.2301.08836
author:
  - me
  - jponnela
---

![thumbnail](/assets/2023-01-24-gptools-stan/thumbnail.png)
Gaussian processes (GPs) are sophisticated distributions to model functional data. Whilst theoretically appealing, they are computationally cumbersome except for small datasets. We implement two methods for scaling GP inference in Stan: First, a general sparse approximation using a directed acyclic dependency graph. Second, a fast, exact method for regularly spaced data modeled by GPs with stationary kernels using the fast Fourier transform. Based on benchmark experiments, we offer guidance for practitioners to decide between different methods and parameterizations. We consider two real-world examples to illustrate the package. The implementation follows Stan's design and exposes performant inference through a familiar interface. Full posterior inference for more than ten thousand data points is feasible on a laptop in less than 20 seconds.

All code to reproduce the results is available on [GitHub](https://github.com/tillahoffmann/gptools).
