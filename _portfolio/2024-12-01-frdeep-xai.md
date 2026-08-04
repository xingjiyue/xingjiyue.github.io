---
title: "Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI"
excerpt: "Developed CNN and LIME-based workflows for radio-galaxy morphology classification, then extended the project with a masked Set Transformer for variable-length source-component data."
collection: portfolio
permalink: /portfolio/2024-12-01-frdeep-xai/
date: 2024-12-01
category: "Research Projects"
institution: "Sun Yat-sen University / Tsinghua University"
role: "Researcher · journal-manuscript first author"
period: "Jul 2021–Oct 2024"
status: "ApJS · under revision"
research_question: "Does a high-accuracy radio-galaxy classifier rely on physically meaningful morphology or on background and data artefacts?"
built: "A CNN classifier, Felzenszwalb/LIME audit workflow, and masked Set Transformer extension."
validation: "A review of 650 images and source-level five-fold evaluation."
result: "91.4% mean test accuracy plus identified data and model failure modes; no Transformer superiority claim."
thumbnail: "/images/projects/frdeep-method.png"
thumbnail_alt: "A radio galaxy image shown with several segmentation methods including Felzenszwalb superpixels"
thumbnail_caption: "Segmentation choice determines which source structures can be perturbed and attributed by LIME."
talk_url: "/talks/2023-11-ml-astronomy"
figures:
  - src: "/images/projects/frdeep-method.png"
    alt: "Radio galaxy image compared across quickshift, Felzenszwalb, SLIC, and watershed segmentation"
    caption: "Felzenszwalb segmentation follows the compact source morphology more closely than fixed-grid alternatives in this example."
  - src: "/images/projects/frdeep-results.png"
    alt: "Bar chart of how often physical and non-physical features contributed to FR-DEEP predictions"
    caption: "Hotspots and lobes contribute strongly, while background influence exposes an interpretable failure mode to audit."
---

**Sun Yat-sen University / Tsinghua University · Jul 2021 – Oct 2024**

Deep learning can classify radio-galaxy morphology accurately, but accuracy alone does not show whether a model relies on physically meaningful structure. This project combined classification, interpretability, data-quality analysis, and a component-based Transformer extension to examine both model performance and model reasoning.

**CNN and data-quality evaluation.** I curated and quality-tagged 650 radio images and trained a PyTorch CNN using source-level five-fold cross-validation. The classifier achieved 91.4% mean test accuracy. Reviewing labels, cutouts, and source quality made it possible to separate model limitations from defects in the underlying data.

**LIME interpretation.** I built a Local Interpretable Model-agnostic Explanations workflow using Felzenszwalb superpixel segmentation and repeated perturbations. Custom overlays showed whether predictions were driven by jets, lobes, hotspots, background structure, or imaging artefacts. The audit translated individual explanations into concrete data-cleaning, relabelling, and retraining recommendations.

**Masked Set Transformer extension.** I also represented each radio source as a variable-length set of detected components. A masked Set Transformer used multi-head self-attention and attention pooling to model interactions between those components without forcing every source into a fixed-length image representation. This extension is presented as implemented work; no unverified performance improvement over the CNN is claimed.

**Research outputs:** [A model local interpretation routine for deep learning based radio galaxy classification](https://www.ursi.org/proceedings/procGA23/papers/YSASummaryHongmingTang.pdf) (IEEE URSI GASS 2023, co-first author) and *Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI* (ApJS, under revision).

**Skills:** Python, PyTorch, CNNs, LIME, Felzenszwalb segmentation, Set Transformers, model evaluation, data-quality analysis, failure analysis.
