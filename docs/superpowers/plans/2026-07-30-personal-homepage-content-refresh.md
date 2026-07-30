# Personal Homepage Content Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refresh Shiyu Yue's Academic Pages website with accurate, evidence-backed personal, research, publication, and technical-project content while preserving its academic-first identity.

**Architecture:** Keep the existing Jekyll/Academic Pages structure. Shared identity stays in `_config.yml`; overview copy stays in `_pages`; detailed evidence stays in `_portfolio`; bibliographic status and external links stay in `_publications`. Existing Liquid archive templates will receive only the minimal status/link wording needed to render `published`, `submitted`, and `under revision` conventionally.

**Tech Stack:** Jekyll, GitHub Pages, Liquid, Markdown, YAML front matter, JSON, Ruby/Bundler

## Global Constraints

- Approved design: `docs/superpowers/specs/2026-07-30-personal-homepage-content-refresh-design.md`
- Public name: `Shiyu Yue`
- Public email: `yshiyu@link.cuhk.edu.hk`
- Public phone: `+852 4434 6668`, visible only on Contact and CV
- MPhil dates: `Aug 2024 – Oct 2026 (expected)`
- FR-DEEP institution and dates: `Sun Yat-sen University / Tsinghua University`, `Jul 2021 – Oct 2024`
- CSPN dates: `Sep 2023 – Dec 2023`; retain the multimodal extension but write entirely in the past tense
- Homepage remains academic-first; AI workflow automation is a Portfolio and CV item, not a homepage Research Highlight
- A&A [S III] work: `submitted`, Aug 2026
- ApJS manuscript: `under revision`
- MNRAS and IEEE URSI GASS outputs: `published` with canonical external paper links
- Do not add SQL, Docker, SLURM, Power BI, Tableau, cloud-platform, production-deployment, or commercial-impact claims
- Keep the current theme, navigation, typography, sidebar structure, and responsive layout
- Use existing Academic Pages front-matter and archive patterns before changing Liquid or CSS
- Use British English consistently in narrative copy
- Do not publish a residential address
- Do not replace or deploy the downloadable PDF in this plan
- Run every shell command through `rtk` as required by `AGENTS.md`

---

## File Structure

### Shared identity

- `_config.yml` — canonical public name, summary, email, employer, location, GitHub, and LinkedIn
- `_pages/contact.md` — public contact details, including the approved phone number

### Overview pages

- `_pages/about.md` — homepage introduction, news, interests, research highlights, and calls to action
- `_pages/cv.md` — compact chronological CV and generated publication/talk lists

### Publication data and rendering

- `_publications/2023-08-01-local-interpretation-radio-galaxy.md`
- `_publications/2024-12-01-pair-counting-without-binning.md`
- `_publications/2025-02-01-can-i-trust-you.md`
- `_publications/2026-08-01-siii-discrepancy-aa.md` — new submitted-manuscript entry
- `_includes/archive-single.html` — publication status and paper link on the Publications index
- `_includes/archive-single-cv.html` — canonical paper link on the CV publication list

### Project evidence

- `_portfolio/2024-08-01-cloudy-manga.md`
- `_portfolio/2024-10-01-3pcf-fast-algorithm.md`
- `_portfolio/2024-12-01-frdeep-xai.md`
- `_portfolio/2025-03-01-cspn-multimodal.md`
- `_portfolio/2026-05-01-ai-workflow-automation.md` — new personal engineering project

### Legacy data cleanup

- `_data/cv.json` — remove Academic Pages demo-person data and leave a truthful, minimal legacy record

---

### Task 1: Canonical identity and public contact details

**Files:**

- Modify: `_config.yml:8-85`
- Modify: `_pages/contact.md:1-18`

**Interfaces:**

- Consumes: confirmed identity, contact, education, and privacy decisions from the approved design
- Produces: canonical sidebar metadata and Contact-page details consumed by all later content checks

- [ ] **Step 1: Run the identity regression search and record the failing baseline**

Run:

```bash
rtk rg -n 'ShiyuYUE|shiyu\.yue@link\.cuhk\.edu\.hk|linkedin\s*: *$' _config.yml _pages/contact.md
```

Expected: matches for `ShiyuYUE`, the old email in both files, and an empty LinkedIn field.

- [ ] **Step 2: Update the canonical fields in `_config.yml`**

