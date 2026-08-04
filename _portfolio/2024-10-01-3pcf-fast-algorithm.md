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

## Research question

Can the three-point correlation function (3PCF) be measured at modern simulation scale without the explicit catalogue triplet counting that makes conventional estimators prohibitively expensive?

## My role

I developed the binning-aware formalism, implemented the measurement pipeline in C++ with OpenMP, designed the numerical tests, and led the first-author MNRAS paper.

## At a glance

- **Domain:** large-scale-structure statistics and cosmological simulations
- **Core idea:** treat binned pair counting as in-situ convolution of density and reference fields
- **Implementation:** C++, OpenMP, multiresolution filtering, and FFT-based operations
- **Output:** first-author paper in *Monthly Notices of the Royal Astronomical Society*

## What I built

I built a pipeline that constructs density and reference fields, filters them at the vertices of sampled triangle configurations, and evaluates the resulting three-point statistic with consistent bin definitions. The computational route scales as O(N log N), replacing catalogue-level triplet enumeration with field operations.

## Method

The formalism connects finite separation bins to window functions in a multiresolution space. For each triangle configuration, filtered fields are evaluated at its vertices and combined in an edge-corrected estimator. The same window functions enter the perturbation-theory prediction, so measurement and theory use the same binning convention.

{% assign method_figure = page.figures[0] %}
{% include academic/figure.html src=method_figure.src alt=method_figure.alt caption=method_figure.caption %}

## Validation

I tested the estimator against binning-corrected tree-level perturbation theory and measurements from MDPL2. Quijote halo catalogues were used to examine sparse-tracer behavior, shot noise, and filter-scale choices. In the published setup, the MDPL2 measurement used more than 10<sup>8</sup> particles and completed in under eight hours on a single compute node.

{% assign result_figure = page.figures[1] %}
{% include academic/figure.html src=result_figure.src alt=result_figure.alt caption=result_figure.caption %}

## Results

The measurements follow the binning-corrected theory at the few-percent level in the quasilinear regime. The comparison also shows why treating bins only after evaluation can generate scale-dependent disagreement, especially for broader filters.

## Outputs

- [Published MNRAS paper](https://doi.org/10.1093/mnras/stae2513)
- Reusable C++/OpenMP measurement workflow for large simulation catalogues
