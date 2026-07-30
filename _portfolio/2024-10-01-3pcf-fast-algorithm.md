---
title: "Fast O(N log N) 3PCF Algorithm for Cosmology"
excerpt: "Developed a novel multiscale approach to the three-point correlation function, treating binned pair-counting as in-situ convolution. Implemented in C++ with OpenMP and validated on MDPL2 simulations."
collection: portfolio
permalink: /portfolio/2024-10-01-3pcf-fast-algorithm/
date: 2024-10-01
---

The three-point correlation function (3PCF) is a key probe of large-scale structure that captures non-Gaussian information beyond the two-point function, but conventional estimators become computationally prohibitive at the scales and precision demanded by modern surveys. This project developed a new theoretical framework for 3PCF estimation that reformulates the problem from a brute-force counting exercise into a scalable signal-processing pipeline.

**Approach.** Rather than looping over galaxy triplets — an O(N³) operation — I reframed binned pair-counting as an in-situ convolution on the density field. This insight transforms the 3PCF into a sequence of filtering operations, each amenable to fast Fourier methods. The resulting algorithm achieves O(N log N) scaling, making it feasible to process datasets with hundreds of millions of particles.

**Implementation.** I built the full measurement pipeline in C++ with OpenMP shared-memory parallelism, targeting multi-core CPU architectures. The pipeline ingests particle catalogues, constructs density fields on adaptive meshes, performs the convolution-based estimator, and outputs multipole-expanded 3PCF measurements in Legendre polynomial bases. I validated the implementation against analytical predictions from binning-corrected tree-level perturbation theory, confirming agreement to within approximately five percent in the quasilinear regime. On the MDPL2 dark-matter simulation — containing more than 10⁸ particles — the pipeline completes a full 3PCF measurement in under eight hours on a single compute node.

**Testing and robustness.** I applied the method to Quijote halo catalogues to study how sparse-tracer sampling, shot noise, and filter-scale choices affect the recovered signal. This work directly informed the design of the estimator's window-function treatment and filtering strategies, ensuring that theoretical predictions and measurements share consistent binning conventions.

**Related publication:** [Pair counting without binning – a new approach to correlation functions in clustering statistics](https://doi.org/10.1093/mnras/stae2513) (*MNRAS*, 2024, first author).

**Skills:** C++, OpenMP, algorithm design, large-scale structure statistics, simulation validation, performance profiling.
