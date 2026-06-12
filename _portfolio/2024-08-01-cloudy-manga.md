---
title: "Photoionisation Model Inference with Cloudy and MaNGA"
excerpt: "Built a Python pipeline to parallelise Cloudy model grids and compare them against MaNGA IFU spectroscopy using 3D line-ratio spaces, interpolation, KDE, and Bayesian inference."
collection: portfolio
---

## Summary

Built a Cloudy plus MaNGA inference pipeline to test whether photoionisation models can reproduce multiple optical emission-line diagnostics simultaneously in star-forming galaxies.

| Item | Details |
|---|---|
| Role | Pipeline development, Cloudy grid generation, diagnostic-space design, Bayesian inference, visualisation, scientific interpretation |
| Data | MaNGA IFU spectroscopy; star-forming spaxels selected with standard optical diagnostics |
| Methods | BPT selection, 3D line-ratio reprojection, KDE, RBF interpolation, grid search, Bayesian parameter inference |
| Implementation | Python, Cloudy, parallel batch processing, reproducible plotting pipeline |
| Result | Identified a persistent [S III]-sensitive tension that is hidden in classical 2D diagnostic diagrams |
| Output | Current MPhil research project; conference talk and paper draft |

## Problem

Photoionisation models are widely used to infer physical conditions in ionised gas, but agreement in classical 2D BPT diagrams does not guarantee that all relevant emission lines are reproduced simultaneously. This project asks whether Cloudy model grids can match MaNGA star-forming spaxels across classical optical ratios and [S III]-sensitive diagnostics at the same time.

## Pipeline

I built an end-to-end Python pipeline that ingests MaNGA IFU measurements, selects star-forming spaxels, computes emission-line ratios, and compares the observed spaxel distribution against Cloudy model grids. On the modelling side, I parallelised Cloudy runs over metallicity, ionisation parameter, density, elemental abundances, and SED assumptions. The pipeline automates batch submission, result collection, quality filtering, interpolation, and figure generation.

## Model-data comparison

Instead of relying only on traditional 2D BPT projections, I used 3D diagnostic spaces to expose model-data tension that can be hidden by projection. Kernel density estimation summarises the observed spaxel distribution, while radial basis function interpolation constructs continuous model surfaces over discrete Cloudy grids. Bayesian inference is then used to estimate metallicity and ionisation parameter for individual spaxels and to compare candidate model configurations.

## Key findings

The main result is that classical diagnostics such as [N II]/Hα, [S II]/Hα, and [O III]/Hβ can be reproduced while [S III]-sensitive diagnostics still show a systematic discrepancy. In the current paper framing, the tension is treated as evidence that abundance-only changes are unlikely to be a complete solution; SED assumptions and model physics remain leading explanations that require further testing.

## My contribution

I developed the data-processing and modelling pipeline, generated and organised Cloudy grids, designed the 3D diagnostic-space comparison, implemented interpolation and Bayesian inference steps, produced the analysis figures, and prepared the conference and paper material.

## Technical relevance

This project demonstrates high-dimensional model validation, automated simulation management, Bayesian parameter inference, reproducible scientific visualisation, and careful interpretation of model-data residuals. These skills map directly to data-science workflows involving simulation, uncertainty, and model diagnostics.

## Related talk

[The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models](/talks/2026-05-guoshoujing) — Guo Shoujing Telescope (LAMOST) Workshop, 2026.
