---
layout: publication
title: Cost-based Feature Selection for Network Model Choice
type: article
venue: Journal of Computational and Graphical Statistics
doi: 10.1080/10618600.2022.2151453
author:
  - lraynal
  - me
  - jponnela
---

Selecting a small set of informative features from a large number of possibly noisy candidates is a challenging problem with many applications in machine learning and approximate Bayesian computation. In practice, the cost of computing informative features also needs to be considered. This is particularly important for networks because the computational costs of individual features can span several orders of magnitude. We addressed this issue for the network model selection problem using two approaches. First, we adapted nine feature selection methods to account for the cost of features. We show for two classes of network models that the cost can be reduced by two orders of magnitude without considerably affecting classification accuracy (proportion of correctly identified models). Second, we selected features using pilot simulations with smaller networks. This approach reduced the computational cost by a factor of 50 without affecting classification accuracy. To demonstrate the utility of our approach, we applied it to three different yeast protein interaction networks and identified the best-fitting duplication divergence model. Supplementary materials, including computer code to reproduce our results, are [available online](https://github.com/tillahoffmann/net-summary-selection).
