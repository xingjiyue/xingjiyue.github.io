---
title: "Interpretable Radio Galaxy Classification with FR-DEEP"
excerpt: "Built a CNN classifier for radio galaxy morphology and a LIME-based interpretability pipeline to audit model decisions. Published at IEEE URSI GASS and under revision at ApJS."
collection: portfolio
---

Deep learning models achieve high accuracy on radio galaxy morphology classification, but high accuracy alone does not guarantee that the model makes decisions for physically meaningful reasons. This project addresses a deceptively simple question: can we trust a CNN classifier trained on radio survey data, or is it exploiting spurious correlations in the imaging?

**Model design and training.** I designed a convolutional neural network using PyTorch, trained on the FR-DEEP dataset of radio galaxy cutouts. Adopting a five-fold cross-validation protocol, the classifier achieved a mean test accuracy of approximately 91.4 percent across folds. But rather than stopping at a performance number, I focused on understanding what drives the classifier's decisions — especially when it fails.

**Interpretability pipeline.** I built a systematic interpretation workflow based on Local Interpretable Model-agnostic Explanations (LIME). The pipeline segments each radio image into superpixels, perturbs regions to generate counterfactual predictions, and produces saliency maps that highlight which image structures most influenced the classifier's output. I developed custom visualisation tools to overlay these saliency maps on the original FIRST survey cutouts, making it possible to inspect whether the model attends to jets, lobes, and hotspots — or to background noise and imaging artefacts.

**What we learned.** The interpretation analysis revealed several failure modes: the classifier sometimes relied on background features or label-inconsistent morphology when images were faint or poorly resolved. A manual re-inspection of 650 FIRST cutouts helped quantify the relationship between data quality, label noise, and model performance. These findings informed targeted improvements to training and data preprocessing, and they support a broader argument that interpretability should be a first-class requirement — not an afterthought — in radio astronomy deep learning.

**Related publications:** [Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI](/publication/2025-can-i-trust-you) (ApJS, under revision) and [A model local interpretation routine for deep learning based radio galaxy classification](/publication/2023-local-interpretation-radio-galaxy) (IEEE URSI GASS 2023, co-first author).

**Skills:** PyTorch, CNN design, LIME (XAI), Python, data visualisation, model validation, failure analysis.
