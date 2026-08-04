---
title: "Hunting Central Stars of Round Galactic Planetary Nebulae"
excerpt: "Integrated four heterogeneous survey sources, applied coordinate-based matching and Gaia validation, and explored a multimodal extension for CSPN candidate selection."
collection: portfolio
permalink: /portfolio/2025-03-01-cspn-multimodal/
date: 2025-03-01
category: "Research Projects"
institution: "The University of Hong Kong Space Laboratory"
role: "Research project participant"
period: "Sep–Dec 2023"
status: "Research project · Best Speaker presentation"
research_question: "How can faint central-star candidates be reconciled across surveys and separated from unrelated field sources?"
built: "A HASH, PanSTARRS, DECaPS, and Gaia reconciliation and candidate-control workflow."
validation: "Positional offsets, duplicate handling, contamination checks, and Gaia astrometry."
result: "A reviewed candidate pipeline and a multimodal extension explored within the Sep–Dec 2023 project."
thumbnail: "/images/projects/cspn-workflow.svg"
thumbnail_alt: "Workflow from HASH targets through survey reconciliation and Gaia validation to reviewed central-star candidates"
thumbnail_caption: "Source identifiers and validation evidence remain traceable from the target list to the reviewed candidates."
talk_url: "/talks/2023-12-lsr-jamboree"
figures:
  - src: "/images/projects/cspn-workflow.svg"
    alt: "HASH, PanSTARRS, DECaPS, and Gaia source-reconciliation workflow"
    caption: "The workflow controls positional offsets and duplicates before Gaia astrometry is used as an external candidate check."
---

## Research question

How can faint central-star candidates in round Galactic planetary nebulae be reconciled across heterogeneous surveys and separated from unrelated field sources?

## My role

During the Sep–Dec 2023 project at The University of Hong Kong Space Laboratory, I integrated survey records, implemented coordinate-based candidate matching and quality controls, used Gaia for external checks, and explored a multimodal extension.

## At a glance

- **Inputs:** HASH targets, PanSTARRS, DECaPS, and Gaia
- **Controls:** schema normalization, coordinate offsets, duplicates, and contamination
- **Extension:** image plus photometric/astrometric multimodal candidate screening
- **Presentation:** Best Speaker Award at the HKU Laboratory for Space Research Jamboree

## What I built

I built a reproducible reconciliation workflow that standardized source fields, retained source identifiers, matched detections around nebular targets, and recorded why a candidate was accepted, rejected, or flagged for review.

## Method

HASH supplied the target list. PanSTARRS and DECaPS detections were reconciled by position while preserving the provenance of each source record. Offset statistics and duplicate rules controlled ambiguous matches before candidate-level information was assembled.

{% assign workflow_figure = page.figures[0] %}
{% include academic/figure.html src=workflow_figure.src alt=workflow_figure.alt caption=workflow_figure.caption %}

## Validation

I compared positional offsets, overlap across imaging sources, photometric consistency, and foreground/background contamination. Gaia astrometry supplied an independent consistency check on candidate distance and motion.

## Results

The project produced a traceable candidate-selection workflow and a reviewed set of candidate evidence. A multimodal design combining images with photometric and astrometric parameters was explored within the completed Sep–Dec 2023 project; it is not described as an ongoing production system.

## Outputs

- [Hunting Central Stars of Round Galactic Planetary Nebulae — HKU Jamboree talk](/talks/2023-12-lsr-jamboree)
- Best Speaker Award, Laboratory for Space Research Jamboree
