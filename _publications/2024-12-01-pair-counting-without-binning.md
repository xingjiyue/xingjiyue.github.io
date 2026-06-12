---
title: "Pair counting without binning – a new approach to correlation functions in clustering statistics"
collection: publications
category: manuscripts
permalink: /publication/2024-pair-counting-without-binning
excerpt: 'A novel O(N log N) approach to the three-point correlation function that treats binned pair-counting as in-situ convolution, validated on large-scale dark-matter simulations.'
date: 2024-12-01
venue: 'Monthly Notices of the Royal Astronomical Society, 535(4), 3500–3516'
citation: 'Yue, S., Feng, L. et al. (2024). "Pair counting without binning – a new approach to correlation functions in clustering statistics." <i>MNRAS</i>, 535(4), 3500–3516.'
---
This paper presents a new theoretical framework for computing the three-point correlation function (3PCF) that replaces conventional binning with an in-situ convolution approach. The method achieves O(N log N) scaling and was validated on the MDPL2 dark-matter simulation with more than 10⁸ particles.

## Key contributions

- Derived a formalism that treats binned pair-counting as convolution, eliminating the need for discrete bin edges
- Implemented the algorithm in C++ with OpenMP parallelism, achieving sub-8-hour runtime on MDPL2-scale data
- Validated against binning-corrected tree-level perturbation theory, with agreement within ~5% in the quasilinear regime
- Tested filtering strategies on Quijote halo catalogues to assess robustness to survey systematics
