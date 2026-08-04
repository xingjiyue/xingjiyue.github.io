# Academic Homepage Visual Redesign Design

**Date:** 2026-08-04

**Status:** Approved in conversation; awaiting review of this written specification

## Goal

Redesign Shiyu Yue's academic website so that a visitor can quickly understand
who Shiyu is, what research she has done, what her individual contributions
were, and which outputs are published, under revision, submitted, or presented.

The redesign must correct the current visual problems: a space-heavy permanent
sidebar, nearly uniform typography, long prose blocks, project listings with no
research figures, and talk entries whose types or titles are not consistently
supported by source material.

The finished site should look like a conventional, polished academic homepage,
not a corporate landing page, dashboard, or decorated CV.

## Evidence and Claim Policy

Content authority remains, in order:

1. Facts explicitly confirmed by the user in this redesign conversation
2. The newest local manuscript, paper, CV, Keynote, and presentation evidence
3. The evidence guardrails in `job_hunt_kb`
4. Existing website content

The site must distinguish publication and presentation states exactly:

- `published` only for published work
- `under revision` for the ApJS manuscript
- `submitted Aug 2026` for the A&A manuscript
- `talk` or `invited talk` only where the presentation type is verified
- `co-authored conference proceeding` for the URSI GASS output; it must not be
  described as a talk or poster

Project figures must come from Shiyu's own papers, manuscripts, talks, analyses,
or workflow materials. Decorative stock imagery is not used. Captions explain
the question, Shiyu's work, and the visible conclusion rather than repeating the
figure title.

For the Cloudy/MaNGA project, the old public claim that a revised configuration
"approximately halved" the discrepancy must not be retained unless the final
submitted-manuscript evidence supports it. The May 2026 research deck supports
the more conservative conclusion that abundance shifts do not reconcile the
joint diagnostics and that ionising-SED shape or model physics remains a leading
direction.

## Reference Patterns

The selected design combines established patterns observed in academic sites:

- Jon Barron's compact paper rows with research thumbnails, complete titles,
  venue/status, one-line contributions, and direct links
- Ryan Golant's use of real research images to make project descriptions
  concrete
- al-folio's concise biography, news, and selected-publication hierarchy

The chosen direction is **paper-first compact**, with a larger portrait added to
the introductory area. The research rows remain the dominant scanning structure.

## Site-wide Visual System

### Page frame

- Remove the permanent left sidebar from all primary pages.
- Use a centered content column of approximately 980-1040 px on desktop.
- Use a lightweight top navigation: `Shiyu Yue`, `Projects`, `Publications`,
  `Talks`, `CV`, and `Contact`.
- Keep navigation and content responsive without horizontal scrolling.
- Replace the current large blue footer with a minimal neutral footer.
- Use one polished light academic theme. Remove the theme toggle and avoid the
  burden of maintaining a second visual system.

### Typography

Typography communicates content purpose rather than applying one face and size
to everything:

- Serif: name, page titles, section titles, paper titles, and project titles
- Sans serif: biography, metadata, dates, statuses, captions, navigation, and
  body copy
- Name: approximately 44-52 px desktop
- Page and major section headings: approximately 28-34 px desktop
- Paper/project titles: approximately 20-24 px desktop
- Body copy: approximately 16-18 px desktop
- Metadata and status text: approximately 13-14 px desktop

Exact values may be adjusted during visual QA, but the hierarchy must remain
obvious and the body text must not be shrunk to fit.

### Colour and spacing

- Use a paper-like light background, near-black text, muted secondary text, and
  one restrained academic accent colour for links and active states.
- Use whitespace and thin neutral dividers instead of repeated cards, coloured
  panels, or heavy shadows.
- Keep line lengths readable and vertical rhythm consistent across pages.

## Homepage

The homepage uses the confirmed compact portrait variant.

### Hero

The hero has biography and education on the left and an enlarged portrait on
the right. The portrait is approximately 180 x 220 px on desktop, with a smaller
but still prominent treatment on mobile.

The hero contains:

- `Shiyu Yue`
- `Physics MPhil candidate · The Chinese University of Hong Kong`
- one concise positioning paragraph about scalable statistical algorithms,
  interpretable machine learning, and Bayesian pipelines for astronomical data
- two clear education lines:
  - `MPhil in Physics · The Chinese University of Hong Kong · Aug 2024-Oct 2026 (expected)`
  - `BSc in Physics · Sun Yat-sen University · Sep 2020-Jul 2024`
- Email, CV, GitHub, and LinkedIn links

The phone number does not appear in the hero.

### Highlighted papers

The homepage highlights exactly three paper-linked projects. Each row contains
one real research thumbnail, the complete paper/manuscript title, formal status,
Shiyu's concrete contribution, and only links that exist.

