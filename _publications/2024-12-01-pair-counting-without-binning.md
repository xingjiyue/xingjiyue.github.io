---
title: "Pair counting without binning – a new approach to correlation functions in clustering statistics"
collection: publications
category: manuscripts
permalink: /publication/2024-pair-counting-without-binning
excerpt: 'A first-author MNRAS paper presenting an O(N log N) approach to the three-point correlation function by treating binned pair-counting as in-situ convolution.'
date: 2024-12-01
venue: 'Monthly Notices of the Royal Astronomical Society, 535(4), 3500–3516'
publication_status: published
paperurl: 'https://doi.org/10.1093/mnras/stae2513'
citation: 'Yue, S., Feng, L. et al. (2024). "Pair counting without binning – a new approach to correlation functions in clustering statistics." <i>MNRAS</i>, 535(4), 3500–3516.'
---

This first-author paper presents a theoretical and computational framework for computing correlation functions without relying on conventional discrete binning. The method treats binned pair-counting as an in-situ convolution problem, giving an O(N log N) route to three-point correlation-function measurements on large cosmological simulations.

## Key contributions

- Derived a binning-aware formalism that connects pair counting, filtering, and field convolution
- Implemented the 3PCF measurement pipeline in C++ with OpenMP parallelism
- Validated the method on MDPL2-scale dark-matter simulations with more than 100 million particles
- Compared measurements against binning-corrected perturbation-theory predictions, reaching few-percent agreement in the quasilinear regime
- Tested filtering strategies on Quijote halo catalogues to study sparse-tracer behaviour and robustness

## Links

- [Related project](/portfolio/2024-10-01-3pcf-fast-algorithm/)
- DOI / arXiv / code: to be added when the canonical public links are finalised
