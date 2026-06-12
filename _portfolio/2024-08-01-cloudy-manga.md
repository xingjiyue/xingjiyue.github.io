---
title: "Photoionisation Model Inference with Cloudy and MaNGA"
excerpt: "Built a Python pipeline to parallelise Cloudy model grids and compare them against MaNGA IFU spectroscopy using 3D line-ratio reprojections and Bayesian inference."
collection: portfolio
---

Optical emission-line ratios are the workhorse diagnostic of ionised gas in galaxies, and standard photoionisation models — computed with codes like Cloudy — are routinely used to interpret them. But can these models simultaneously reproduce the full set of emission lines observed in modern integral-field spectroscopy? This project confronts that question using data from the MaNGA survey.

**Pipeline architecture.** I built an end-to-end Python pipeline that ingests MaNGA IFU data, extracts star-forming spaxels using BPT classification, and computes a comprehensive set of emission-line fluxes. On the modelling side, I parallelised Cloudy to generate large grids spanning metallicity, ionisation parameter, and elemental abundance variations — particularly sulphur, which has emerged as a persistent discrepancy in the literature. The pipeline automates batch submission, result collection, and quality filtering, making it practical to explore high-dimensional parameter spaces.

**Model-data comparison.** Rather than relying solely on traditional 2D BPT diagrams — where model overlap can mask real discrepancies — I adopted a 3D reprojection approach that reveals model-data tension more clearly. I used kernel density estimation to summarise the observed spaxel distribution and radial basis function interpolation to construct continuous model surfaces, enabling quantitative scoring of candidate models against the data. Bayesian inference at the individual spaxel level provides metallicity and ionisation-parameter estimates with formal uncertainties.

**Key findings.** Standard Cloudy models over-predict [S III] λ9530 Å line strengths by approximately a factor of three relative to the MaNGA data. A revised model configuration — with sulphur abundance approximately 0.3 dex lower and gas metallicity about 0.6 dex higher than the stellar value — reduces this discrepancy by roughly half while preserving good agreement in standard line-ratio diagnostics such as [N II]/Hα and [O III]/Hβ. This demonstrates that even widely used photoionisation models require careful empirical validation against modern IFU datasets.

**Skills:** Python, Cloudy, Bayesian inference, MaNGA IFU spectroscopy, KDE, RBF interpolation, high-dimensional visualisation, model validation.
