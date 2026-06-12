---
permalink: /
title: "Shiyu Yue"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<img src="/images/photo.jpg" width="260" alt="Shiyu Yue profile photo">

I am an MPhil student in Physics at [The Chinese University of Hong Kong](https://www.phy.cuhk.edu.hk/), working at the intersection of computational astrophysics, Bayesian inference, interpretable machine learning, and scalable data analysis.

My work focuses on building reliable statistical and computational tools for complex astronomical data: from fast correlation-function estimators for large-scale structure, to explainable radio-galaxy classifiers, to photoionisation-model inference with integral-field spectroscopy.

**Current focus.** I am developing a Cloudy plus MaNGA inference pipeline to test whether photoionisation models can reproduce classical optical diagnostics and [S III]-sensitive diagnostics simultaneously in star-forming galaxies.

[Research](/research/){: .btn .btn--primary} [Projects](/portfolio/){: .btn} [Publications](/publications/){: .btn} [CV](/cv/){: .btn}

## News

- **Jun 2026** — Presented *"The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models"* at the Guo Shoujing Telescope (LAMOST) Workshop.
- **Jun 2026** — Paper *"Pair Counting Without Binning"* published in *Monthly Notices of the Royal Astronomical Society*, 535(4), 3500–3516.
- **Feb 2025** — *"Can I Trust You?"* submitted to *The Astrophysical Journal Supplement Series* and under revision.
- **Aug 2024** — Started MPhil in Physics at CUHK under Postgraduate Studentship.

## Selected publications

### Pair counting without binning — a new approach to correlation functions in clustering statistics
**Shiyu Yue**, Longlong Feng, Wenjie Ju, Jun Pan, Zhiqi Huang, Feng Fang, Zhuoyang Li, Yan-Chuan Cai, Weishan Zhu. *MNRAS*, 535, 3500, 2024.

[arXiv](https://arxiv.org/abs/2408.16398){: .btn} [DOI](https://doi.org/10.1093/mnras/stae2513){: .btn} [Project](/portfolio/2024-10-01-3pcf-fast-algorithm/){: .btn}

### A model local interpretation routine for deep learning based radio galaxy classification
Hongming Tang, **Shiyu Yue**, Zijun Wang, Jizhe Lai, Leyao Wei, Yan Luo, Chuni Liang, Jiani Chu. IEEE URSI GASS 2023.

[arXiv](https://arxiv.org/abs/2307.03453){: .btn} [Project](/portfolio/2024-12-01-frdeep-xai/){: .btn}

## Selected projects

### [Fast cosmological statistics](/portfolio/2024-10-01-3pcf-fast-algorithm/)
Developed an O(N log N) three-point correlation-function pipeline in C++/OpenMP, validated on MDPL2 simulations with more than 100 million particles and compared against binning-corrected perturbation-theory predictions.

### [Interpretable deep learning](/portfolio/2024-12-01-frdeep-xai/)
Built a PyTorch plus LIME workflow for radio-galaxy morphology classification, combining CNN performance with failure-mode analysis and visual model diagnostics.

### [Bayesian photoionisation inference](/portfolio/2024-08-01-cloudy-manga/)
Built a Cloudy plus MaNGA modelling pipeline for high-dimensional model-data comparison in optical emission-line diagnostics, focusing on the persistent [S III] tension in star-forming galaxies.

### [Multimodal survey-data selection](/portfolio/2025-03-01-cspn-multimodal/)
Cross-matched HASH planetary-nebula catalogues with PanSTARRS, DECaPS, and Gaia to identify central-star candidates and prepare a multimodal extension with imaging and astrometric data.
