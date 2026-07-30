---
title: "Fast O(N log N) 3PCF Algorithm for Cosmology"
excerpt: "Developed a scalable three-point correlation-function framework by treating binned pair-counting as in-situ convolution. Implemented in C++/OpenMP and validated on MDPL2 and Quijote simulations."
collection: portfolio
---

## Summary

Developed a scalable O(N log N) estimator for the three-point correlation function (3PCF), turning pair counting into an in-situ convolution problem and enabling measurements on large cosmological simulations.

| Item | Details |
|---|---|
| Role | First-author research project; algorithm design, implementation, validation, and writing |
| Data | MDPL2 dark-matter simulation; Quijote halo catalogues |
| Methods | Binning-aware correlation statistics, multiscale filtering, in-situ convolution, Legendre multipole expansion |
| Implementation | C++, OpenMP, Python validation and plotting scripts |
| Result | Full 3PCF measurement on more than 100 million particles in under 8 hours; about 5 percent agreement with binning-corrected theory in the quasilinear regime |
| Output | First-author MNRAS paper |

## Problem

The three-point correlation function is a key statistic for non-Gaussian information in large-scale structure, but conventional triplet-counting estimators are computationally expensive and difficult to apply directly to modern simulations and survey-scale datasets. This project asks whether the counting problem can be reformulated so that the measurement and the theoretical prediction handle binning consistently.

## Method

Rather than looping over every triplet, I reframed binned pair-counting as an in-situ convolution on the density field. The resulting estimator transforms the 3PCF measurement into a sequence of filtering and convolution operations. The framework was connected to binning-corrected tree-level perturbation theory so that measurements and predictions use the same window-function treatment.

## Implementation and validation

I built the measurement pipeline in C++ with OpenMP shared-memory parallelism. The code ingests particle catalogues, constructs density-field representations, applies multiscale filters, computes multipole-expanded statistics, and exports results for Python-based validation and visualisation. I tested the pipeline on MDPL2-scale dark-matter simulations and Quijote halo catalogues, focusing on numerical accuracy, sparse-tracer behaviour, shot noise, and filter-radius choices.

## Results

The pipeline completes a full 3PCF measurement on more than 100 million particles within a practical runtime. In the quasilinear regime, the measured signal agrees with binning-corrected perturbation-theory predictions at the few-percent level, demonstrating that the algorithm is both computationally scalable and physically interpretable.

## My contribution

I developed the core theoretical reformulation, implemented the C++/OpenMP pipeline, designed the validation tests, produced the analysis figures, and wrote the first-author paper.

## Technical relevance

This project demonstrates scalable algorithm design, high-performance C++ implementation, numerical validation, performance profiling, and large-scale simulation data processing. The same skills transfer naturally to large data pipelines, statistical computing, and simulation-based inference.

## Related publication

[Pair counting without binning – a new approach to correlation functions in clustering statistics](/publication/2024-pair-counting-without-binning) — *Monthly Notices of the Royal Astronomical Society*, 535(4), 3500–3516, first author.
