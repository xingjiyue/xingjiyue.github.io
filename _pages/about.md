---
layout: academic
permalink: /
title: "Shiyu Yue"
hide_title: true
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="profile-hero">
  <div class="profile-hero__copy">
    <p class="profile-hero__eyebrow">Physics MPhil candidate · The Chinese University of Hong Kong</p>
    <h1 class="profile-hero__name">Shiyu Yue</h1>
    <p class="profile-hero__intro">I develop scalable statistical algorithms, interpretable machine-learning methods, and Bayesian model–data pipelines for astronomical data.</p>
    <div class="profile-hero__education" aria-label="Education">
      {% include academic/education-row.html degree="MPhil in Physics" institution="The Chinese University of Hong Kong" dates="Aug 2024–Oct 2026 (expected)" note="Postgraduate Studentship" %}
      {% include academic/education-row.html degree="BSc in Physics" institution="Sun Yat-sen University" dates="Sep 2020–Jul 2024" note="GPA 3.9/4.0 (Top 5%) · Outstanding Graduate · Outstanding Graduation Thesis" %}
    </div>
    <nav class="profile-hero__links" aria-label="Profile links">
      <a href="mailto:yshiyu@link.cuhk.edu.hk">Email</a>
      <a href="/files/cv_1.pdf">CV</a>
      <a href="https://github.com/xingjiyue">GitHub</a>
      <a href="https://www.linkedin.com/in/shiyu-yue-314b3238b">LinkedIn</a>
    </nav>
  </div>
  <img class="profile-hero__portrait" src="/images/photo.jpg" alt="Portrait of Shiyu Yue" width="184" height="224">
</section>

<div class="section-heading">
  <h2>Selected work</h2>
  <a href="/publications/">All publications</a>
</div>

{% assign pair_counting = site.publications | where: "permalink", "/publication/2024-pair-counting-without-binning" | first %}
{% include academic/paper-row.html item=pair_counting %}

{% assign frdeep = site.publications | where: "permalink", "/publication/2025-can-i-trust-you" | first %}
{% include academic/paper-row.html item=frdeep %}

{% assign siii = site.publications | where: "permalink", "/publication/2026-siii-discrepancy-aa" | first %}
{% include academic/paper-row.html item=siii %}

<div class="section-heading">
  <h2>Recent news</h2>
</div>

{% include academic/news-row.html date="Aug 2026" text="[S III] discrepancy manuscript submitted to Astronomy & Astrophysics." url="/portfolio/2024-08-01-cloudy-manga/" %}
{% include academic/news-row.html date="May 2026" text="Presented the [S III] discrepancy work at the Guo Shoujing Telescope Workshop." url="/talks/2026-05-guoshoujing" %}
{% include academic/news-row.html date="Feb 2025" text="“Can I trust you?” manuscript under revision at ApJS." url="/publication/2025-can-i-trust-you" %}
{% include academic/news-row.html date="Dec 2024" text="“Pair counting without binning” published in MNRAS 535(4)." url="https://doi.org/10.1093/mnras/stae2513" %}