Use `apply_patch` to make the relevant configuration block read:

```yaml
locale                   : "en-US"
site_theme               : "default"
title                    : "Shiyu Yue"
title_separator          : "-"
name                     : &name "Shiyu Yue"
description              : &description "Physics MPhil candidate at CUHK working on cosmological statistics, interpretable machine learning, and Bayesian model–data analysis"
url                      : https://xingjiyue.github.io
baseurl                  : ""
repository               : "xingjiyue/xingjiyue.github.io"

author:
  avatar           : "photo.jpg"
  name             : "Shiyu Yue"
  pronouns         :
  bio              : "Physics MPhil candidate at CUHK. Cosmological statistics, interpretable machine learning, and Bayesian model–data analysis."
  location         : "Hong Kong SAR"
  employer         : "The Chinese University of Hong Kong"
  uri              :
  email            : "yshiyu@link.cuhk.edu.hk"
```

Keep all unlisted Academic Pages settings unchanged. In the existing social
fields, set:

```yaml
  github           : "xingjiyue"
  linkedin         : "shiyu-yue-314b3238b"
```

Do not add the phone number to `_config.yml`, because that would expose it in
the homepage sidebar.

- [ ] **Step 3: Replace the Contact page body**

Keep the existing YAML front matter and replace the body with:

```markdown
**Email** — [yshiyu@link.cuhk.edu.hk](mailto:yshiyu@link.cuhk.edu.hk)

**Phone** — [+852 4434 6668](tel:+85244346668)

**GitHub** — [github.com/xingjiyue](https://github.com/xingjiyue)

**LinkedIn** — [linkedin.com/in/shiyu-yue](https://www.linkedin.com/in/shiyu-yue-314b3238b)

**Location** — Hong Kong SAR

---

I am an MPhil candidate in Physics at [The Chinese University of Hong Kong](https://www.phy.cuhk.edu.hk/), with expected completion in October 2026. I welcome enquiries about research collaboration, PhD opportunities, and research or data-intensive technical roles.
```

- [ ] **Step 4: Run identity and privacy checks**

Run:

```bash
rtk rg -n 'ShiyuYUE|shiyu\.yue@link\.cuhk\.edu\.hk' _config.yml _pages/contact.md
rtk rg -nF '+852 4434 6668' _config.yml _pages/contact.md
rtk rg -n 'name +:|email +:|linkedin +:' _config.yml
```

Expected:

- first command: no matches, exit code 1
- second command: exactly one match in `_pages/contact.md` and none in `_config.yml`
- third command: `Shiyu Yue`, `yshiyu@link.cuhk.edu.hk`, and `shiyu-yue-314b3238b`

- [ ] **Step 5: Commit the identity update**

```bash
rtk git add _config.yml _pages/contact.md
rtk git diff --cached --check
rtk git commit -m "fix: unify public identity and contact details"
```

Expected: one commit affecting only `_config.yml` and `_pages/contact.md`.

---

### Task 2: Rewrite the academic-first homepage

**Files:**

- Modify: `_pages/about.md:1-38`

**Interfaces:**

- Consumes: canonical identity from Task 1 and approved publication/project facts
- Produces: homepage narrative and links to the CV, Publications, and Cloudy/MaNGA Portfolio page

- [ ] **Step 1: Run the homepage regression search**

Run:

```bash
rtk rg -n 'Jun 2026|======|ongoing multimodal|MPhil student' _pages/about.md
```

Expected: matches for `Jun 2026`, `======`, and `MPhil student`.

- [ ] **Step 2: Replace `_pages/about.md` with the approved homepage copy**

Use this complete content:

```markdown
---
permalink: /
title: "Shiyu Yue"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am an MPhil candidate in Physics at [The Chinese University of Hong Kong](https://www.phy.cuhk.edu.hk/), with expected completion in October 2026. My research spans cosmological statistics, interpretable machine learning, and Bayesian model–data analysis.

I develop computational methods that connect physical questions with reliable evidence: deriving statistical approaches, implementing scalable research software, and validating results against simulations and observations.

## Recent news

- **Aug 2026** — Work on the [S III] discrepancy submitted to *Astronomy & Astrophysics*. [Project overview](/portfolio/2024-08-01-cloudy-manga/)
- **Feb 2025** — *"Can I Trust You?"* under revision at *The Astrophysical Journal Supplement Series*.
- **Dec 2024** — *"Pair Counting Without Binning"* published in *Monthly Notices of the Royal Astronomical Society*, 535(4).
- **Aug 2024** — Began an MPhil in Physics at CUHK with a Postgraduate Studentship.

## Research interests

Large-scale structure statistics · Two- and three-point correlation functions · Bayesian inference · Interpretable deep learning · Radio-galaxy morphology · Integral-field spectroscopy · Photoionisation modelling · Cosmological simulations · Multi-source astronomical data

## Research highlights

- **Fast 3PCF algorithm:** Developed an O(N log N) three-point correlation-function workflow in C++ and OpenMP, validated on simulations with more than 10<sup>8</sup> particles and measured at MDPL2 scale in under eight hours.
- **Interpretable radio-galaxy ML:** Built a CNN and LIME-based audit workflow for 650 FR-DEEP images, achieving 91.4% mean test accuracy across source-level folds, and extended the work with a masked Set Transformer for variable-length source-component data.
- **Cloudy and MaNGA inference:** Built a Python workflow for large photoionisation-model grids, 3D line-ratio diagnostics, and per-spaxel Bayesian inference; revised models approximately halved the [S III] discrepancy.
- **CSPN candidate selection:** Integrated four heterogeneous survey sources, applied coordinate-based matching and Gaia validation, and explored a multimodal extension combining imaging and tabular features.

[View CV (PDF)](/files/cv_1.pdf){: .btn .btn--primary} [Publications](/publications/){: .btn}
```

- [ ] **Step 3: Verify the homepage content boundaries**

Run:

```bash
rtk rg -n 'Jun 2026|======|ongoing|production|stakeholder|business' _pages/about.md
rtk rg -n 'Aug 2026|Oct 2026|91\.4%|Set Transformer|10<sup>8</sup>|approximately halved' _pages/about.md
```

Expected:

- first command: no matches, exit code 1
- second command: one or more matches for every approved homepage fact

- [ ] **Step 4: Build the site after the homepage change**

Run:

```bash
rtk bundle exec jekyll build --trace
```

Expected: exit code 0 and generated `_site/index.html`.

- [ ] **Step 5: Commit the homepage update**

```bash
rtk git add _pages/about.md
rtk git diff --cached --check
rtk git commit -m "feat: refresh academic homepage narrative"
```

Expected: one commit affecting only `_pages/about.md`.

---

### Task 3: Add conventional publication status and paper links

**Files:**

- Modify: `_includes/archive-single.html:35-99`
- Modify: `_includes/archive-single-cv.html:25-44`
- Modify: `_publications/2023-08-01-local-interpretation-radio-galaxy.md:1-17`
- Modify: `_publications/2024-12-01-pair-counting-without-binning.md:1-19`
- Modify: `_publications/2025-02-01-can-i-trust-you.md:1-18`
- Create: `_publications/2026-08-01-siii-discrepancy-aa.md`

**Interfaces:**

- Consumes: `publication_status`, `venue`, `date`, `paperurl`, and `citation` front-matter fields
- Produces: conventional index wording and canonical links for the Publications and CV archive lists

- [ ] **Step 1: Demonstrate the current status-rendering failure**

Run:

```bash
rtk rg -n "Published in" _includes/archive-single.html
rtk rg -n 'publication_status|paperurl' _publications
```

Expected:

- the include has one unconditional `Published in` branch for all publications
- existing publication files have no `publication_status` or `paperurl`

- [ ] **Step 2: Add status-aware Liquid rendering**

In `_includes/archive-single.html`, replace the existing publications branch:

```liquid
{% elsif post.collection == 'publications' %}
  <p>Published in <i>{{ post.venue }}</i>, {{ post.date | default: "1900-01-01" | date: "%Y" }} </p>
```

with:

```liquid
{% elsif post.collection == 'publications' %}
  {% assign publication_year = post.date | default: "1900-01-01" | date: "%Y" %}
  {% if post.publication_status == "submitted" %}
    <p>Submitted to <i>{{ post.venue }}</i>, {{ publication_year }}</p>
  {% elsif post.publication_status == "under_revision" %}
    <p>Under revision at <i>{{ post.venue }}</i>, {{ publication_year }}</p>
  {% else %}
    <p>Published in <i>{{ post.venue }}</i>, {{ publication_year }}</p>
  {% endif %}
```