1. **Pair counting without binning - a new approach to correlation functions in clustering statistics**
   - `MNRAS 2024 · first author`
   - O(N log N) estimator, C++/OpenMP implementation, and MDPL2 validation

2. **Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI**
   - `ApJS · under revision`
   - CNN classification, LIME audit, data-quality and failure analysis

3. **The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models**
   - `A&A · submitted Aug 2026`
   - 3D model-data diagnostics, Cloudy grids, and Bayesian inference with MaNGA

### Recent news

Recent news is a compact date-and-event list rather than large bullets. It shows
no more than five current, verified items and links to the relevant project,
paper, or talk when available.

### Removed homepage content

The existing research-interest keyword paragraph and repeated research-highlight
bullet list are removed. The highlighted paper rows already communicate those
themes more specifically and with stronger evidence.

## Projects Information Architecture

The `/portfolio/` Projects page must itself be detailed. It is not only an index
of titles. It shows meaningful evidence before a visitor clicks into a project.

### Projects landing page

Each project section contains:

1. Full project or paper title
2. Institution, role, dates, and publication status
3. One-sentence research question
4. Three concrete contribution lines:
   - What I built
   - How I tested or validated it
   - What the result or output was
5. One core figure with an explanatory caption
6. Existing links such as `Read details`, `Paper`, `Talk`, or `Code`

The page groups four entries under **Research Projects** and the AI workflow
entry under **Engineering Project**.

### Project detail pages

Every project detail page follows the same readable structure:

```text
Research question
My role
At a glance
What I built
Method
Validation
Results
Outputs
```

The three paper-linked projects receive two figures each: one method figure and
one result figure. CSPN and AI Workflow receive at least one evidence-bearing
figure or diagram. Figures have concise captions and descriptive alt text.

### Project-specific content

#### Pair counting without binning - a new approach to correlation functions in clustering statistics

- Explain the in-situ convolution reformulation of pair counting.
- Describe the binning-aware formalism and C++/OpenMP implementation.
- Show validation against theory and MDPL2/Quijote simulations.
- Use a 3PCF measurement schematic and a simulation-theory comparison.
- Keep project-specific performance claims with their precise context.

#### Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI

- Identify the institutions as Sun Yat-sen University / Tsinghua University.
- Use the verified period `Jul 2021-Oct 2024`.
- Describe the 650-image review, source-level five-fold evaluation, and 91.4%
  mean test accuracy.
- Explain Felzenszwalb segmentation, LIME explanations, and failure analysis.
- Include the masked Set Transformer as implemented work without claiming an
  unverified improvement over the CNN.
- Use a radio-image-to-segmentation-to-LIME figure and a result/failure figure.

#### The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models

- Explain MaNGA star-forming-spaxel selection and Cloudy model-grid generation.
- Explain the reprojected 3D diagnostic spaces, KDE, RBF interpolation,
  model-data distance, and Bayesian inference.
- Distinguish early exploratory configurations from the conclusion supported by
  the submitted manuscript and newest local research evidence.
- Use a data/model/distance method figure and a joint-diagnostic result figure.
- Report `submitted to A&A in Aug 2026`; do not imply acceptance.

#### Hunting Central Stars of Round Galactic Planetary Nebulae

- Use `The University of Hong Kong Space Laboratory · Sep-Dec 2023`.
- Describe HASH, PanSTARRS, DECaPS, and Gaia source reconciliation.
- Explain coordinate matching, offset analysis, duplicate control, candidate
  validation, and contamination checks.
- Describe the multimodal extension in the past tense as an explored project
  direction, not an ongoing production system.
- Use a source-integration workflow or candidate/offset result figure.

#### AI Workflow Automation and Decision Support

- Label it `Personal engineering project · Mar-May 2026`.
- Show ingestion, normalization, retrieval, schema validation, conditional
  routing, retries, logging, state tracking, email notification, and human review.
- Use an end-to-end workflow diagram.
- Do not claim a commercial deployment, production ownership, or unsupported
  performance metrics.

### Research route

The existing `/research/` route becomes an alias or redirect to `/portfolio/` so
there is one maintained source for detailed project content.

## Publications

Publications use the same scan-first visual language as the homepage, but show
the full publication list. Published outputs expose canonical links; submitted
or under-revision work gets an external link only when a public preprint exists.

Each entry contains title, authors, venue/status, year, contribution context
when useful, thumbnail when available, and verified links. The URSI item remains
a publication/conference proceeding, not a presentation.

## Talks and Presentations

The page is divided into two groups.

### Oral and invited talks

Reverse chronological order:

1. **Talk · May 2026**  
   *The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models*  
   Guo Shoujing Telescope Workshop

2. **Talk · Jan 2026**  
   *How to Fit All Emission Lines Simultaneously with Photoionisation Models*  
   CCBC Symposium

