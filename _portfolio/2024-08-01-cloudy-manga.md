---
title: "Photoionisation Model Inference with Cloudy and MaNGA"
excerpt: "Built a Python pipeline to parallelise Cloudy model grids and compare them against MaNGA IFU spectroscopy using 3D line-ratio reprojections and Bayesian inference."
collection: portfolio
---

This project investigates whether standard photoionisation models can simultaneously reproduce the full set of emission lines observed in MaNGA integral-field spectroscopy data. The answer: not without modifications.

## Approach

- Built a **Python** pipeline to ingest and preprocess **MaNGA** IFU spectroscopy data
- Parallelised **Cloudy** photoionisation model grids across metallicity and abundance parameter space
- Used 3D line-ratio reprojections (extending the BPT diagnostic) to visualise model-data tension
- Applied **Bayesian inference** to formally quantify discrepancies and identify promising model revisions

## Results

Standard photoionisation models over-predict [S III] line strengths by a factor of ~3. Our revised models halve this discrepancy while preserving agreement in standard line-ratio diagnostics (e.g., [N II]/Hα and [O III]/Hβ). This demonstrates that even widely used models require careful validation against modern IFU data.

## Skills

Python, Cloudy, Bayesian inference, MaNGA IFU spectroscopy, high-dimensional visualisation, model validation
