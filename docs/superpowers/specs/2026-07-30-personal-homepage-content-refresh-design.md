# Personal Homepage Content Refresh Design

**Date:** 2026-07-30

**Status:** Approved in conversation; awaiting review of this written specification

## Goal

Refresh Shiyu Yue's Academic Pages website using the supplied CV sources and the
workspace evidence base. Correct inaccurate or stale information, add relevant
missing experience, and strengthen the English wording while keeping the site
primarily academic in identity.

## Positioning

The website will present Shiyu Yue first as a physics researcher and CUHK MPhil
candidate, then show the computational methods and broader technical abilities
that support the research.

The narrative order is:

1. Physics research identity
2. Computational and statistical methods
3. Verified research outcomes
4. Broader technical capability

The existing Academic Pages theme, navigation, and overall layout will remain.
This refresh is a content and factual-consistency project, not a visual redesign.

## Source and Claim Policy

Information will be prioritized in this order:

1. Facts explicitly confirmed by the user in this revision
2. Verified evidence and do-not-claim documents in `job_hunt_kb`
3. Recent general and role-specific CV sources in the supplied archive
4. Existing website content

Role-specific CVs may supply stronger verbs, clearer structure, and concise
technical explanations. Their job-specific positioning, unsupported metrics,
and commercial framing must not be copied automatically.

Publication states must remain exact:

- `published` only for published work
- `submitted` for the A&A manuscript
- `under revision` for the ApJS manuscript
- `in preparation` only when explicitly supported and needed

Conflicting metrics will be omitted or expressed conservatively unless the user
has confirmed the exact value. The site must not add SQL, Docker, SLURM, Power
BI, Tableau, cloud-platform, production-deployment, or commercial-impact claims
without stronger evidence.

## Confirmed Personal Facts

- Public name: `Shiyu Yue`
- Public email: `yshiyu@link.cuhk.edu.hk`
- Public phone: `+852 4434 6668`
- Phone visibility: Contact and CV pages only, not the homepage sidebar
- Current degree: MPhil in Physics, The Chinese University of Hong Kong
- Degree dates: `Aug 2024 – Oct 2026 (expected)`
- Location: Hong Kong SAR
- Languages: Cantonese and Mandarin (native); English (fluent, IELTS 7.5)
- FR-DEEP institutions: Sun Yat-sen University / Tsinghua University
- FR-DEEP dates: `Jul 2021 – Oct 2024`
- CSPN dates: `Sep 2023 – Dec 2023`
- CSPN multimodal extension remains part of the project but is described in the
  past tense, not as ongoing work
- The n8n / Dify / RAG project will be added as a separate Portfolio item

## Information Architecture

### Homepage

The homepage will contain:

1. A concise two-paragraph academic introduction
2. Recent News
3. Research Interests
4. Four Research Highlights
5. Calls to action for the CV and Publications pages

The four Research Highlights remain:

- Fast 3PCF algorithm
- Interpretable radio-galaxy ML
- Cloudy and MaNGA inference
- CSPN multi-source candidate selection

The AI workflow automation project will not become a fifth homepage Research
Highlight because it would weaken the academic-first hierarchy. It remains
discoverable through Portfolio and CV.

### Portfolio

Portfolio will contain five substantive project pages:

1. Fast O(N log N) 3PCF Algorithm for Cosmology
2. Interpretable Radio Galaxy Classification with FR-DEEP
3. Photoionisation Model Inference with Cloudy and MaNGA
4. Multimodal Identification of Planetary Nebula Central Stars
5. AI Workflow Automation and Decision Support

### CV

The public CV page will use this order:

1. Education
2. Research and Technical Experience
3. Teaching and Leadership
4. Skills and Languages
5. Awards
6. Publications
7. Talks

### Publications and Contact

The Publications page will include the three existing outputs and a new A&A
submitted manuscript entry connected to the Cloudy/MaNGA project.

