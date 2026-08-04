---
title: "The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models"
excerpt: "Built a Python and Cloudy workflow for MaNGA spectroscopy, 3D line-ratio diagnostics, and Bayesian model–data comparison; work on the [S III] discrepancy was submitted to A&A in August 2026."
collection: portfolio
permalink: /portfolio/2024-08-01-cloudy-manga/
date: 2024-08-01
category: "Research Projects"
institution: "The Chinese University of Hong Kong"
role: "MPhil researcher"
period: "Aug 2024–Oct 2026 (expected)"
status: "A&A · submitted Aug 2026"
research_question: "Can one photoionisation-model configuration reproduce classical optical diagnostics and [S III]-sensitive line ratios simultaneously?"
built: "Cloudy grids and a MaNGA 3D model–data comparison and Bayesian-inference pipeline."
validation: "Joint optical diagnostic spaces, KDE, RBF interpolation, model–data distances, and spaxel-level inference."
result: "Abundance shifts do not reconcile all diagnostics; the ionising SED and model physics remain leading directions. Submitted to A&A in Aug 2026."
thumbnail: "/images/projects/siii-results.png"
thumbnail_alt: "Joint sulphur and standard optical diagnostic result showing incompatible preferred abundance shifts"
thumbnail_caption: "The tested abundance shifts cannot minimize the sulphur-sensitive and standard optical diagnostics at the same point."
talk_url: "/talks/2026-05-guoshoujing"
figures:
  - src: "/images/projects/siii-method.png"
    alt: "Distance-matrix workflow comparing MaNGA data density with interpolated Cloudy model surfaces"
    caption: "Observed density and interpolated model surfaces are compared within reprojected diagnostic planes to obtain a quantitative distance."
  - src: "/images/projects/siii-results.png"
    alt: "Combined diagnostic result demonstrating incompatible abundance shifts for sulphur and standard optical line ratios"
    caption: "Sulphur-sensitive and standard diagnostics prefer incompatible abundance shifts, so chemistry changes alone do not resolve the tension."
---

Optical emission-line ratios are the workhorse diagnostic of ionised gas in galaxies, and standard photoionisation models — computed with codes like Cloudy — are routinely used to interpret them. But can these models simultaneously reproduce the full set of emission lines observed in modern integral-field spectroscopy? This project confronts that question using data from the MaNGA survey.

**Pipeline architecture.** I built an end-to-end Python pipeline that ingests MaNGA IFU data, extracts star-forming spaxels using BPT classification, and computes a comprehensive set of emission-line fluxes. On the modelling side, I parallelised Cloudy to generate large grids spanning metallicity, ionisation parameter, and elemental abundance variations — particularly sulphur, which has emerged as a persistent discrepancy in the literature. The pipeline automates batch submission, result collection, and quality filtering, making it practical to explore high-dimensional parameter spaces.

**Model-data comparison.** Rather than relying solely on traditional 2D BPT diagrams — where model overlap can mask real discrepancies — I adopted a 3D reprojection approach that reveals model-data tension more clearly. I used kernel density estimation to summarise the observed spaxel distribution and radial basis function interpolation to construct continuous model surfaces, enabling quantitative scoring of candidate models against the data. Bayesian inference at the individual spaxel level provides metallicity and ionisation-parameter estimates with formal uncertainties.

**Key findings.** Standard Cloudy models over-predict [S III] λ9530 Å line strengths by approximately a factor of three relative to the MaNGA data. A revised model configuration — with sulphur abundance approximately 0.3 dex lower and gas metallicity about 0.6 dex higher than the stellar value — reduces this discrepancy by roughly half while preserving good agreement in standard line-ratio diagnostics such as [N II]/Hα and [O III]/Hβ. This demonstrates that even widely used photoionisation models require careful empirical validation against modern IFU datasets.

**Research output.** Work on the [S III] discrepancy was submitted to *Astronomy & Astrophysics* in August 2026. The manuscript status is reported as submitted, not accepted or published.

**Skills:** Python, Cloudy, Bayesian inference, MaNGA IFU spectroscopy, KDE, RBF interpolation, high-dimensional visualisation, model validation.
