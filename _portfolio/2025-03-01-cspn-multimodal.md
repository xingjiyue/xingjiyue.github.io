---
title: "Multimodal Identification of Planetary Nebula Central Stars"
excerpt: "Cross-matched the HASH catalogue with PanSTARRS and DECaPS DR2 to identify CSPN candidates, with ongoing multimodal extension using IPHAS, VPHAS+, and Gaia."
collection: portfolio
---

Central stars of planetary nebulae (CSPNe) are the hot, compact remnants that illuminate the surrounding nebula, yet they are notoriously difficult to identify: they are often faint, embedded in bright nebulosity, and easily confused with foreground or background field stars. This project develops a systematic, data-driven approach to CSPN candidate selection, moving beyond manual inspection toward automated, reproducible identification.

**Catalogue cross-matching.** The core workflow cross-matches the HASH (Hong Kong/AAO/Strasbourg Hα) planetary nebula catalogue against wide-field optical and near-infrared imaging surveys. I queried PanSTARRS DR2 and DECaPS DR2 for sources within the reported nebula positions, recording candidate magnitudes, colours, and astrometric offsets between catalogue centres and detected point sources. Each candidate was assessed against expected CSPN properties — compactness, colour, and positional coincidence with the nebula centre.

**Validation with Gaia.** To distinguish genuine CSPNe from chance alignments, I cross-validated candidates against Gaia DR3 astrometry. Parallax and proper-motion measurements provide independent distance and kinematic constraints that help filter out unrelated field stars. Quantifying the distribution of positional offsets between catalogue coordinates and Gaia-verified central stars also revealed systematic biases in earlier HASH entries, which informs improved cross-matching strategies.

**Ongoing: multimodal extension.** The current work extends the selection framework to a multimodal setting, combining IPHAS narrow-band Hα imaging, VPHAS+ optical photometry, and Gaia astrometric parameters. The goal is to train a classifier that jointly uses imaging morphology and tabular stellar parameters to rank CSPN candidates, improving both completeness and purity over single-survey methods.

**Skills:** Python, survey data cross-matching, astrometry, Gaia DR3, PanSTARRS, DECaPS, multimodal data fusion.
