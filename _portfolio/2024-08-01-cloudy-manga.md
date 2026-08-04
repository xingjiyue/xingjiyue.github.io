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

## Research question

Can one photoionisation-model configuration reproduce classical optical diagnostics and [S III]-sensitive line ratios simultaneously for MaNGA star-forming regions?

## My role

I built the MaNGA and Cloudy analysis pipeline, generated and organized model grids, designed the reprojected diagnostic comparison, and implemented quantitative model–data distance and Bayesian inference steps for my MPhil research.

## At a glance

- **Data:** MaNGA integral-field spectroscopy, selected at the star-forming-spaxel level
- **Models:** parallel Cloudy grids spanning metallicity, ionisation parameter, and abundance variations
- **Comparison:** 3D diagnostic reprojection, KDE, RBF interpolation, and model–data distances
- **Status:** submitted to *Astronomy & Astrophysics* in Aug 2026

## What I built

The Python workflow ingests MaNGA line measurements, selects star-forming spaxels, filters low-quality measurements, and constructs observed diagnostic distributions. On the model side, it schedules Cloudy grids, collects valid runs, and converts them into continuously interpolated diagnostic surfaces suitable for joint comparison and spaxel-level inference.

## Method

Traditional two-dimensional diagrams can hide tension when projected model grids overlap the data. I therefore reprojected combinations of line ratios into three-dimensional spaces, summarized the observed distribution with kernel density estimation, interpolated the model surface with radial basis functions, and evaluated distance within matched planes.

{% assign method_figure = page.figures[0] %}
{% include academic/figure.html src=method_figure.src alt=method_figure.alt caption=method_figure.caption %}

## Validation

Candidate configurations were required to address sulphur-sensitive and standard optical diagnostics jointly rather than improve only one projection. Per-spaxel Bayesian inference supplied metallicity and ionisation-parameter constraints, while the distance matrices exposed whether the same abundance shifts were preferred across diagnostics.

{% assign result_figure = page.figures[1] %}
{% include academic/figure.html src=result_figure.src alt=result_figure.alt caption=result_figure.caption %}

## Results

The tested abundance adjustments do not reconcile the optical diagnostics simultaneously. The remaining tension points toward the ionising-SED shape and/or additional photoionisation-model physics as leading directions for further tests. The manuscript was submitted to *Astronomy & Astrophysics* in August 2026; this status does not imply acceptance.

## Outputs

- A&A manuscript — submitted Aug 2026
- [May 2026 Guo Shoujing Telescope Workshop talk](/talks/2026-05-guoshoujing)
- [January 2026 CCBC talk](/talks/2026-01-ccbc)
