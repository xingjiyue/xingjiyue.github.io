---
layout: academic
title: "CV"
permalink: /cv/
author_profile: false
page_class: "cv-page"
redirect_from:
  - /resume
---

<a class="cv-download" href="/files/cv_1.pdf">Download CV (PDF)</a>

<p class="cv-contact"><strong>Email</strong> <a href="mailto:yshiyu@link.cuhk.edu.hk">yshiyu@link.cuhk.edu.hk</a><br><strong>Phone</strong> <a href="tel:+85244346668">+852 4434 6668</a></p>

## Education

{% include academic/education-row.html degree="MPhil in Physics" institution="The Chinese University of Hong Kong" dates="Aug 2024–Oct 2026 (expected)" note="Postgraduate Studentship" %}
{% include academic/education-row.html degree="BSc in Physics" institution="Sun Yat-sen University" dates="Sep 2020–Jul 2024" note="GPA 3.9/4.0 (Top 5%) · Outstanding Graduate · Outstanding Graduation Thesis" %}

## Research and technical experience

**The [S III] Discrepancy in Star-Forming Galaxies**, The Chinese University of Hong Kong, Aug 2024–Oct 2026 (expected)
: Built a Python and Cloudy workflow for MaNGA integral-field spectroscopy, large model grids, 3D line-ratio diagnostics, and per-spaxel Bayesian inference. The tested abundance shifts do not reconcile the diagnostics jointly; ionising-SED shape and model physics remain leading directions. Related work was submitted to *Astronomy & Astrophysics* in Aug 2026.

**Fast Statistical Algorithms for Cosmology**, Sun Yat-sen University, Oct 2021–Oct 2024
: Developed an O(N log N) correlation-function workflow in C++ and OpenMP, validated it against theory and simulations with more than 10⁸ particles, and completed MDPL2-scale measurements in under eight hours. First-author paper published in *MNRAS*.

**Interpretable Radio Galaxy Classification with FR-DEEP**, Sun Yat-sen University / Tsinghua University, Jul 2021–Oct 2024
: Curated and quality-tagged 650 images; trained a CNN with 91.4% mean test accuracy across source-level folds; developed a LIME-based interpretation and failure-analysis workflow; and implemented a masked Set Transformer for variable-length source-component data.

**Multi-source Identification of Planetary Nebula Central Stars**, The University of Hong Kong Space Laboratory, Sep 2023–Dec 2023
: Integrated four heterogeneous survey sources, applied coordinate-based matching and Gaia validation, and explored a multimodal extension combining imaging and tabular features.

**AI Workflow Automation and Decision Support**, Personal engineering project, Mar 2026–May 2026
: Built an n8n and Dify workflow for structured ingestion, retrieval-augmented generation, schema-validated outputs, conditional routing, retries, logging, state tracking, email notifications, and human-review checkpoints.

## Teaching and leadership

**Teaching Assistant**, The Chinese University of Hong Kong, Sep 2024–Present
: Supported course administration, maintained assignment and grade records, answered student questions in English and Chinese, and explained quantitative concepts.

**New Media Center Lead**, Sun Yat-sen University, Sep 2021–Sep 2022
: Led content planning and production for the School's official WeChat account and coordinated review and publication schedules across faculty, administrative staff, and student teams.

## Skills and languages

**Programming and scientific computing:** Python, C++, OpenMP, Linux, Git, GitHub\\
**Data and machine learning:** PyTorch, Pandas, NumPy, SciPy, Xarray, Scikit-learn, Matplotlib, CNNs, Set Transformers, LIME\\
**Modelling and inference:** Bayesian inference, statistical modelling, KDE, RBF interpolation, model validation, correlation functions\\
**Workflow automation:** n8n, Dify, RAG, structured outputs, conditional routing, retry/error logging\\
**Languages:** Cantonese and Mandarin (native); English (fluent, IELTS 7.5)

## Awards

- Postgraduate Studentship, The Chinese University of Hong Kong, 2024–2026
- Outstanding Graduate and Outstanding Graduation Thesis, Sun Yat-sen University, 2024
- First Award Scholarship, Sun Yat-sen University, three consecutive years, 2021–2023
- China Aerospace Foundation–Uniasia Aerospace Scholarship, 2021
- Outstanding Camper, Nanjing University Summer Camp of Astronomy
- Best Speaker Award, Laboratory for Space Research, The University of Hong Kong

## Publications

{% include base_path %}
<ul>{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

## Talks

<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}</ul>
