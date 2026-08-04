---
title: "Pair counting without binning – a new approach to correlation functions in clustering statistics"
excerpt: "A binning-aware O(N log N) approach to three-point correlation functions, implemented in C++/OpenMP and validated against theory and cosmological simulations."
collection: portfolio
permalink: /portfolio/2024-10-01-3pcf-fast-algorithm/
date: 2024-10-01
category: "Research Projects"
institution: "Sun Yat-sen University"
role: "Researcher · first author"
period: "Oct 2021–Oct 2024"
status: "MNRAS 2024 · first author"
research_question: "Can three-point correlation functions be measured at modern simulation scale without explicit catalogue triplet counting?"
built: "A binning-aware in-situ convolution estimator and a C++/OpenMP measurement pipeline."
validation: "Binning-corrected perturbation theory plus MDPL2 and Quijote simulations."
result: "An O(N log N) measurement route published in MNRAS."
thumbnail: "/images/projects/3pcf-validation.png"
thumbnail_alt: "Six panels comparing measured three-point correlations with perturbation-theory predictions at three filter scales"
thumbnail_caption: "MDPL2 measurements follow the binning-corrected prediction across top-hat and Gaussian filters."
paper_url: "https://doi.org/10.1093/mnras/stae2513"
figures:
  - src: "/images/projects/3pcf-method.png"
    alt: "Schematic of triangle sampling with three spherical filters for a three-point correlation measurement"
    caption: "The estimator samples triangle configurations while filtering the density and reference fields at their vertices."
  - src: "/images/projects/3pcf-validation.png"
    alt: "Measured and predicted three-point correlation curves for top-hat and Gaussian filters"
    caption: "The measured signal agrees with the binning-corrected prediction; ignoring binning produces visible scale-dependent offsets."
---

The three-point correlation function (3PCF) is a key probe of large-scale structure that captures non-Gaussian information beyond the two-point function, but conventional estimators become computationally prohibitive at the scales and precision demanded by modern surveys. This project developed a new theoretical framework for 3PCF estimation that reformulates the problem from a brute-force counting exercise into a scalable signal-processing pipeline.

**Approach.** Rather than looping over galaxy triplets — an O(N³) operation — I reframed binned pair-counting as an in-situ convolution on the density field. This insight transforms the 3PCF into a sequence of filtering operations, each amenable to fast Fourier methods. The resulting algorithm achieves O(N log N) scaling, making it feasible to process datasets with hundreds of millions of particles.

**Implementation.** I built the full measurement pipeline in C++ with OpenMP shared-memory parallelism, targeting multi-core CPU architectures. The pipeline ingests particle catalogues, constructs density fields on adaptive meshes, performs the convolution-based estimator, and outputs multipole-expanded 3PCF measurements in Legendre polynomial bases. I validated the implementation against analytical predictions from binning-corrected tree-level perturbation theory, confirming agreement to within approximately five percent in the quasilinear regime. On the MDPL2 dark-matter simulation — containing more than 10⁸ particles — the pipeline completes a full 3PCF measurement in under eight hours on a single compute node.

**Testing and robustness.** I applied the method to Quijote halo catalogues to study how sparse-tracer sampling, shot noise, and filter-scale choices affect the recovered signal. This work directly informed the design of the estimator's window-function treatment and filtering strategies, ensuring that theoretical predictions and measurements share consistent binning conventions.

**Related publication:** [Pair counting without binning – a new approach to correlation functions in clustering statistics](https://doi.org/10.1093/mnras/stae2513) (*MNRAS*, 2024, first author).

**Skills:** C++, OpenMP, algorithm design, large-scale structure statistics, simulation validation, performance profiling.
