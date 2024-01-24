---
layout: publication
title: Network Layout Algorithm With Covariate Smoothing
type: article
venue: arXiv
doi: 10.48550/arXiv.2401.04771
author:
- osmiley
- me
- jponnela
---

Network science explores intricate connections among objects, employed in diverse domains like social interactions, fraud detection, and disease spread. Visualization of networks facilitates conceptualizing research questions and forming scientific hypotheses. Networks, as mathematical high-dimensional objects, require dimensionality reduction for (planar) visualization. Visualizing empirical networks present additional challenges. They often contain false positive (spurious) and false negative (missing) edges. Traditional visualization methods don't account for errors in observation, potentially biasing interpretations. Moreover, contemporary network data includes rich nodal attributes. However, traditional methods neglect these attributes when computing node locations. Our visualization approach aims to leverage nodal attribute richness to compensate for network data limitations. We employ a statistical model estimating the probability of edge connections between nodes based on their covariates. We enhance the Fruchterman-Reingold algorithm to incorporate estimated dyad connection probabilities, allowing practitioners to balance reliance on observed versus estimated edges. We explore optimal smoothing levels, offering a natural way to include relevant nodal information in layouts. Results demonstrate the effectiveness of our method in achieving robust network visualization, providing insights for improved analysis.
