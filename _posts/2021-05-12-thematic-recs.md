---
layout: publication
title: Thematic recommendations on knowledge graphs using multilayer networks
type: article
venue: arXiv
doi: 10.48550/arXiv.2105.05733
pages: 2105.05733
author:
- mbeguerisse
- dkorkinof
- me
---

We present a framework to generate and evaluate thematic recommendations based on multilayer network representations of knowledge graphs (KGs). In this representation, each layer encodes a different type of relationship in the KG, and directed interlayer couplings connect the same entity in different roles. The relative importance of different types of connections is captured by an intuitive salience matrix that can be estimated from data, tuned to incorporate domain knowledge, address different use cases, or respect business logic.

We apply an adaptation of the personalised PageRank algorithm to multilayer models of KGs to generate item-item recommendations. These recommendations reflect the knowledge we hold about the content and are suitable for thematic and/or cold-start recommendation settings. Evaluating thematic recommendations from user data presents unique challenges that we address by developing a method to evaluate recommendations relying on user-item ratings, yet respecting their thematic nature. We also show that the salience matrix can be estimated from user data. We demonstrate the utility of our methods by significantly improving consumption metrics in an AB test where collaborative filtering delivered subpar performance. We also apply our approach to movie recommendation using publicly-available data to ensure the reproducibility of our results. We demonstrate that our approach outperforms existing thematic recommendation methods and is even competitive with collaborative filtering approaches.