The Contact page will show the confirmed email, phone, GitHub, LinkedIn,
location, and a short collaboration statement.

## Page Content Design

### Site Configuration and Sidebar

`_config.yml` will be updated so the public name appears consistently as
`Shiyu Yue`. The sidebar bio will identify Shiyu as a CUHK Physics MPhil
candidate and describe the main research areas without job-application wording.

The sidebar will include:

- `yshiyu@link.cuhk.edu.hk`
- GitHub username `xingjiyue`
- LinkedIn profile `shiyu-yue-314b3238b`
- Hong Kong SAR
- The Chinese University of Hong Kong

The phone number will not appear in the sidebar.

### Homepage Introduction

The introduction will connect cosmological statistics, interpretable machine
learning, and Bayesian model-data analysis. It will emphasize the full research
workflow: deriving methods, implementing scalable tools, and validating results
against simulations or observations.

The wording must remain understandable to both researchers and technically
literate non-specialists. Industry-style phrases such as "business drivers,"
"stakeholder trust," or "production platform" will not be used.

### Recent News

Recent News will contain only dated, supportable events. It will include:

- `Aug 2026` — Work on the [S III] discrepancy submitted to A&A
- `Feb 2025` — "Can I Trust You?" under revision at ApJS
- `Dec 2024` — "Pair Counting Without Binning" published in MNRAS 535(4)
- `Aug 2024` — Began the CUHK Physics MPhil with a Postgraduate Studentship

The current incorrect `Jun 2026` publication date for the MNRAS paper will be
removed. The A&A item will link to the Cloudy/MaNGA project page. No formal
manuscript title will be invented if one is not present in the source material.

### Research Highlights

#### Fast 3PCF Algorithm

The homepage may state:

- O(N log N) scaling
- C++ and OpenMP implementation
- validation on simulations with more than 10^8 particles
- sub-eight-hour MDPL2-scale measurement

CPU/GPU benchmark details remain project-specific and will not be generalized
into a broad GPU engineering claim.

#### FR-DEEP

The homepage and project page will cover:

- a CNN trained and evaluated with source-level five-fold validation
- approximately 91.4 percent mean test accuracy
- a 650-image data-quality review
- LIME-based interpretation and failure analysis
- a masked Set Transformer using multi-head self-attention and attention
  pooling to model variable-length source-component tokens

The Transformer extension will be described as work performed. The site will
not claim an unverified accuracy improvement over the CNN.

#### Cloudy and MaNGA

The homepage and project page will cover:

- a Python and Cloudy model-grid workflow
- MaNGA integral-field spectroscopy
- 3D line-ratio diagnostics
- KDE/RBF model-data comparison
- per-spaxel Bayesian inference
- a revised model that approximately halves the sulphur-line discrepancy
- submission of the [S III] discrepancy work to A&A in Aug 2026

Conflicting record-count and improvement-percentage variants will not be placed
on the homepage.

#### CSPN

The project will be dated `Sep 2023 – Dec 2023`. It will describe:

- integration of four heterogeneous imaging or catalogue sources
- coordinate-based matching and data-quality control
- Gaia-based validation
- exploration of a multimodal extension combining imaging and tabular features

All work will use the past tense. The words `ongoing`, `Present`, and
`currently building` will be removed for this project.

### AI Workflow Automation Project

A new Portfolio page will describe the Mar–May 2026 personal engineering
project. It may include:

- n8n and Dify workflow orchestration
- retrieval-augmented generation
- structured ingestion and normalization
- schema-validated outputs
- conditional routing
- retry and error logging
- state tracking
- email notifications
- human-review checkpoints

The page will frame the work as a personal engineering project. It must not be
presented as a production platform, commercial deployment, or evidence of
enterprise ownership.

### CV Page

The CV page will:

- use `Aug 2024 – Oct 2026 (expected)` for the CUHK MPhil
- use `Sun Yat-sen University / Tsinghua University` and
  `Jul 2021 – Oct 2024` for FR-DEEP
