---
permalink: /
title: "Shiyu Yue"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am an MPhil student in Physics at [The Chinese University of Hong Kong](https://www.phy.cuhk.edu.hk/), working at the intersection of computational astrophysics, Bayesian inference, interpretable machine learning, and scalable data analysis.

My work focuses on building reliable statistical and computational tools for complex astronomical data: from fast correlation-function estimators for large-scale structure, to explainable radio-galaxy classifiers, to photoionisation-model inference with integral-field spectroscopy.

[Research](/research/){: .btn .btn--primary} [Projects](/portfolio/){: .btn} [Publications](/publications/){: .btn} [CV](/cv/){: .btn}

## Recent News

- **Jun 2026** — Presented *"The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models"* at the Guo Shoujing Telescope (LAMOST) Workshop.
- **Jun 2026** — Paper *"Pair Counting Without Binning"* published in *Monthly Notices of the Royal Astronomical Society*, 535(4), 3500–3516.
- **Feb 2025** — *"Can I Trust You?"* submitted to *The Astrophysical Journal Supplement Series* and under revision.
- **Aug 2024** — Started MPhil in Physics at CUHK under Postgraduate Studentship.

## Research Interests

Computational astrophysics · Large-scale structure statistics · Three-point correlation functions · Bayesian inference · Interpretable deep learning · Radio-galaxy morphology · Integral-field spectroscopy · MaNGA · Cloudy photoionisation modelling · Multimodal survey-data pipelines

## Selected Work

### Fast cosmological statistics
Developed an O(N log N) three-point correlation-function pipeline in C++/OpenMP, validated on MDPL2 simulations with more than 10^8 particles and compared against binning-corrected perturbation-theory predictions.

[Read project](/portfolio/2024-10-01-3pcf-fast-algorithm/)

### Interpretable deep learning
Built a PyTorch + LIME workflow for radio-galaxy morphology classification, combining CNN performance with failure-mode analysis and visual model diagnostics.

[Read project](/portfolio/2024-12-01-frdeep-xai/)

### Bayesian photoionisation inference
Built a Cloudy + MaNGA modelling pipeline for high-dimensional model-data comparison in optical emission-line diagnostics, focusing on the persistent [S III] tension in star-forming galaxies.

[Read project](/portfolio/2024-08-01-cloudy-manga/)

### Multimodal survey-data selection
Cross-matched HASH planetary-nebula catalogues with PanSTARRS, DECaPS, and Gaia to identify central-star candidates and prepare a multimodal extension with imaging and astrometric data.

[Read project](/portfolio/2025-03-01-cspn-multimodal/)
