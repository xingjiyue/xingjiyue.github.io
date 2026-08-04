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

## Research question

When a radio-galaxy classifier reaches high accuracy, is it using jets, lobes, and hotspots, or is it relying on background structure, image artefacts, or inconsistent labels?

## My role

Across the Sun Yat-sen University / Tsinghua University collaboration, I reviewed the dataset, trained and evaluated the CNN, built the LIME interpretation pipeline, analyzed failure modes, and implemented the masked Set Transformer extension.

## At a glance

- **Period:** Jul 2021–Oct 2024
- **Data:** 650 reviewed FR-DEEP radio images
- **Evaluation:** source-level five-fold splits; 91.4% mean test accuracy
- **Interpretability:** Felzenszwalb segmentation and repeated LIME perturbations
- **Status:** ApJS manuscript under revision

## What I built

I built a PyTorch CNN workflow with quality tagging and source-level evaluation, then added custom LIME visualizations that rank positive and negative superpixel contributions. I also implemented a masked Set Transformer for variable-length sets of detected radio-source components.

## Method

The interpretability workflow compares segmentation schemes before applying LIME. Felzenszwalb superpixels were used to perturb locally coherent regions, and the resulting weights were rendered in multiple modes so that differences between jets, lobes, hotspots, cores, background, and artefacts could be inspected consistently.

{% assign method_figure = page.figures[0] %}
{% include academic/figure.html src=method_figure.src alt=method_figure.alt caption=method_figure.caption %}

## Validation

I reviewed labels and cutouts for all 650 images and used source-level five-fold evaluation to reduce leakage between related samples. Explanations were grouped by physical and non-physical feature types, allowing accuracy, data quality, and model rationale to be assessed separately.

{% assign result_figure = page.figures[1] %}
{% include academic/figure.html src=result_figure.src alt=result_figure.alt caption=result_figure.caption %}

## Results

The CNN achieved 91.4% mean test accuracy. LIME showed that hotspots and lobes often contribute as expected, while background dependence and unusual source structure expose cases requiring data cleaning, label review, or retraining. The Set Transformer is reported as implemented work; no unverified performance improvement over the CNN is claimed.

## Outputs

- *Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI* — ApJS, under revision
- [IEEE URSI GASS 2023 conference proceeding](https://www.ursi.org/proceedings/procGA23/papers/YSASummaryHongmingTang.pdf)
- [Related invited talk](/talks/2023-11-ml-astronomy)