In the same file, change every visible `Download Paper` label to `View Paper`.
Do not change the `post.paperurl` field name or the slides/BibTeX branches.

- [ ] **Step 3: Add paper links to the compact CV publication include**

In `_includes/archive-single-cv.html`, replace:

```liquid
{% if post.venue%}<p class="archive__item-excerpt" itemprop="description">{{ post.citation }}</p> {% endif %}
```

with:

```liquid
{% if post.venue %}
  <p class="archive__item-excerpt" itemprop="description">
    {{ post.citation }}
    {% if post.paperurl %}<br /><a href="{{ post.paperurl }}">View paper</a>{% endif %}
  </p>
{% endif %}
```

- [ ] **Step 4: Add exact status/link fields to the three existing publications**

Add these fields to
`_publications/2023-08-01-local-interpretation-radio-galaxy.md`:

```yaml
publication_status: published
paperurl: 'https://www.ursi.org/proceedings/procGA23/papers/YSASummaryHongmingTang.pdf'
```

Add these fields to
`_publications/2024-12-01-pair-counting-without-binning.md`:

```yaml
publication_status: published
paperurl: 'https://doi.org/10.1093/mnras/stae2513'
```

Add this field to `_publications/2025-02-01-can-i-trust-you.md`:

```yaml
venue: 'The Astrophysical Journal Supplement Series'
publication_status: under_revision
```

Keep the ApJS entry without `paperurl` unless a public preprint URL is separately
verified.

- [ ] **Step 5: Create the A&A submitted-manuscript entry**

Create `_publications/2026-08-01-siii-discrepancy-aa.md` with:

```markdown
---
title: "A&A submission on the [S III] discrepancy"
collection: publications
category: manuscripts
permalink: /publication/2026-siii-discrepancy-aa
excerpt: 'Cloudy and MaNGA analysis of the persistent [S III] discrepancy using 3D line-ratio diagnostics and Bayesian model–data comparison.'
date: 2026-08-01
venue: 'Astronomy & Astrophysics'
publication_status: submitted
citation: 'Yue, S. et al. (2026). Manuscript on the [S III] discrepancy in photoionisation models. Submitted to <i>Astronomy & Astrophysics</i>.'
---

This submitted work investigates the persistent mismatch between standard photoionisation models and observed [S III] emission in MaNGA integral-field spectroscopy.

## Approach

- Generated and validated large Cloudy model grids across metallicity, ionisation parameter, and abundance variations
- Compared models with observed spaxel distributions in reprojected 3D diagnostic spaces
- Used KDE, RBF interpolation, and per-spaxel Bayesian inference for quantitative model–data comparison

## Result

A revised model configuration approximately halved the [S III] discrepancy while preserving agreement in standard optical line-ratio diagnostics.

[View the related Cloudy and MaNGA project](/portfolio/2024-08-01-cloudy-manga/)
```

- [ ] **Step 6: Verify publication semantics and links**

Run:

```bash
rtk rg -n 'publication_status:|paperurl:' _publications
rtk rg -n 'Published in|Submitted to|Under revision at|View Paper|View paper' _includes/archive-single.html _includes/archive-single-cv.html
rtk curl -L --fail --silent --show-error --output /dev/null https://doi.org/10.1093/mnras/stae2513
rtk curl -L --fail --silent --show-error --output /dev/null https://www.ursi.org/proceedings/procGA23/papers/YSASummaryHongmingTang.pdf
rtk bundle exec jekyll build --trace
```

Expected:

- four publication status fields
- two published-paper URLs
- all three status labels in the Liquid include
- both external-link checks exit 0
- Jekyll build exits 0

- [ ] **Step 7: Commit publication metadata and rendering**

```bash
rtk git add _includes/archive-single.html _includes/archive-single-cv.html _publications
rtk git diff --cached --check
rtk git commit -m "feat: add publication status and paper links"
```

Expected: one commit containing the two include changes, three metadata edits,
and one new publication entry.

---

### Task 4: Refresh research projects and add AI workflow automation

**Files:**

- Modify: `_portfolio/2024-08-01-cloudy-manga.md`
- Modify: `_portfolio/2024-10-01-3pcf-fast-algorithm.md`
- Modify: `_portfolio/2024-12-01-frdeep-xai.md`
- Modify: `_portfolio/2025-03-01-cspn-multimodal.md`
- Create: `_portfolio/2026-05-01-ai-workflow-automation.md`

