---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

[Download CV (PDF)](/files/cv_1.pdf){: .btn .btn--primary}

## Education

**MPhil in Physics**, The Chinese University of Hong Kong, Aug 2024–Present  
Research areas: photoionisation modelling, integral-field spectroscopy, Bayesian inference, and computational astrophysics.

**BSc in Physics**, Sun Yat-sen University, Sep 2020–Jul 2024 — GPA 3.9 / 4.0  
Undergraduate research: fast correlation-function algorithms for large-scale structure and interpretable machine learning for radio-galaxy morphology.

## Research Experience

**How to Fit All Emission Lines Simultaneously with Photoionisation Models**, CUHK, Aug 2024–Present
: Built a Python pipeline for MaNGA integral-field spectroscopy data; parallelised Cloudy photoionisation model grids across metallicity, ionisation parameter, abundance, and SED assumptions; used 3D line-ratio reprojections, KDE, RBF interpolation, and Bayesian inference to evaluate model-data tension in classical and [S III]-sensitive diagnostics.

**A Fast Statistical Algorithm for Cosmology Based on Multiscale Analysis**, Sun Yat-sen University, Oct 2021–Oct 2024
: Developed an O(N log N) three-point correlation-function algorithm treating binned pair-counting as in-situ convolution; implemented in C++ with OpenMP; validated on MDPL2 dark-matter simulations with more than 100 million particles; tested filtering strategies on Quijote halo catalogues; led first-author MNRAS paper.

**Explainable AI for Radio Galaxy Morphology Classification**, XJTLU & SYSU, Jul 2021–Aug 2021, Sep 2022–Dec 2024
: Designed a CNN classifier for FR-DEEP radio-galaxy data; built a LIME-based interpretation workflow with Felzenszwalb segmentation and custom saliency visualisation; diagnosed model attention, label inconsistency, and failure modes.

**Hunting Central Stars of Round Galactic Planetary Nebulae**, HKU, Sep 2023–Dec 2023, Sep 2025–Present
: Cross-matched HASH with PanSTARRS and DECaPS DR2 to identify CSPN candidates; quantified central-star offsets and validated candidates with Gaia DR3. Ongoing multimodal extension uses IPHAS, VPHAS+, and Gaia photometry.

## Technical Skills

**Programming:** Python, C++, LaTeX, Git, Linux  
**Data analysis:** NumPy, SciPy, Pandas, Xarray, statistical modelling, uncertainty estimation, survey cross-matching  
**Machine learning:** PyTorch, CNNs, LIME/XAI, cross-validation, model diagnostics, failure analysis  
**Scientific computing:** OpenMP, parallel workflows, batch processing, performance profiling, reproducible pipelines  
**Inference and modelling:** Bayesian inference, KDE, RBF interpolation, forward modelling, model-data comparison  
**Astronomy tools:** Cloudy, MaNGA IFU workflow, Gaia DR3, PanSTARRS, DECaPS, HASH

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
