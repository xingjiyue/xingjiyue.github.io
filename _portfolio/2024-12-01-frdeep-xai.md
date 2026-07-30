---
title: "Interpretable Radio Galaxy Classification with FR-DEEP"
excerpt: "Developed CNN and LIME-based workflows for radio-galaxy morphology classification, then extended the project with a masked Set Transformer for variable-length source-component data."
collection: portfolio
permalink: /portfolio/2024-12-01-frdeep-xai/
date: 2024-12-01
---

**Sun Yat-sen University / Tsinghua University · Jul 2021 – Oct 2024**

Deep learning can classify radio-galaxy morphology accurately, but accuracy alone does not show whether a model relies on physically meaningful structure. This project combined classification, interpretability, data-quality analysis, and a component-based Transformer extension to examine both model performance and model reasoning.

**CNN and data-quality evaluation.** I curated and quality-tagged 650 radio images and trained a PyTorch CNN using source-level five-fold cross-validation. The classifier achieved 91.4% mean test accuracy. Reviewing labels, cutouts, and source quality made it possible to separate model limitations from defects in the underlying data.

**LIME interpretation.** I built a Local Interpretable Model-agnostic Explanations workflow using Felzenszwalb superpixel segmentation and repeated perturbations. Custom overlays showed whether predictions were driven by jets, lobes, hotspots, background structure, or imaging artefacts. The audit translated individual explanations into concrete data-cleaning, relabelling, and retraining recommendations.

**Masked Set Transformer extension.** I also represented each radio source as a variable-length set of detected components. A masked Set Transformer used multi-head self-attention and attention pooling to model interactions between those components without forcing every source into a fixed-length image representation. This extension is presented as implemented work; no unverified performance improvement over the CNN is claimed.

**Research outputs:** [A model local interpretation routine for deep learning based radio galaxy classification](https://www.ursi.org/proceedings/procGA23/papers/YSASummaryHongmingTang.pdf) (IEEE URSI GASS 2023, co-first author) and *Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI* (ApJS, under revision).

**Skills:** Python, PyTorch, CNNs, LIME, Felzenszwalb segmentation, Set Transformers, model evaluation, data-quality analysis, failure analysis.