**Interfaces:**

- Consumes: project facts and conservative-claim policy from the approved design
- Produces: five conventional Academic Pages Portfolio entries linked from the Portfolio index, homepage, CV, and A&A publication entry

- [ ] **Step 1: Record the stale project baseline**

Run:

```bash
rtk rg -n 'ongoing|Present|currently|XJTLU|Dec 2024|Set Transformer|A&A|n8n|Dify' _portfolio
```

Expected: CSPN contains ongoing/present-tense wording; FR-DEEP lacks the Set
Transformer; Cloudy lacks A&A status; no automation Portfolio file exists.

- [ ] **Step 2: Update the Cloudy/MaNGA project**

In `_portfolio/2024-08-01-cloudy-manga.md`, keep the existing technical
explanation and make these exact additions:

Add to front matter:

```yaml
permalink: /portfolio/2024-08-01-cloudy-manga/
date: 2024-08-01
```

Replace the excerpt with:

```yaml
excerpt: "Built a Python and Cloudy workflow for MaNGA spectroscopy, 3D line-ratio diagnostics, and Bayesian model–data comparison; work on the [S III] discrepancy was submitted to A&A in August 2026."
```

Add this section immediately before the Skills line:

```markdown
**Research output.** Work on the [S III] discrepancy was submitted to *Astronomy & Astrophysics* in August 2026. The manuscript status is reported as submitted, not accepted or published.
```

- [ ] **Step 3: Keep the 3PCF project academically precise**

In `_portfolio/2024-10-01-3pcf-fast-algorithm.md`, add:

```yaml
permalink: /portfolio/2024-10-01-3pcf-fast-algorithm/
date: 2024-10-01
```

Replace the existing Related publication paragraph with:

```markdown
**Related publication:** [Pair counting without binning – a new approach to correlation functions in clustering statistics](https://doi.org/10.1093/mnras/stae2513) (*MNRAS*, 2024, first author).
```

Keep the GPU benchmark project-specific. Do not add `GPU engineering`,
`distributed systems`, `SLURM`, or cloud-infrastructure language.

- [ ] **Step 4: Replace the FR-DEEP project with the confirmed institution, dates, and Transformer extension**

Use this complete content for `_portfolio/2024-12-01-frdeep-xai.md`:

```markdown
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
```

- [ ] **Step 5: Replace the CSPN project with past-tense, bounded work**

Use this complete content for `_portfolio/2025-03-01-cspn-multimodal.md`:

```markdown
---
title: "Multi-source Identification of Planetary Nebula Central Stars"
excerpt: "Integrated four heterogeneous survey sources, applied coordinate-based matching and Gaia validation, and explored a multimodal extension for CSPN candidate selection."
collection: portfolio
permalink: /portfolio/2025-03-01-cspn-multimodal/
date: 2025-03-01
---

**The University of Hong Kong Space Laboratory · Sep 2023 – Dec 2023**

Central stars of planetary nebulae are often faint, embedded in bright nebulosity, and difficult to distinguish from unrelated field stars. This project developed a reproducible candidate-selection workflow based on cross-source reconciliation and explicit quality control.

**Catalogue integration.** I reconciled four heterogeneous imaging and catalogue sources, standardised their fields, and matched candidates using sky coordinates. Duplicate-control and traceability rules preserved the relationship between each candidate and its source records.

**Quality control and validation.** I compared positional offsets, object overlap, photometry, and foreground/background contamination. Gaia astrometry supplied an external consistency check for candidate distances and motions.

**Multimodal extension.** During the project, I explored a multimodal design combining image features with tabular photometric and astrometric parameters for candidate screening. This was a research extension completed within the Sep–Dec 2023 project period, not an ongoing production system.

**Skills:** catalogue cross-matching, coordinate reconciliation, schema standardisation, data-quality control, Gaia DR3, multimodal model design.
```

- [ ] **Step 6: Create the AI workflow automation Portfolio entry**

Create `_portfolio/2026-05-01-ai-workflow-automation.md` with:

