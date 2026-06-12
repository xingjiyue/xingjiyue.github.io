---
title: "Fast O(N log N) 3PCF Algorithm for Cosmology"
excerpt: "Developed a novel multiscale approach to the three-point correlation function, treating binned pair-counting as in-situ convolution. Implemented in C++ with OpenMP and validated on MDPL2 simulations."
collection: portfolio
---

This project developed a new theoretical framework for computing the three-point correlation function (3PCF) that achieves O(N log N) scaling by reformulating binned pair-counting as an in-situ convolution operation.

## Approach

- Derived a formalism that eliminates the need for discrete bin edges in 3PCF estimation
- Implemented the algorithm in **C++** with **OpenMP** parallelism for shared-memory HPC
- Validated against **MDPL2** dark-matter simulation (>10⁸ particles) with sub-8-hour runtime
- Tested filtering and smoothing strategies on **Quijote** halo catalogues

## Results

The method recovers the 3PCF signal in agreement with binning-corrected tree-level perturbation theory to within ~5% in the quasilinear regime, while significantly reducing computational cost compared to conventional brute-force triple-counting.

## Skills

C++, OpenMP, algorithm design, simulation validation, large-scale structure statistics