- use `Sep 2023 – Dec 2023` for CSPN
- add the AI workflow automation project
- add the masked Set Transformer extension
- add Teaching Assistant experience
- add student communication and leadership experience
- add Cantonese, Mandarin, and English with IELTS 7.5
- add the A&A submitted manuscript
- show `yshiyu@link.cuhk.edu.hk` and `+852 4434 6668`

The CV will not repeat the private residential address found in some source
files.

### JSON CV Data

The public `/cv/` route currently renders `_pages/cv.md`; it does not call
`_data/cv.json` or `_includes/cv-template.html`. The JSON file still contains
Academic Pages example data, and the current conversion script does not parse
the live Markdown structure reliably.

This refresh will not create a second public CV implementation. The placeholder
JSON data will either be replaced with a clearly minimal representation of the
confirmed profile or marked as unused without changing the public route.
Rebuilding the Markdown-to-JSON converter is a separate maintenance project and
is outside this content refresh.

## Data Flow

Public identity data flows from `_config.yml` into the sidebar and shared
metadata. Page-specific narrative content lives in Markdown:

```text
Confirmed CV facts and evidence
            |
            v
  _config.yml + Markdown collections
            |
            v
        Jekyll build
            |
            v
 Homepage / CV / Portfolio / Publications / Contact
```

Content should be written once at the appropriate level:

- shared identity in `_config.yml`
- overview wording on the homepage
- detailed evidence on Portfolio pages
- formal status and citation data in Publication entries
- compact chronological summaries on the CV page

## Consistency and Error Handling

When sources disagree:

1. Use facts confirmed in this specification.
2. Prefer conservative verified language.
3. Omit an exact number rather than select one arbitrarily.
4. Do not upgrade publication status.
5. Keep project-specific benchmarks within the relevant project page.

The revision must remove or replace public occurrences of:

- `ShiyuYUE`
- `shiyu.yue@link.cuhk.edu.hk`
- `XJTLU` as the FR-DEEP institution
- FR-DEEP dates extending beyond Oct 2024
- CSPN wording that presents the project as ongoing
- the MNRAS paper described as published in Jun 2026
- the stray `======` line on the homepage

## Files in Scope

Expected public-content files:

- `_config.yml`
- `_pages/about.md`
- `_pages/contact.md`
- `_pages/cv.md`
- `_portfolio/2024-08-01-cloudy-manga.md`
- `_portfolio/2024-10-01-3pcf-fast-algorithm.md`
- `_portfolio/2024-12-01-frdeep-xai.md`
- `_portfolio/2025-03-01-cspn-multimodal.md`
- one new `_portfolio/*.md` file for AI workflow automation
- `_publications/2023-08-01-local-interpretation-radio-galaxy.md`
- `_publications/2024-12-01-pair-counting-without-binning.md`
- `_publications/2025-02-01-can-i-trust-you.md`
- one new `_publications/*.md` file for the A&A submission
- `_data/cv.json`, limited to removal of misleading template data

The implementation plan must inspect existing talk entries before deciding
whether any talk metadata needs wording-only consistency changes.

## Verification

The completed refresh must pass:

1. Repository search for stale identity and project facts
2. JSON/YAML/front-matter syntax checks
3. Jekyll production build
4. Rendered desktop and mobile inspection of:
   - Homepage
   - CV
   - Publications
   - Portfolio index and all five project pages
   - Contact
5. Internal-link and downloadable-CV checks
6. Final claim review against this specification and the evidence guardrails
7. Privacy review confirming that the approved phone appears only on Contact
   and CV and that no residential address is published

## Out of Scope

- Visual theme replacement
- Navigation redesign
- A new JavaScript application or interactive portfolio
- Rebuilding the Markdown-to-JSON CV converter
- Adding unsupported tools for keyword coverage
- Publishing or deploying the website
- Replacing the downloadable PDF until a canonical PDF version is selected