```markdown
---
title: "AI Workflow Automation and Decision Support"
excerpt: "Built a personal n8n and Dify workflow for structured ingestion, evidence retrieval, schema-validated outputs, conditional routing, and human review."
collection: portfolio
permalink: /portfolio/2026-05-01-ai-workflow-automation/
date: 2026-05-01
---

**Personal engineering project · Mar 2026 – May 2026**

This project explored how a multi-stage AI workflow could turn unstructured web and API inputs into traceable, reviewable summaries without treating model output as an autonomous final decision.

**Workflow design.** I used n8n and Dify to coordinate ingestion, normalisation, deduplication, retrieval-augmented generation, and LLM-assisted assessment. Explicit structured-output contracts passed state between stages and made downstream routing predictable.

**Reliability and review.** The workflow included schema validation, conditional routing, retries, error logging, state tracking, email notifications, and human-review checkpoints. Intermediate evidence and decisions were retained so that failures could be isolated and outputs could be checked before action.

**Scope.** This was a personal engineering project rather than a production or commercial deployment. Its value lies in modular workflow design, traceability, and controlled use of language models.

**Skills:** n8n, Dify, RAG, structured outputs, workflow orchestration, validation, retry handling, logging, human-in-the-loop review.
```

- [ ] **Step 7: Verify dates, tense, boundaries, and Portfolio count**

Run:

```bash
rtk rg -n 'XJTLU|Jul 2026|ongoing|currently building|production platform|commercial deployment' _portfolio
rtk rg -n 'Jul 2021 – Oct 2024|masked Set Transformer|Sep 2023 – Dec 2023|submitted to.*Astronomy & Astrophysics|n8n|Dify' _portfolio
rtk find _portfolio -maxdepth 1 -name '*.md' | rtk wc -l
rtk bundle exec jekyll build --trace
```

Expected:

- first command: no unsupported or stale phrasing; the automation page may use
  the exact negating sentence `rather than a production or commercial
  deployment`, which must be manually confirmed as a limitation, not a claim
- second command: all confirmed project facts present
- third command: `5`
- Jekyll build exits 0

- [ ] **Step 8: Commit the Portfolio refresh**

```bash
rtk git add _portfolio
rtk git diff --cached --check
rtk git commit -m "feat: refresh research and engineering projects"
```

Expected: one commit with four edited Portfolio files and one new file.

---

### Task 5: Update the public CV and remove demo JSON data

**Files:**

- Modify: `_pages/cv.md:1-70`
- Modify: `_data/cv.json:1-end`

**Interfaces:**

- Consumes: canonical identity from Task 1, publication collection from Task 3, and Portfolio facts from Task 4
- Produces: public `/cv/` page plus a truthful minimal legacy JSON record

- [ ] **Step 1: Run the CV consistency baseline**

Run:

```bash
rtk rg -n 'XJTLU|Sep 2025|Present|Oct 2026|Teaching Assistant|IELTS|4434 6668|AI Workflow|Set Transformer' _pages/cv.md
rtk rg -n 'Your Sidebar Name|GitHub University|Paper Title Number|none@example\.org' _data/cv.json
```

Expected: stale CV facts and multiple Academic Pages demo-data matches.

- [ ] **Step 2: Replace `_pages/cv.md` with the approved public CV**

Use this complete content:

```markdown
---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

[Download CV (PDF)](/files/cv_1.pdf){: .btn .btn--primary}

**Email:** [yshiyu@link.cuhk.edu.hk](mailto:yshiyu@link.cuhk.edu.hk)  
**Phone:** [+852 4434 6668](tel:+85244346668)

## Education

**MPhil in Physics**, The Chinese University of Hong Kong, Aug 2024–Oct 2026 (expected)  
Postgraduate Studentship

**BSc in Physics**, Sun Yat-sen University, Sep 2020–Jul 2024  
GPA 3.9 / 4.0 (Top 5%); Outstanding Graduate; Outstanding Graduation Thesis

## Research and technical experience

**Photoionisation Model Inference with Cloudy and MaNGA**, The Chinese University of Hong Kong, Aug 2024–Present
: Built a Python and Cloudy workflow for MaNGA integral-field spectroscopy, large model grids, 3D line-ratio diagnostics, and per-spaxel Bayesian inference. Revised model configurations approximately halved the [S III] discrepancy. Related work was submitted to *Astronomy & Astrophysics* in Aug 2026.

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

**Programming and scientific computing:** Python, C++, OpenMP, Linux, Git, GitHub  
**Data and machine learning:** PyTorch, Pandas, NumPy, SciPy, Xarray, Scikit-learn, Matplotlib, CNNs, Set Transformers, LIME  
**Modelling and inference:** Bayesian inference, statistical modelling, KDE, RBF interpolation, model validation, correlation functions  
**Workflow automation:** n8n, Dify, RAG, structured outputs, conditional routing, retry/error logging  
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
```

