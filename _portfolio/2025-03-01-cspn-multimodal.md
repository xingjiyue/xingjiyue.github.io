---
title: "Multimodal Identification of Planetary Nebula Central Stars"
excerpt: "Cross-matched HASH with PanSTARRS, DECaPS DR2, and Gaia DR3 to identify CSPN candidates, with ongoing multimodal extension using IPHAS, VPHAS+, and Gaia."
collection: portfolio
---

## Summary

Developed a reproducible candidate-selection workflow for identifying central stars of planetary nebulae, combining catalogue cross-matching, imaging-survey photometry, and Gaia astrometry.

| Item | Details |
|---|---|
| Role | Catalogue querying, cross-matching, candidate filtering, validation, visual inspection, multimodal extension |
| Data | HASH planetary-nebula catalogue; PanSTARRS; DECaPS DR2; Gaia DR3; ongoing IPHAS and VPHAS+ extension |
| Methods | Positional cross-matching, photometric filtering, astrometric validation, offset analysis, multimodal candidate ranking |
| Implementation | Python, survey-data queries, table processing, visual inspection and validation scripts |
| Result | Built a systematic workflow for ranking CSPN candidates and quantifying central-star offset behaviour |
| Output | HKU Laboratory for Space Research presentation; Best Speaker Award |

## Problem

Central stars of planetary nebulae are often faint, compact, and embedded in bright nebulosity. Catalogue positions can also be uncertain, making manual identification slow and difficult to reproduce. This project develops a data-driven approach to candidate selection.

## Catalogue cross-matching

The core workflow cross-matches the HASH planetary-nebula catalogue against wide-field imaging surveys. I queried PanSTARRS and DECaPS DR2 for sources near reported nebula positions, recording candidate magnitudes, colours, and angular offsets between catalogue centres and detected point sources. Candidates were then assessed using compactness, colour, and positional coincidence.

## Gaia validation

I cross-validated candidate sources with Gaia DR3 astrometry. Parallax and proper-motion information help reject unrelated field stars and identify candidates with plausible central-star properties. The offset distribution between catalogue centres and Gaia-supported candidates also provides information about systematic positional uncertainties in earlier catalogue entries.

## Ongoing multimodal extension

The current extension combines IPHAS narrow-band H-alpha imaging, VPHAS+ optical photometry, and Gaia astrometric parameters. The goal is to train a classifier or ranking model that jointly uses imaging morphology and tabular stellar parameters, improving candidate completeness and purity relative to single-survey selection.

## My contribution

I built the cross-matching workflow, processed survey catalogues, designed candidate filters, inspected candidate images, validated sources with Gaia DR3, and prepared the presentation material.

## Technical relevance

This project demonstrates catalogue-scale data integration, multimodal feature construction, astrometric validation, candidate ranking, and reproducible survey-data processing.

## Related talk

[Hunting Central Stars of Round Galactic Planetary Nebulae](/talks/2023-12-lsr-jamboree) — Annual Research Jamboree, Laboratory for Space Research, HKU.
