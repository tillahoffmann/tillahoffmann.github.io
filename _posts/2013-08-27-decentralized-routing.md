---
layout: publication
title: Decentralized Routing On Spatial Networks With Stochastic Edge Weights
thumbnail: /assets/2013-08-27-decentralized-routing.png
type: article
venue: Physical Review E
volume: 8
issue: 2
pages: 022815
doi: 10.1103/PhysRevE.88.022815
author:
  - me
  - rlambiotte
  - mporter
---

We investigate algorithms to find short paths in spatial networks with stochastic edge weights. Our formulation of the problem of finding short paths differs from traditional formulations because we specifically do not make two of the usual simplifying assumptions: (1) we allow edge weights to be stochastic rather than deterministic and (2) we do not assume that global knowledge of a network is available. We develop a decentralized routing algorithm that provides en route guidance for travelers on a spatial network with stochastic edge weights without the need to rely on global knowledge about the network. To guide a traveler, our algorithm uses an estimation function that evaluates cumulative arrival probability distributions based on distances between pairs of nodes. The estimation function carries a notion of proximity between nodes and thereby enables routing without global knowledge. In testing our decentralized algorithm, we define a criterion that makes it possible to discriminate among arrival probability distributions, and we test our algorithm and this criterion using both synthetic and real networks.