- [ ] **Step 3: Replace demo JSON with a minimal truthful legacy record**

Replace `_data/cv.json` with:

```json
{
  "_comment": "Legacy JSON CV data. The public /cv/ page renders _pages/cv.md.",
  "basics": {
    "name": "Shiyu Yue",
    "email": "yshiyu@link.cuhk.edu.hk",
    "phone": "+852 4434 6668",
    "website": "https://xingjiyue.github.io",
    "summary": "Physics MPhil candidate at The Chinese University of Hong Kong working on cosmological statistics, interpretable machine learning, and Bayesian model-data analysis.",
    "location": {
      "address": "",
      "postalCode": "",
      "city": "Hong Kong",
      "countryCode": "HK",
      "region": "Hong Kong SAR"
    },
    "profiles": [
      {
        "network": "GitHub",
        "username": "xingjiyue",
        "url": "https://github.com/xingjiyue"
      },
      {
        "network": "LinkedIn",
        "username": "shiyu-yue-314b3238b",
        "url": "https://www.linkedin.com/in/shiyu-yue-314b3238b"
      }
    ]
  },
  "work": [],
  "education": [
    {
      "institution": "The Chinese University of Hong Kong",
      "area": "MPhil in Physics",
      "studyType": "MPhil",
      "startDate": "2024-08",
      "endDate": "2026-10",
      "gpa": null,
      "courses": []
    },
    {
      "institution": "Sun Yat-sen University",
      "area": "BSc in Physics",
      "studyType": "BSc",
      "startDate": "2020-09",
      "endDate": "2024-07",
      "gpa": "3.9/4.0",
      "courses": []
    }
  ],
  "skills": [],
  "languages": [
    {
      "language": "Cantonese",
      "fluency": "Native"
    },
    {
      "language": "Mandarin",
      "fluency": "Native"
    },
    {
      "language": "English",
      "fluency": "Fluent; IELTS 7.5"
    }
  ],
  "interests": [],
  "references": [],
  "publications": [],
  "presentations": [],
  "teaching": [],
  "portfolio": []
}
```

Do not modify `scripts/cv_markdown_to_json.py`; rebuilding that legacy converter
is outside this plan.

- [ ] **Step 4: Validate CV facts, privacy boundaries, and JSON syntax**

Run:

```bash
rtk rg -n 'XJTLU|Jul 2026|Sep 2025|ongoing|Your Sidebar Name|GitHub University|Paper Title Number' _pages/cv.md _data/cv.json
rtk rg -n 'Oct 2026|Sun Yat-sen University / Tsinghua University|Jul 2021–Oct 2024|Sep 2023–Dec 2023|IELTS 7\.5|AI Workflow|Set Transformer' _pages/cv.md
rtk python3 -m json.tool _data/cv.json
rtk rg -lF '+852 4434 6668' _config.yml _pages/about.md _pages/contact.md _pages/cv.md
rtk bundle exec jekyll build --trace
```

Expected:

- first command: no stale or demo-data matches, exit code 1
- second command: all confirmed CV facts present
- JSON command: formatted JSON output and exit code 0
- phone search: `_pages/contact.md` and `_pages/cv.md` only
- Jekyll build: exit code 0

- [ ] **Step 5: Commit the CV and legacy-data cleanup**

```bash
rtk git add _pages/cv.md _data/cv.json
rtk git diff --cached --check
rtk git commit -m "feat: update public CV from verified profile"
```

Expected: one commit affecting only the public CV and legacy JSON record.

---

### Task 6: Full-site claim, link, build, and visual verification

**Files:**

- Verify: all files changed in Tasks 1–5
- Do not create or modify files unless verification reveals a defect covered by the approved design

**Interfaces:**

- Consumes: the complete content refresh
- Produces: evidence that the site builds, renders conventionally, links correctly, and contains no known stale facts

- [ ] **Step 1: Run the complete stale-content search**

