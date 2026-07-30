---
title: "Interpretable Radio Galaxy Classification with FR-DEEP"
excerpt: "Built a CNN classifier for radio-galaxy morphology and a LIME-based interpretability pipeline to audit model attention, label consistency, and failure modes."
collection: portfolio
---

## Summary

Built a CNN plus LIME interpretation workflow for radio-galaxy morphology classification, using explainable AI to test whether model decisions are physically meaningful rather than driven only by background artefacts or dataset bias.

| Item | Details |
|---|---|
| Role | Model design, training, interpretability workflow, visualisation, failure analysis, manuscript writing |
| Data | FR-DEEP / FIRST radio-galaxy image cutouts |
| Methods | CNN classification, five-fold cross-validation, LIME, Felzenszwalb superpixel segmentation, saliency-map diagnostics |
| Implementation | Python, PyTorch, image segmentation, custom visualisation tools |
| Result | About 91.4 percent mean test accuracy with systematic model-attention diagnostics |
| Output | IEEE URSI GASS 2023 proceeding; ApJS manuscript under revision |

## Problem

Deep learning models can classify radio-galaxy morphology with high accuracy, but high accuracy alone does not prove that the model uses physically meaningful information. In radio astronomy, a classifier may learn survey artefacts, background noise, resolution effects, or label inconsistencies rather than the jets, lobes, and hotspots that define source morphology.

## Method

I trained a convolutional neural network on FR-DEEP radio-galaxy cutouts and evaluated it with a five-fold cross-validation protocol. To interpret the classifier, I built a LIME-based local explanation pipeline. Each image is segmented into superpixels, perturbed to test local prediction sensitivity, and visualised as a saliency map over the original FIRST cutout.

## Model auditing

The interpretation pipeline made it possible to inspect whether the classifier attends to physically relevant radio structures. I used the saliency maps to diagnose cases where the model focused on background regions, isolated compact components, low-resolution structures, or morphology that conflicted with the assigned label. A manual re-inspection of 650 FIRST cutouts helped connect model behaviour to data quality and label reliability.

## Results

The classifier achieved about 91.4 percent mean test accuracy, but the more important result was the failure taxonomy: interpretability revealed where the model was reliable, where the input data were limiting, and where label or morphology ambiguity affected performance. This supported the argument that explainability should be part of the radio-galaxy classification pipeline, not a decorative post-processing step.

## My contribution

I contributed to CNN model development, LIME explanation design, visualisation, failure-mode inspection, interpretation of radio morphology, and manuscript preparation.

## Technical relevance

This project demonstrates practical machine-learning evaluation beyond accuracy: cross-validation, visual diagnostics, feature-attribution analysis, label-noise inspection, failure-mode taxonomy, and communication of model reliability to domain scientists.

## Related publications

- [Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI](/publication/2025-can-i-trust-you) — *The Astrophysical Journal Supplement Series*, under revision.
- [A model local interpretation routine for deep learning based radio galaxy classification](/publication/2023-local-interpretation-radio-galaxy) — IEEE URSI GASS 2023, co-first author.
