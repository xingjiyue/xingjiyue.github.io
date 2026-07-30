---
title: "A model local interpretation routine for deep learning based radio galaxy classification"
collection: publications
category: conferences
permalink: /publication/2023-local-interpretation-radio-galaxy
excerpt: 'Conference proceeding introducing a LIME-based interpretation framework for radio galaxy morphology classifiers, presented at IEEE URSI GASS 2023.'
date: 2023-08-01
venue: 'IEEE URSI GASS 2023'
publication_status: published
paperurl: 'https://www.ursi.org/proceedings/procGA23/papers/YSASummaryHongmingTang.pdf'
citation: 'Tang, H., Yue, S. et al. (2023). "A model local interpretation routine for deep learning based radio galaxy classification." <i>IEEE URSI GASS 2023</i>.'
---
This conference proceeding introduces a model-interpretation routine designed to audit deep learning classifiers for radio galaxy morphology. The method uses LIME to generate local explanations and provides visual diagnostics for model attention.

## Key contributions

- Developed a reusable LIME-based interpretation routine for radio galaxy CNN classifiers
- Generated superpixel-segmented saliency maps to visualise which image regions drive classification decisions
- Demonstrated that the routine can detect cases where the classifier relies on background features rather than source morphology