Run:

```bash
rtk rg -n 'ShiyuYUE|shiyu\.yue@link\.cuhk\.edu\.hk|XJTLU|Jun 2026|Jul 2026|Sep 2025|Your Sidebar Name|GitHub University|Paper Title Number' _config.yml _pages _portfolio _publications _data/cv.json
```

Expected: no matches, exit code 1.

- [ ] **Step 2: Run the unsupported-claim search**

Run:

```bash
rtk rg -ni '\bSQL\b|\bDocker\b|\bSLURM\b|Power BI|Tableau|cloud platform|production deployment|commercial impact' _pages _portfolio _publications
```

Expected: no affirmative unsupported claims. A negating limitation on the AI
workflow page is acceptable only if it is clearly phrased as out of scope.

- [ ] **Step 3: Verify required facts and privacy boundaries**

Run:

```bash
rtk rg -n 'yshiyu@link\.cuhk\.edu\.hk|Oct 2026|Jul 2021.?Oct 2024|Sep 2023.?Dec 2023|91\.4%|Set Transformer|submitted|under revision|publication_status: published' _config.yml _pages _portfolio _publications
rtk rg -lF '+852 4434 6668' _config.yml _pages/about.md _pages/contact.md _pages/cv.md
rtk rg -ni 'Postgraduate Hall|residential address|Shatin N\.T\.' _config.yml _pages _portfolio _publications
```

Expected:

- required facts appear in their intended content files
- phone appears only in Contact and CV
- no residential-address match

- [ ] **Step 4: Validate data files and build from a clean output directory**

Run:

```bash
rtk python3 -m json.tool _data/cv.json
rtk bundle exec jekyll clean
rtk bundle exec jekyll build --trace
```

Expected: JSON exits 0; Jekyll clean and build exit 0; `_site/` is regenerated.

- [ ] **Step 5: Verify generated routes and rendered status labels**

Run:

```bash
rtk proxy test -f _site/index.html
rtk proxy test -f _site/cv/index.html
rtk proxy test -f _site/publications/index.html
rtk proxy test -f _site/portfolio/index.html
rtk proxy test -f _site/contact/index.html
rtk proxy test -f _site/publication/2026-siii-discrepancy-aa/index.html
rtk proxy test -f _site/files/cv_1.pdf
rtk rg -n 'Submitted to|Under revision at|Published in|View Paper' _site/publications/index.html
```

Expected: all route checks exit 0 and the Publications index contains the four
conventional status/link labels. The copied downloadable CV exists at
`_site/files/cv_1.pdf`.

- [ ] **Step 6: Start a local preview and inspect desktop and mobile layouts**

Run:

```bash
rtk bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Expected: Jekyll reports `Server address: http://127.0.0.1:4000/`.

Using the `browser:control-in-app-browser` skill, inspect these routes at approximately
1440×900 and 390×844:

```text
/
/cv/
/publications/
/portfolio/
/portfolio/2024-08-01-cloudy-manga/
/portfolio/2024-10-01-3pcf-fast-algorithm/
/portfolio/2024-12-01-frdeep-xai/
/portfolio/2025-03-01-cspn-multimodal/
/portfolio/2026-05-01-ai-workflow-automation/
/contact/
```

Confirm:

- no overflow, clipped headings, or broken archive cards
- sidebar remains conventional and does not expose the phone
- Contact and CV show the phone
- publication statuses are grammatically correct
- published paper links are visible
- new Portfolio pages use the same spacing and typography as existing pages
- mobile navigation and content remain usable

Stop the preview with `Ctrl-C` after inspection.

- [ ] **Step 7: Verify external paper links**

Run:

```bash
rtk curl -L --fail --silent --show-error --output /dev/null https://doi.org/10.1093/mnras/stae2513
rtk curl -L --fail --silent --show-error --output /dev/null https://www.ursi.org/proceedings/procGA23/papers/YSASummaryHongmingTang.pdf
```

Expected: both commands exit 0.

- [ ] **Step 8: Review the final repository state**

Run:

```bash
rtk git status --short
rtk git log -5 --oneline
rtk git diff HEAD~5..HEAD --check
```

Expected:

- no uncommitted source changes
- the five implementation commits appear after the design commits
- diff check exits 0

Do not push or deploy. Publishing remains outside this plan.
