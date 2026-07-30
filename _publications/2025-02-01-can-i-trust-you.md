---
title: "Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI"
collection: publications
category: manuscripts
permalink: /publication/2025-can-i-trust-you
excerpt: 'A systematic evaluation of CNN-based radio galaxy morphology classification using LIME-based interpretability, with custom visualisation to reveal model attention patterns and failure modes.'
date: 2025-02-01
venue: 'The Astrophysical Journal Supplement Series'
publication_status: under_revision
citation: 'Yue, S., Tang, H. et al. (2025). "Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI." <i>ApJS</i>, under revision.'
---
This work investigates whether a CNN classifier trained on the FR-DEEP dataset can be trusted for radio galaxy morphology classification. Using LIME-based interpretability methods, we systematically audit model decisions across different source populations and morphologies.

## Key contributions

- Trained a CNN achieving ~91.4% mean test accuracy on FR-DEEP radio galaxy classification
- Built a LIME-based interpretation pipeline with superpixel segmentation and custom saliency visualisation
- Identified specific failure modes where the model relies on non-physical features or background artefacts
- Proposed interpretability-aware training strategies for radio astronomy deep learning pipelines
