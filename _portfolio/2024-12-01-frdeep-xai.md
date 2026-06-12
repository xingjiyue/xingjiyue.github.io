---
title: "Interpretable Radio Galaxy Classification with FR-DEEP"
excerpt: "Built a CNN classifier for radio galaxy morphology and a LIME-based interpretability pipeline to audit model decisions. Published at IEEE URSI GASS and under revision at ApJS."
collection: portfolio
---

This project addresses the question: can we trust deep learning classifiers for radio galaxy morphology? Using the FR-DEEP dataset, we trained a CNN and built a systematic interpretability pipeline to diagnose model behavior.

## Approach

- Designed a **CNN** using **PyTorch** for FR-DEEP radio galaxy morphology classification
- Achieved ~91.4% mean test accuracy on the classification task
- Built a **LIME**-based interpretation workflow with superpixel segmentation
- Developed custom visualisation tools for saliency maps to reveal model attention patterns

## Results

The interpretation pipeline successfully identified cases where the classifier relied on background artefacts or non-physical features rather than source morphology. This enabled targeted improvements to the training strategy and informed the design of more robust classifiers.

## Publications

- *Can I trust you?* – ApJS, under revision
- IEEE URSI GASS 2023 conference proceeding (co-first author)

## Skills

PyTorch, CNN design, LIME (XAI), Python, data visualisation, model validation
