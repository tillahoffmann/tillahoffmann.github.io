---
layout: publication
title: Approximate Inference for Longitudinal Mechanistic HIV Contact Networks
type: article
venue: arXiv
doi: 10.48550/arXiv.2401.04771
author:
- osmiley
- me
- jponnela
---

Network models are increasingly used to study infectious disease spread. Exponential Random Graph models have a history in this area, with scalable inference methods now available. An alternative approach uses mechanistic network models. Mechanistic network models directly capture individual behaviors, making them suitable for studying sexually transmitted diseases. Combining mechanistic models with Approximate Bayesian Computation allows flexible modeling using domain-specific interaction rules among agents, avoiding network model oversimplifications. These models are ideal for longitudinal settings as they explicitly incorporate network evolution over time. We implemented a discrete-time version of a previously published continuous-time model of evolving contact networks for men who have sex with men (MSM) and proposed an ABC-based approximate inference scheme for it. As expected, we found that a two-wave longitudinal study design improves the accuracy of inference compared to a cross-sectional design. However, the gains in precision in collecting data twice, up to 18%, depend on the spacing of the two waves and are sensitive to the choice of summary statistics. In addition to methodological developments, our results inform the design of future longitudinal network studies in sexually transmitted diseases, specifically in terms of what data to collect from participants and when to do so.
