---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

My research lies at the intersection of computational astrophysics, statistical inference, and interpretable machine learning. I build methods and pipelines for extracting robust physical information from large, noisy, and high-dimensional astronomical datasets.

## Research directions

### Cosmological statistics and scalable algorithms

I develop fast estimators for correlation functions and large-scale-structure statistics, with emphasis on computational scaling, binning-aware theory, numerical validation, and simulation-based testing. My first-author MNRAS work reformulates pair counting as an in-situ convolution problem, enabling an O(N log N) route to three-point correlation-function measurements on large simulations.

**Related project:** [Fast O(N log N) 3PCF Algorithm for Cosmology](/portfolio/2024-10-01-3pcf-fast-algorithm/)

### Interpretable machine learning for astronomical images

I use explainable-AI methods to audit deep-learning classifiers, diagnose failure modes, and evaluate whether model decisions are physically meaningful. In the FR-DEEP radio-galaxy project, I combined CNN classification with LIME-based local explanations to test whether the classifier attends to jets, lobes, and hotspots rather than background artefacts or label-inconsistent structures.

**Related project:** [Interpretable Radio Galaxy Classification with FR-DEEP](/portfolio/2024-12-01-frdeep-xai/)

### Bayesian inference for emission-line diagnostics

I compare photoionisation models against integral-field spectroscopy using 3D diagnostic spaces, interpolation, density estimation, and Bayesian parameter inference. My current MPhil work focuses on whether Cloudy photoionisation models can reproduce classical optical diagnostics and [S III]-sensitive line ratios simultaneously in MaNGA star-forming galaxies.

**Related project:** [Photoionisation Model Inference with Cloudy and MaNGA](/portfolio/2024-08-01-cloudy-manga/)

### Multimodal survey-data pipelines

I also work on catalogue cross-matching and multimodal candidate selection, including the identification of planetary-nebula central-star candidates using HASH, PanSTARRS, DECaPS, Gaia, and ongoing IPHAS/VPHAS+ extensions.

**Related project:** [Multimodal Identification of Planetary Nebula Central Stars](/portfolio/2025-03-01-cspn-multimodal/)
