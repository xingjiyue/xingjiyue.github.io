---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

[Download CV (PDF)](/files/shiiyu-yue-cv.pdf){: .btn .btn--primary}

## Education

**MPhil in Physics**, The Chinese University of Hong Kong, Aug 2024–Present

**BSc in Physics**, Sun Yat-sen University, Sep 2020–Jul 2024 — GPA 3.9 / 4.0

## Research Experience

**How to Fit All Emission Lines Simultaneously with Photoionisation Models**, CUHK, Aug 2024–Present
: Built a Python pipeline for MaNGA integral-field spectroscopy data; parallelised Cloudy photoionisation model grids across metallicity and abundance parameters; used 3D line-ratio reprojections and Bayesian inference to evaluate model-data tension. Revised models halve the [S III] discrepancy while preserving agreement in standard line ratios.

**A Fast Statistical Algorithm for Cosmology Based on Multiscale Analysis**, Sun Yat-sen University, Oct 2021–Oct 2024
: Developed an O(N log N) three-point correlation function algorithm treating binned pair-counting as in-situ convolution; implemented in C++ with OpenMP; validated on MDPL2 dark-matter simulations (>10⁸ particles); tested filtering strategies on Quijote halo catalogues.

**Explainable AI for Radio Galaxy Morphology Classification**, XJTLU & SYSU, Jul 2021–Aug 2021, Sep 2022–Dec 2024
: Designed a CNN classifier for FR-DEEP radio galaxy data; built a LIME-based interpretation workflow with segmentation and custom visualisation to diagnose model attention and misclassification.

**Hunting Central Stars of Round Galactic Planetary Nebulae**, HKU, Sep 2023–Dec 2023, Sep 2025–Present
: Cross-matched HASH catalogue with PanSTARRS and DECaPS DR2 to identify CSPN candidates; quantified central-star offsets and validated with Gaia DR3. Ongoing multimodal extension using IPHAS, VPHAS+, and Gaia photometry.

## Skills

**Languages:** Python, C++, LaTeX \
**ML & Data:** PyTorch, NumPy, SciPy, Pandas, Xarray, CNN design, LIME (XAI), Bayesian inference, statistical modelling \
**HPC & Pipelines:** OpenMP, parallelised workflows, batch processing, reproducible analysis pipelines, regression testing \
**Domain Methods:** 2-point and 3-point correlation functions, kernel density estimation, RBF interpolation, forward modelling, model-data comparison \
**Tools:** Linux, Git, GitHub, Cloudy, MaNGA IFU spectroscopy workflow

## Awards

- **Postgraduate Studentships**, CUHK, 2024–2026
- **Outstanding Graduate**, Sun Yat-sen University, Jun 2024
- **Outstanding Graduation Thesis**, Sun Yat-sen University, Jun 2024
- **First Award Scholarship**, Sun Yat-sen University (3 consecutive years), 2021–2023
- **China Aerospace Foundation–Uniasia Aerospace Scholarship**, Nov 2021
- **Best Speaker Award**, Laboratory for Space Research, HKU

## Publications

{% include base_path %}
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Talks

  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
