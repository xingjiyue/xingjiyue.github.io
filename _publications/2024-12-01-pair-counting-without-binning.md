---
title: "Pair counting without binning – a new approach to correlation functions in clustering statistics"
collection: publications
category: manuscripts
permalink: /publication/2024-pair-counting-without-binning
excerpt: 'A first-author MNRAS paper presenting an O(N log N) approach to the three-point correlation function by treating binned pair-counting as in-situ convolution.'
date: 2024-12-01
venue: 'Monthly Notices of the Royal Astronomical Society, 535(4), 3500–3516'
publication_status: published
display_status: 'MNRAS 535(4), 3500–3516 · 2024 · published'
contribution: 'Developed the binning-aware O(N log N) estimator, implemented the C++/OpenMP pipeline, and validated it against theory and large simulations.'
project_url: '/portfolio/2024-10-01-3pcf-fast-algorithm/'
thumbnail: '/images/projects/3pcf-validation.png'
thumbnail_alt: 'Measured three-point correlation curves compared with binning-corrected perturbation-theory predictions'
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
- [Published article](https://doi.org/10.1093/mnras/stae2513)