3. **Talk · Dec 2023**  
   *Hunting Central Stars of Round Galactic Planetary Nebulae*  
   HKU Laboratory for Space Research Jamboree · Best Speaker Award

4. **Talk · Nov 2023**  
   *Pair counting without binning - a new approach to correlation functions in clustering statistics*  
   International Workshop on Intelligent Computing in Astronomy

5. **Invited Talk · Nov 2023**  
   *A model local interpretation routine for deep learning based radio galaxy classification*  
   International Workshop on Machine Learning in Astronomy

Dates use day-level precision only where the source material verifies the day.
Unsupported `Virtual / International` or inferred location labels are removed.

### Related conference output

Placed after the oral and invited talks:

- **Co-authored conference proceeding · Aug 2023**  
  *A model local interpretation routine for deep learning based radio galaxy classification*  
  IEEE URSI GASS 2023

This item links to the proceeding and does not use `presented`, `talk`, `oral`,
or `poster` wording.

## CV and Education

The public CV remains an HTML page with a downloadable PDF button. It uses the
same site-wide typography and removes the permanent sidebar.

Education entries use a clear visual hierarchy:

- Degree and institution are primary.
- Dates are visually aligned and secondary.
- `expected` is explicitly attached to Oct 2026.
- Scholarship, GPA, ranking, and honours appear on separate subordinate lines.

Confirmed education content:

- `MPhil in Physics`, The Chinese University of Hong Kong,
  `Aug 2024-Oct 2026 (expected)`, Postgraduate Studentship
- `BSc in Physics`, Sun Yat-sen University, `Sep 2020-Jul 2024`,
  GPA 3.9/4.0 (Top 5%), Outstanding Graduate, Outstanding Graduation Thesis

The phone number `+852 4434 6668` appears only on CV and Contact. The professional
email is `yshiyu@link.cuhk.edu.hk`. No private residential address is published.

## Component and Data Design

The implementation keeps Jekyll and the existing content collections. It does
not migrate the site to another framework.

Reusable includes or layouts will cover:

- paper/project row
- project metadata
- figure and caption
- education row
- talk entry
- compact news row

Project front matter will consistently hold:

- complete title
- project category
- institution and role
- start/end dates
- publication state
- thumbnail
- figures, captions, and alt text
- paper, talk, and code links when they exist

Missing optional links or images produce no empty buttons or broken placeholders.
Shared content should be stored once and rendered into the appropriate overview
or detail component when practical.

The existing unused `folio_base`/`folio_style.css` experiment should be removed
or left unreferenced after the new scoped Sass/CSS implementation is in place.

## Responsive and Accessibility Requirements

- The hero becomes a single column on mobile while keeping the portrait visible.
- Paper/project rows retain a readable thumbnail and text relationship at narrow
  widths; they stack when necessary.
- No text, navigation, figure, or control overlaps at desktop, tablet, or phone
  widths.
- Every informative image has descriptive alt text and a visible caption.
- Link text identifies its destination; links are not represented by colour alone.
- Text and muted metadata maintain accessible contrast.
- Native heading order and keyboard navigation remain intact.

## Verification

The implementation must pass:

1. Jekyll production build
2. YAML/front-matter and structured-data validation
3. Internal-link, PDF, and external-publication-link checks
4. Repository searches for stale identity data, placeholder links, unsupported
   talk types, and removed claims
5. Desktop, tablet, and mobile visual QA for:
   - Homepage
   - Projects landing page
   - All five project detail pages
   - Publications
   - Talks
   - CV
   - Contact
6. Figure QA at rendered size for crop, legibility, caption, and attribution
7. Privacy review confirming that the phone appears only on CV and Contact and
   that no residential address is public
8. Final evidence review of title, status, dates, institution, and presentation
   type against this specification

## Files Expected in Scope

Implementation will likely touch:

- `_config.yml`
- `_data/navigation.yml`
- `_pages/about.md`
- `_pages/portfolio.html`
- `_pages/publications.html`
- `_pages/talks.html`
- `_pages/cv.md`
- `_pages/contact.md`
- `_pages/research.md`
- all five `_portfolio/*.md` files
- relevant `_publications/*.md` and `_talks/*.md` files
- new or revised `_includes/*.html` presentation components
- one scoped Sass/CSS entry or partial
- `images/` or a dedicated project-figure asset directory

The implementation plan must inspect the final generated HTML before choosing
the exact include boundaries and must preserve stable public URLs where possible.

## Out of Scope

- Migrating away from Jekyll/GitHub Pages
- Adding a blog, teaching page, analytics, CMS, or interactive research app
- Inventing publication links for private manuscripts
- Creating unverified performance claims
- Publishing or deploying the website unless the user separately requests it
- Rewriting the downloadable CV PDF in this redesign cycle
