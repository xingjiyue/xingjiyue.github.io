# Academic Homepage Visual Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild Shiyu Yue's Jekyll site as a compact, paper-first academic homepage with a clear typographic hierarchy, enlarged portrait, evidence-bearing project figures, detailed project pages, and source-verified publication, talk, education, and contact information.

**Architecture:** Keep the existing Academic Pages/Jekyll collections and public URLs, but replace their sidebar-driven presentation with a new no-sidebar `academic` layout and scoped reusable components. Store project/publication facts and figure metadata in front matter, render them through shared Liquid includes, and enforce content and generated-HTML contracts with Python `unittest` tests plus a production Jekyll build. Treat `/portfolio/` as the single maintained research index and redirect `/research/` to it.

**Tech Stack:** Jekyll 4, Liquid, Markdown/Kramdown, Sass, vanilla JavaScript/jQuery already present in the theme, Python 3 standard-library tests, Poppler/macOS image utilities for source-figure extraction, and the in-app browser for responsive visual QA.

## Global Constraints

- The approved specification is `docs/superpowers/specs/2026-08-04-academic-homepage-visual-redesign-design.md`; where existing site text conflicts with it, the specification wins.
- Run every repository shell command with the required `rtk` prefix from `/Users/yshiyu/Desktop/my_materials/website`.
- Use `/opt/homebrew/opt/ruby/bin/bundle` (Bundler 4.0.11 with Ruby 4.0.5), not the macOS system Ruby.
- Preserve existing public URLs for collection items and primary pages.
- Do not publish private manuscripts, invent links, infer presentation types, or reintroduce the unsupported Cloudy claim that a revised configuration “approximately halved” the discrepancy.
- Phone `+852 4434 6668` may appear only on `/cv/` and `/contact/`; use `yshiyu@link.cuhk.edu.hk` everywhere.
- Use only Shiyu's paper, manuscript, talk, analysis, or workflow materials for project visuals. Every informative image needs visible caption text and descriptive alt text.
- Do not deploy or push. Each task ends with a local commit containing only the files named in that task.

---

### Task 1: Establish the academic shell and source-level contract tests

**Files:**

- Create: `tests/__init__.py`
- Create: `tests/test_site_contract.py`
- Create: `_layouts/academic.html`
- Create: `_sass/layout/_academic.scss`
- Modify: `.gitignore`
- Modify: `_config.yml`
- Modify: `_data/navigation.yml`
- Modify: `_layouts/default.html`
- Modify: `_includes/masthead.html`
- Modify: `_includes/footer.html`
- Modify: `assets/css/main.scss`
- Modify: `assets/js/_main.js`
- Regenerate: `assets/js/main.min.js`

- [ ] Add `.superpowers/` to `.gitignore` so the visualization companion remains local and cannot enter a site commit.

- [ ] Create `tests/test_site_contract.py` with reusable repository helpers and the first shell contracts:

```python
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class SiteShellContractTests(unittest.TestCase):
    def test_primary_navigation_is_compact_and_not_duplicated(self):
        navigation = read("_data/navigation.yml")
        self.assertNotIn('title: "About"', navigation)
        for label in ("Projects", "Publications", "Talks", "CV", "Contact"):
            self.assertEqual(navigation.count(f'title: "{label}"'), 1)

    def test_academic_layout_has_one_primary_main_region_and_no_sidebar(self):
        layout = read("_layouts/academic.html")
        self.assertEqual(len(re.findall(r"<main\b", layout)), 1)
        self.assertIn('class="academic-shell"', layout)
        self.assertNotIn("sidebar", layout.lower())

    def test_dark_theme_and_theme_toggle_are_removed(self):
        self.assertNotIn("_dark", read("assets/css/main.scss"))
        self.assertNotIn("theme-toggle", read("_includes/masthead.html"))
        script = read("assets/js/_main.js")
        for stale in ("determineThemeSetting", "setTheme", "toggleTheme"):
            self.assertNotIn(stale, script)

    def test_academic_css_defines_required_visual_hierarchy(self):
        css = read("_sass/layout/_academic.scss")
        for selector in (
            ".academic-shell",
            ".academic-page__title",
            ".profile-hero__name",
            ".paper-row__title",
            ".project-summary__title",
            ".academic-figure",
        ):
            self.assertIn(selector, css)


if __name__ == "__main__":
    unittest.main()
```

- [ ] Run the source tests and confirm they fail because the academic layout and styles do not exist yet:

```bash
rtk python3 -m unittest tests.test_site_contract -v
```

- [ ] Create `_layouts/academic.html` as the single no-sidebar page frame:

```liquid
---
layout: default
---
<main id="main" class="academic-shell" role="main">
  <article class="academic-page{% if page.page_class %} {{ page.page_class }}{% endif %}">
    {% unless page.hide_title %}
      <header class="academic-page__header">
        {% if page.kicker %}<p class="academic-page__kicker">{{ page.kicker }}</p>{% endif %}
        <h1 class="academic-page__title">{{ page.title }}</h1>
        {% if page.intro %}<p class="academic-page__intro">{{ page.intro }}</p>{% endif %}
      </header>
    {% endunless %}
    <div class="academic-page__content">
      {{ content }}
    </div>
  </article>
</main>
```

- [ ] Update `_config.yml` collection/page defaults so pages, portfolio items, publications, and talks use `layout: academic` and `author_profile: false`; keep current permalinks and future-dated content enabled.

```yaml
defaults:
  - scope:
      path: ""
      type: pages
    values:
      layout: academic
      author_profile: false
  - scope:
      path: ""
      type: portfolio
    values:
      layout: academic
      author_profile: false
  - scope:
      path: ""
      type: publications
    values:
      layout: academic
      author_profile: false
  - scope:
      path: ""
      type: talks
    values:
      layout: academic
      author_profile: false
```

- [ ] Remove the duplicate `About` item from `_data/navigation.yml`; keep `Shiyu Yue` as the masthead home link followed by `Projects`, `Publications`, `Talks`, `CV`, and `Contact`.

- [ ] Replace `_includes/masthead.html` with the existing greedy-navigation structure but no theme control. Keep exactly one brand link and the five data-driven navigation entries. Give the menu button `aria-label="Toggle navigation"`.

- [ ] Replace `_includes/footer.html` with a neutral single-line footer:

```liquid
<div class="page__footer-copyright">
  &copy; {{ site.time | date: '%Y' }} {{ site.name | default: site.title }}
  <span aria-hidden="true"> · </span>
  <a href="/sitemap/">Sitemap</a>
</div>
```

- [ ] Remove conditional dark-theme markup from `_layouts/default.html`. Add `class="site-body"` to `<body>` and keep the existing browser-upgrade, masthead, content, footer, and script order.

- [ ] Remove the dark-theme Sass import from `assets/css/main.scss`, add `"layout/academic"` after the base layout imports, and keep vendor imports intact.

- [ ] Create `_sass/layout/_academic.scss` with a complete scoped visual system:

```scss
$academic-serif: Georgia, "Times New Roman", serif;
$academic-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
$academic-paper: #fbfaf7;
$academic-ink: #202124;
$academic-muted: #62666d;
$academic-rule: #d9d7d0;
$academic-link: #315f8c;

.site-body { background: $academic-paper; color: $academic-ink; }
.academic-shell { width: min(100% - 40px, 1020px); margin: 0 auto; padding: 56px 0 88px; }
.academic-page__header { max-width: 760px; margin-bottom: 42px; }
.academic-page__kicker { margin: 0 0 8px; color: $academic-muted; font: 600 0.78rem/1.4 $academic-sans; letter-spacing: .08em; text-transform: uppercase; }
.academic-page__title,
.profile-hero__name,
.paper-row__title,
.project-summary__title { color: $academic-ink; font-family: $academic-serif; font-weight: 500; letter-spacing: -.015em; }
.academic-page__title { margin: 0; font-size: clamp(2rem, 4vw, 2.65rem); line-height: 1.08; }
.academic-page__intro { max-width: 680px; margin: 18px 0 0; color: $academic-muted; font: 1.08rem/1.65 $academic-sans; }
.academic-page__content { font: 1rem/1.68 $academic-sans; }
.academic-page__content h2 { margin: 58px 0 22px; font: 500 clamp(1.65rem, 3vw, 2rem)/1.18 $academic-serif; }
.academic-page__content h3 { margin: 34px 0 12px; font: 500 1.35rem/1.28 $academic-serif; }
.academic-page__content a { color: $academic-link; text-underline-offset: .16em; }
.section-heading { display: flex; align-items: baseline; justify-content: space-between; gap: 20px; margin: 54px 0 20px; border-bottom: 1px solid $academic-rule; padding-bottom: 10px; }
.section-heading h2 { margin: 0; }
.paper-row,
.project-summary { display: grid; grid-template-columns: minmax(180px, 30%) 1fr; gap: 26px; padding: 26px 0; border-bottom: 1px solid $academic-rule; }
.paper-row__title,
.project-summary__title { margin: 0 0 8px; font-size: clamp(1.3rem, 2.4vw, 1.55rem); line-height: 1.25; }
.paper-row__meta,
.project-summary__meta,
.project-summary__label { color: $academic-muted; font-size: .84rem; line-height: 1.5; }
.paper-row__image,
.project-summary__image { width: 100%; aspect-ratio: 4 / 3; object-fit: contain; background: #fff; border: 1px solid $academic-rule; }
.academic-figure { margin: 34px 0; }
.academic-figure img { display: block; width: 100%; height: auto; background: #fff; border: 1px solid $academic-rule; }
.academic-figure figcaption { margin-top: 10px; color: $academic-muted; font-size: .84rem; line-height: 1.55; }
.link-row { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 12px; font-size: .88rem; }
.link-row a { font-weight: 600; }
@media (max-width: 700px) {
  .academic-shell { width: min(100% - 28px, 1020px); padding: 34px 0 64px; }
  .paper-row,
  .project-summary { grid-template-columns: 1fr; gap: 16px; }
  .paper-row__image,
  .project-summary__image { max-height: 260px; }
}
```

- [ ] Remove theme-setting/toggle code and the dark/light Plotly switch from `assets/js/_main.js`. Keep FitVids, greedy navigation, smooth scrolling, and sticky-footer behavior. If Plotly blocks are retained, render them with `plotlyLightLayout` only.

- [ ] Regenerate the minified bundle and run tests/build:

```bash
rtk npm install
rtk npm run build:js
rtk python3 -m unittest tests.test_site_contract -v
rtk /opt/homebrew/opt/ruby/bin/bundle exec jekyll build
```

- [ ] Commit only the shell/test files:

```bash
rtk git add .gitignore tests _config.yml _data/navigation.yml _layouts/academic.html _layouts/default.html _includes/masthead.html _includes/footer.html _sass/layout/_academic.scss assets/css/main.scss assets/js/_main.js assets/js/main.min.js
rtk git commit -m "feat: establish compact academic site shell"
```

---

### Task 2: Add reusable academic content components and metadata contracts

**Files:**

- Create: `_includes/academic/figure.html`
- Create: `_includes/academic/link-row.html`
- Create: `_includes/academic/education-row.html`
- Create: `_includes/academic/news-row.html`
- Create: `_includes/academic/paper-row.html`
- Create: `_includes/academic/project-summary.html`
- Create: `_includes/academic/talk-entry.html`
- Modify: `_sass/layout/_academic.scss`
- Modify: `tests/test_site_contract.py`

- [ ] Extend `tests/test_site_contract.py` with component contracts that assert each include exists, every image include emits `alt` and `figcaption`, and optional links are guarded by Liquid conditions.

```python
class ComponentContractTests(unittest.TestCase):
    def test_figure_component_is_accessible(self):
        figure = read("_includes/academic/figure.html")
        self.assertIn('alt="{{ include.alt }}"', figure)
        self.assertIn("<figcaption>", figure)

    def test_optional_links_are_guarded(self):
        links = read("_includes/academic/link-row.html")
        for key in ("paper_url", "talk_url", "code_url", "details_url"):
            self.assertIn(f"if include.{key}", links)

    def test_all_reusable_components_exist(self):
        for name in (
            "education-row.html", "news-row.html", "paper-row.html",
            "project-summary.html", "talk-entry.html",
        ):
            self.assertTrue((ROOT / "_includes" / "academic" / name).is_file())
```

- [ ] Run the new tests and confirm they fail before component creation.

- [ ] Implement `_includes/academic/figure.html`:

```liquid
<figure class="academic-figure{% if include.class %} {{ include.class }}{% endif %}">
  <img src="{{ include.src }}" alt="{{ include.alt }}" loading="lazy"{% if include.width %} width="{{ include.width }}"{% endif %}{% if include.height %} height="{{ include.height }}"{% endif %}>
  <figcaption>{{ include.caption }}</figcaption>
</figure>
```

- [ ] Implement `_includes/academic/link-row.html` with only existing destinations:

```liquid
<div class="link-row" aria-label="Related links">
  {% if include.details_url %}<a href="{{ include.details_url }}">Read details</a>{% endif %}
  {% if include.paper_url %}<a href="{{ include.paper_url }}">Paper</a>{% endif %}
  {% if include.talk_url %}<a href="{{ include.talk_url }}">Talk</a>{% endif %}
  {% if include.code_url %}<a href="{{ include.code_url }}">Code</a>{% endif %}
</div>
```

- [ ] Implement `education-row.html`, `news-row.html`, and `talk-entry.html` with semantic structures, visible date/status labels, and no inline styles:

```liquid
<!-- education-row.html -->
<div class="education-row">
  <div><strong>{{ include.degree }}</strong><span>{{ include.institution }}</span></div>
  <time>{{ include.dates }}</time>
  {% if include.note %}<p>{{ include.note }}</p>{% endif %}
</div>

<!-- news-row.html -->
<div class="news-row">
  <time>{{ include.date }}</time>
  <p>{% if include.url %}<a href="{{ include.url }}">{{ include.text }}</a>{% else %}{{ include.text }}{% endif %}</p>
</div>

<!-- talk-entry.html -->
<article class="talk-entry">
  <p class="talk-entry__meta">{{ include.item.display_type }} · {{ include.item.display_date }}</p>
  <h2><a href="{{ include.item.url }}">{{ include.item.title }}</a></h2>
  <p>{{ include.item.venue }}{% if include.item.award %} · {{ include.item.award }}{% endif %}</p>
</article>
```

- [ ] Implement `paper-row.html` from a passed collection document and `project-summary.html` from a passed portfolio document. Both must render the complete title, status/meta line, concrete contribution/question, thumbnail with alt text, and guarded link row. Do not truncate titles. Use the following complete project-summary structure; the paper-row structure follows directly below it.

```liquid
<article class="project-summary">
  <div>
    <img class="project-summary__image" src="{{ include.item.thumbnail }}" alt="{{ include.item.thumbnail_alt }}" loading="lazy">
    <p class="project-summary__caption">{{ include.item.thumbnail_caption }}</p>
  </div>
  <div>
    <p class="project-summary__meta">{{ include.item.institution }} · {{ include.item.role }} · {{ include.item.period }}</p>
    <h3 class="project-summary__title"><a href="{{ include.item.url }}">{{ include.item.title }}</a></h3>
    <p><strong>Research question.</strong> {{ include.item.research_question }}</p>
    <dl class="project-summary__facts">
      <dt>What I built</dt><dd>{{ include.item.built }}</dd>
      <dt>How I tested it</dt><dd>{{ include.item.validation }}</dd>
      <dt>Result / output</dt><dd>{{ include.item.result }}</dd>
    </dl>
    {% include academic/link-row.html details_url=include.item.url paper_url=include.item.paper_url talk_url=include.item.talk_url code_url=include.item.code_url %}
  </div>
</article>
```

```liquid
<article class="paper-row">
  <a href="{{ include.item.project_url | default: include.item.url }}" aria-label="Read {{ include.item.title }}">
    <img class="paper-row__image" src="{{ include.item.thumbnail }}" alt="{{ include.item.thumbnail_alt }}" loading="lazy">
  </a>
  <div>
    <p class="paper-row__meta">{{ include.item.display_status }}</p>
    <h3 class="paper-row__title"><a href="{{ include.item.project_url | default: include.item.url }}">{{ include.item.title }}</a></h3>
    <p>{{ include.item.contribution }}</p>
    {% include academic/link-row.html details_url=include.item.project_url paper_url=include.item.paperurl talk_url=include.item.talk_url code_url=include.item.code_url %}
  </div>
</article>
```

- [ ] Add matching styles for `.education-row`, `.news-row`, `.talk-entry`, `.project-summary__facts`, and responsive component behavior. Dates must be secondary text and never carry the same font size/weight as titles.

- [ ] Run source tests and the production build, inspect that Liquid compiles, then commit:

```bash
rtk python3 -m unittest tests.test_site_contract -v
rtk /opt/homebrew/opt/ruby/bin/bundle exec jekyll build
rtk git add _includes/academic _sass/layout/_academic.scss tests/test_site_contract.py
rtk git commit -m "feat: add reusable academic content components"
```

---

### Task 3: Create the evidence-bearing project figure set

**Files:**

- Create: `scripts/extract_project_figures.sh`
- Create: `images/projects/3pcf-method.png`
- Create: `images/projects/3pcf-validation.png`
- Create: `images/projects/frdeep-method.png`
- Create: `images/projects/frdeep-results.png`
- Create: `images/projects/siii-method.png`
- Create: `images/projects/siii-results.png`
- Create: `images/projects/cspn-workflow.svg`
- Create: `images/projects/ai-workflow.svg`
- Modify: `tests/test_site_contract.py`

- [ ] Add a figure-manifest test. It must assert all eight files exist, have nonzero size, and each raster image begins with the PNG signature; it must also reject `tmp/`, `_site/`, or `.superpowers/` figure paths.

```python
class ProjectFigureContractTests(unittest.TestCase):
    FIGURES = (
        "3pcf-method.png", "3pcf-validation.png",
        "frdeep-method.png", "frdeep-results.png",
        "siii-method.png", "siii-results.png",
        "cspn-workflow.svg", "ai-workflow.svg",
    )

    def test_project_figure_manifest(self):
        for name in self.FIGURES:
            path = ROOT / "images" / "projects" / name
            self.assertTrue(path.is_file(), name)
            self.assertGreater(path.stat().st_size, 200, name)
            if path.suffix == ".png":
                self.assertEqual(path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
```

- [ ] Write `scripts/extract_project_figures.sh` as a reproducible asset-preparation script. It accepts `/Users/yshiyu/Desktop/my_materials` as argument 1, renders source pages at 180–220 dpi, crops only figure regions, strips temporary page renders, and writes the six named PNGs under `images/projects/`. Source mapping:

```text
3pcf-method.png       ← job_hunt_kb/Pair counting without binning – a new approach to correlation functions in clustering statistics.pdf, PDF page 11, Figure 6
3pcf-validation.png   ← same PDF/page, Figure 7
frdeep-method.png     ← job_hunt_kb/ApJ_Can_I_trust_you.pdf, PDF page 12, Figures 1–2
frdeep-results.png    ← same PDF, PDF page 19, Figures 8–9
siii-method.png       ← job_hunt_kb/郭守敬_May23.pdf, PDF page 9, model–data distance diagnostic
siii-results.png      ← same PDF, PDF page 12, joint-diagnostic result
```

The script must use `mktemp -d`, `trap` cleanup, `pdftocairo` or `pdftoppm`, and `sips` crop commands. It must fail if a source is missing and must never modify the source PDFs.

- [ ] Run the script once, inspect every crop at original resolution, and adjust the crop rectangles until axes/labels are readable and no surrounding paper body text remains:

```bash
rtk bash scripts/extract_project_figures.sh /Users/yshiyu/Desktop/my_materials
rtk sips -g pixelWidth -g pixelHeight images/projects/*.png
```

- [ ] Create `cspn-workflow.svg` as a semantic source-integration diagram with this exact flow: `HASH targets → PanSTARRS + DECaPS source reconciliation → coordinate/offset and duplicate controls → Gaia astrometric validation → reviewed candidate list`. Add an internal SVG `<title>` and `<desc>`.

- [ ] Create `ai-workflow.svg` as an end-to-end workflow diagram with this exact flow: `Web/API ingestion → normalization and deduplication → retrieval → LLM structured output → schema validation → conditional routing/retries → logging and state → email notification → human review`. Add an internal SVG `<title>` and `<desc>` and do not include product logos.

- [ ] Run the figure tests and open every raster/SVG directly for legibility. Commit only source script and final assets:

```bash
rtk python3 -m unittest tests.test_site_contract -v
rtk git add scripts/extract_project_figures.sh images/projects tests/test_site_contract.py
rtk git commit -m "feat: add evidence-based project figures"
```

---

### Task 4: Rebuild the homepage around the enlarged portrait and three papers

**Files:**

- Modify: `_pages/about.md`
- Modify: `_sass/layout/_academic.scss`
- Modify: `tests/test_site_contract.py`

- [ ] Add homepage tests asserting `layout: academic`, `hide_title: true`, the portrait path, both education periods, the professional email, exactly three `paper-row` includes, no phone, no `Research interests` heading, and no `approximately halved` text.

- [ ] Replace `_pages/about.md` with a custom hero followed by three highlighted paper rows and compact news. Use this exact factual copy in the hero:

```html
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
```

- [ ] Render exactly these three publications through `paper-row.html`, in this order: MNRAS pair counting, ApJS FR-DEEP, A&A [S III]. Do not include the URSI proceeding in the homepage highlights.

- [ ] Add at most four news rows:

```text
Aug 2026 — [S III] discrepancy manuscript submitted to Astronomy & Astrophysics.
May 2026 — Presented the [S III] discrepancy work at the Guo Shoujing Telescope Workshop.
Feb 2025 — “Can I trust you?” manuscript under revision at ApJS.
Dec 2024 — “Pair counting without binning” published in MNRAS 535(4).
```

- [ ] Add desktop/mobile hero styles. Desktop uses two columns with a portrait approximately `184 × 224px`; mobile keeps the portrait visible above or directly after the introductory copy. Name size must use `clamp(2.75rem, 6vw, 3.35rem)` and portrait must not shrink below 144 px width.

- [ ] Run tests/build and inspect `/` at 1440, 768, and 390 CSS-pixel widths. Confirm the first viewport communicates identity, education, and research direction without a sidebar.

- [ ] Commit:

```bash
rtk git add _pages/about.md _sass/layout/_academic.scss tests/test_site_contract.py
rtk git commit -m "feat: rebuild academic homepage"
```

---

### Task 5: Make the Projects landing page detailed and paper-titled

**Files:**

- Modify: `_pages/portfolio.html`
- Modify: all five `_portfolio/*.md` front matter blocks
- Modify: `_sass/layout/_academic.scss`
- Modify: `tests/test_site_contract.py`

- [ ] Add portfolio schema tests requiring these front-matter keys on every project: `title`, `category`, `institution`, `role`, `period`, `status`, `research_question`, `built`, `validation`, `result`, `thumbnail`, `thumbnail_alt`, and `figures`. Require `figures` length 2 for the three paper-linked projects and at least 1 for CSPN/AI.

- [ ] Normalize project front matter to these exact titles/groups and verified metadata:

| File | Title | Group | Institution / period | Status |
|---|---|---|---|---|
| `2024-10-01-3pcf-fast-algorithm.md` | `Pair counting without binning – a new approach to correlation functions in clustering statistics` | Research Projects | Sun Yat-sen University · Oct 2021–Oct 2024 | MNRAS 2024 · first author |
| `2024-12-01-frdeep-xai.md` | `Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI` | Research Projects | Sun Yat-sen University / Tsinghua University · Jul 2021–Oct 2024 | ApJS · under revision |
| `2024-08-01-cloudy-manga.md` | `The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models` | Research Projects | The Chinese University of Hong Kong · Aug 2024–Oct 2026 (expected) | A&A · submitted Aug 2026 |
| `2025-03-01-cspn-multimodal.md` | `Hunting Central Stars of Round Galactic Planetary Nebulae` | Research Projects | The University of Hong Kong Space Laboratory · Sep–Dec 2023 | Research project · Best Speaker presentation |
| `2026-05-01-ai-workflow-automation.md` | `AI Workflow Automation and Decision Support` | Engineering Project | Personal engineering project · Mar–May 2026 | Completed personal project |

- [ ] Populate each project with one-sentence `research_question`, concrete `built`, `validation`, and `result` strings. The landing-page copy must state:

```text
3PCF — Built: binning-aware in-situ convolution estimator and C++/OpenMP pipeline. Validation: perturbation theory plus MDPL2 and Quijote simulations. Result: O(N log N) measurement route, published in MNRAS.
FR-DEEP — Built: CNN, Felzenszwalb/LIME audit, and masked Set Transformer extension. Validation: 650 reviewed images and source-level five-fold evaluation. Result: 91.4% mean test accuracy plus identified data/model failure modes; no Transformer superiority claim.
[S III] — Built: Cloudy grid and MaNGA 3D model–data/Bayesian pipeline. Validation: joint optical diagnostic spaces, KDE, RBF interpolation, and spaxel-level inference. Result: abundance shifts do not reconcile all diagnostics; SED/model physics remains a leading direction; submitted to A&A Aug 2026.
CSPN — Built: HASH/PanSTARRS/DECaPS/Gaia reconciliation and candidate-control workflow. Validation: offsets, duplicates, contamination, and Gaia astrometry. Result: reviewed candidate pipeline and an explored multimodal extension completed within Sep–Dec 2023.
AI workflow — Built: ingestion, normalization, retrieval, validation, routing, retry/logging, notification, and review stages. Validation: schema and state checks plus human-review checkpoints. Result: traceable personal workflow prototype; no production or commercial claim.
```

- [ ] Rebuild `_pages/portfolio.html` with `layout: academic`, an explanatory intro, four detailed `project-summary` components under `Research Projects`, and the AI entry under `Engineering Project`. Keep the core figure/caption visible on the landing page and keep each existing detail URL.

- [ ] Run schema/source tests, build, and visually inspect `/portfolio/` at desktop/mobile widths. Each entry must show meaningful project evidence before click-through.

- [ ] Commit:

```bash
rtk git add _pages/portfolio.html _portfolio _sass/layout/_academic.scss tests/test_site_contract.py
rtk git commit -m "feat: expand detailed projects index"
```

---

### Task 6: Rewrite all five project detail pages with a shared evidence structure

**Files:**

- Create: `_layouts/project.html`
- Create: `_includes/academic/project-hero.html`
- Modify: `_config.yml`
- Modify: `_portfolio/2024-08-01-cloudy-manga.md`
- Modify: `_portfolio/2024-10-01-3pcf-fast-algorithm.md`
- Modify: `_portfolio/2024-12-01-frdeep-xai.md`
- Modify: `_portfolio/2025-03-01-cspn-multimodal.md`
- Modify: `_portfolio/2026-05-01-ai-workflow-automation.md`
- Modify: `_sass/layout/_academic.scss`
- Modify: `tests/test_site_contract.py`

- [ ] Add detail-page tests requiring the exact ordered headings `Research question`, `My role`, `At a glance`, `What I built`, `Method`, `Validation`, `Results`, `Outputs`; reject stale headings/copy and require every front-matter figure to be rendered.

- [ ] Create `_layouts/project.html` nested on `academic` and a `project-hero.html` include that renders complete title, institution/role/period/status, research question, and guarded links. Set `hide_title: true` in the project layout to prevent duplicate `<h1>` elements. Change the portfolio collection default in `_config.yml` from `layout: academic` to `layout: project`.

- [ ] Rewrite the 3PCF detail page around the in-situ convolution reformulation, binning-aware theory, C++/OpenMP implementation, MDPL2/Quijote validation, and the MNRAS output. Render `3pcf-method.png` after `Method` and `3pcf-validation.png` after `Validation`. Keep performance claims scoped to the published setup: more than `10^8` particles and under eight hours on the stated compute context.

- [ ] Rewrite the FR-DEEP detail page with institutions `Sun Yat-sen University / Tsinghua University`, period `Jul 2021–Oct 2024`, 650-image review, source-level five-fold evaluation, 91.4% mean test accuracy, Felzenszwalb segmentation, LIME audit/failure analysis, and the masked Set Transformer as implemented work only. Render `frdeep-method.png` and `frdeep-results.png`.

- [ ] Rewrite the [S III] detail page around MaNGA star-forming-spaxel selection, Cloudy grids, reprojected 3D diagnostics, KDE, RBF interpolation, model–data distance, and Bayesian inference. Render `siii-method.png` and `siii-results.png`. Its results paragraph must use this conservative conclusion:

```text
The tested abundance adjustments do not reconcile the optical diagnostics simultaneously. The remaining tension points toward the ionising-SED shape and/or additional photoionisation-model physics as leading directions for further tests. The manuscript was submitted to Astronomy & Astrophysics in August 2026; this status does not imply acceptance.
```

- [ ] Rewrite the CSPN page in past tense around HASH, PanSTARRS, DECaPS, coordinate matching, offset/duplicate/contamination checks, and Gaia validation. Render `cspn-workflow.svg`. Describe the multimodal extension as explored during Sep–Dec 2023, not ongoing.

- [ ] Rewrite the AI Workflow page around ingestion, normalization, retrieval, structured outputs, schema validation, conditional routing, retries, logging/state, email notifications, and human review. Render `ai-workflow.svg`. State that it was a personal Mar–May 2026 prototype, not a commercial/production deployment.

- [ ] Run tests/build and inspect all five generated pages for single `<h1>`, heading order, readable figures/captions, correct links, and no unsupported claim.

- [ ] Commit:

```bash
rtk git add _config.yml _layouts/project.html _includes/academic/project-hero.html _portfolio _sass/layout/_academic.scss tests/test_site_contract.py
rtk git commit -m "feat: add detailed evidence-led project pages"
```

---

### Task 7: Rebuild Publications with canonical titles, statuses, and links

**Files:**

- Modify: `_pages/publications.html`
- Modify: all four `_publications/*.md`
- Modify: `_sass/layout/_academic.scss`
- Modify: `tests/test_site_contract.py`

- [ ] Add publication tests requiring complete title, authors/citation, display status, project URL, thumbnail/alt, and `paperurl` only when a verified public link exists. Reject `to be added`, the Cloudy “approximately halved” claim, and any claim that the URSI item was presented by Shiyu.

- [ ] Set exact publication titles/statuses:

```text
Pair counting without binning – a new approach to correlation functions in clustering statistics — MNRAS 535(4), 3500–3516 · 2024 · published
Can I trust you?: Interpreting radio galaxy classifier with FR-DEEP dataset and eXplainable AI — ApJS · under revision
The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models — A&A · submitted Aug 2026
A model local interpretation routine for deep learning based radio galaxy classification — IEEE URSI GASS 2023 · published conference proceeding
```

- [ ] Keep verified canonical links:

```text
MNRAS: https://doi.org/10.1093/mnras/stae2513
URSI proceeding: https://www.ursi.org/proceedings/procGA23/papers/YSASummaryHongmingTang.pdf
URSI arXiv: https://arxiv.org/abs/2307.03453
```

Do not add an external manuscript link for ApJS or A&A unless a public preprint is found in the existing source material during implementation.

- [ ] Rebuild `/publications/` with the shared `paper-row` component in reverse chronological order, preserving all current publication detail permalinks. Use research thumbnails for the three paper-linked items and the FR-DEEP figure for URSI.

- [ ] Update the A&A detail text to the conservative submitted-manuscript conclusion from Task 6. Update URSI text to “co-authored conference proceeding” and remove “presented” from its excerpt.

- [ ] Run tests/build, verify DOI/PDF links with non-mutating HTTP checks, and visually inspect `/publications/` and every publication detail page.

- [ ] Commit:

```bash
rtk git add _pages/publications.html _publications _sass/layout/_academic.scss tests/test_site_contract.py
rtk git commit -m "feat: rebuild verified publications pages"
```

---

### Task 8: Correct and regroup Talks and related conference output

**Files:**

- Modify: `_pages/talks.html`
- Modify: `_config.yml`
- Modify: `_layouts/talk.html`
- Modify: all six `_talks/*.md`
- Modify: `_includes/archive-single-talk-cv.html`
- Modify: `_sass/layout/_academic.scss`
- Modify: `tests/test_site_contract.py`

- [ ] Add talk tests that require five entries in `Oral and invited talks`, one URSI entry in `Related conference output`, and forbid `poster`, `Conference presentation`, `Virtual / International`, or URSI wording that says Shiyu presented it.

- [ ] Correct talk metadata to this exact ordered list:

| Type/date | Title | Venue |
|---|---|---|
| Talk · May 2026 | `The [S III] Discrepancy in Star-Forming Galaxies: A Challenge for Photoionization Models` | Guo Shoujing Telescope Workshop |
| Talk · Jan 2026 | `How to Fit All Emission Lines Simultaneously with Photoionisation Models` | CCBC Symposium |
| Talk · Dec 2023 | `Hunting Central Stars of Round Galactic Planetary Nebulae` | HKU Laboratory for Space Research Jamboree · Best Speaker Award |
| Talk · Nov 2023 | `Pair counting without binning – a new approach to correlation functions in clustering statistics` | International Workshop on Intelligent Computing in Astronomy |
| Invited Talk · Nov 2023 | `A model local interpretation routine for deep learning based radio galaxy classification` | International Workshop on Machine Learning in Astronomy |
| Co-authored conference proceeding · Aug 2023 | `A model local interpretation routine for deep learning based radio galaxy classification` | IEEE URSI GASS 2023 |

- [ ] Replace the incorrect Jan 2026 3PCF body with emission-line/photoionisation content supported by the Keynote title. Remove unsupported exact locations and day-level dates except `2026-01-09` and `2026-05-23`, which are source-verified.

- [ ] Rebuild `/talks/` with two sections. Render the first five through `talk-entry.html` under `Oral and invited talks`; explicitly render URSI last under `Related conference output` with no talk/poster label.

- [ ] Make `_layouts/talk.html` a no-sidebar academic detail layout with a single title, metadata line, and body. Change the talks collection default in `_config.yml` from `layout: academic` to `layout: talk`. Update the CV talk include so URSI is described as a proceeding, not a talk.

- [ ] Run tests/build and visually inspect `/talks/` plus all six detail URLs.

- [ ] Commit:

```bash
rtk git add _config.yml _pages/talks.html _layouts/talk.html _talks _includes/archive-single-talk-cv.html _sass/layout/_academic.scss tests/test_site_contract.py
rtk git commit -m "fix: correct talks and conference output"
```

---

### Task 9: Clarify CV, Contact, and the canonical research route

**Files:**

- Modify: `_pages/cv.md`
- Modify: `_pages/contact.md`
- Modify: `_pages/research.md`
- Modify: `_sass/layout/_academic.scss`
- Modify: `tests/test_site_contract.py`

- [ ] Add privacy/identity tests that scan public source pages: email must be `yshiyu@link.cuhk.edu.hk`; phone string and `tel:+85244346668` may occur only in `cv.md` and `contact.md`; no residential-address field may be present.

- [ ] Restyle `/cv/` with the academic layout, a visible `Download CV (PDF)` link, and education rows with primary degree/institution, aligned secondary dates, and subordinate honours. Keep exact confirmed education:

```text
MPhil in Physics · The Chinese University of Hong Kong · Aug 2024–Oct 2026 (expected)
Postgraduate Studentship

BSc in Physics · Sun Yat-sen University · Sep 2020–Jul 2024
GPA 3.9/4.0 (Top 5%) · Outstanding Graduate · Outstanding Graduation Thesis
```

- [ ] Correct the CV Cloudy experience to use the conservative Task 6 conclusion. Keep phone and email. Preserve the existing five project experiences, teaching/leadership, skills, awards, publications, and talks, but use the new compact typography and corrected talk metadata.

- [ ] Keep `/contact/` concise with email, phone, GitHub, LinkedIn, Hong Kong SAR, and the collaboration/PhD/technical-role sentence. Do not add a home address.

- [ ] Replace `_pages/research.md` content with a redirect-only page preserving `/research/`:

```yaml
---
permalink: /research/
redirect_to: /portfolio/
sitemap: false
---
```

If the redirect plugin does not emit a redirect in the current build, use a minimal accessible HTML fallback with a canonical link, meta refresh to `/portfolio/`, and a visible `Continue to Projects` link.

- [ ] Run privacy/content tests and production build. Inspect `/cv/`, `/contact/`, and generated `/research/index.html`.

- [ ] Commit:

```bash
rtk git add _pages/cv.md _pages/contact.md _pages/research.md _sass/layout/_academic.scss tests/test_site_contract.py
rtk git commit -m "feat: clarify cv contact and research route"
```

---

### Task 10: Add generated-site validation and perform full visual QA

**Files:**

- Create: `tests/test_generated_site.py`
- Modify: `_sass/layout/_academic.scss` only if visual defects are found
- Modify: touched templates/content only if a validation defect is found

- [ ] Create `tests/test_generated_site.py` using only `html.parser`, `urllib.parse`, and `pathlib`. Validate generated HTML after `_site` build:

```python
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import unittest


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.images = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        elif tag == "img":
            self.images.append(data)
        elif tag == "a" and data.get("href"):
            self.links.append(data["href"])


class GeneratedSiteTests(unittest.TestCase):
    REQUIRED = (
        "index.html", "portfolio/index.html", "publications/index.html",
        "talks/index.html", "cv/index.html", "contact/index.html",
    )

    def parse(self, relative):
        parser = PageParser()
        parser.feed((SITE / relative).read_text(encoding="utf-8"))
        return parser

    def test_required_pages_have_one_h1_and_all_images_have_alt(self):
        for relative in self.REQUIRED:
            parser = self.parse(relative)
            self.assertEqual(parser.h1_count, 1, relative)
            for image in parser.images:
                self.assertTrue(image.get("alt", "").strip(), (relative, image))

    def test_internal_absolute_links_resolve(self):
        for html in SITE.rglob("*.html"):
            parser = PageParser()
            parser.feed(html.read_text(encoding="utf-8"))
            for href in parser.links:
                parsed = urlparse(href)
                if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
                    continue
                target = SITE / parsed.path.lstrip("/")
                if parsed.path.endswith("/"):
                    target = target / "index.html"
                self.assertTrue(target.exists(), (html.relative_to(SITE), href))


if __name__ == "__main__":
    unittest.main()
```

- [ ] Build from a clean `_site` and run both test modules:

```bash
rtk /opt/homebrew/opt/ruby/bin/bundle exec jekyll clean
rtk env JEKYLL_ENV=production /opt/homebrew/opt/ruby/bin/bundle exec jekyll build
rtk python3 -m unittest discover -s tests -v
```

- [ ] Run stale-claim and privacy searches; all commands must return no unexpected matches:

```bash
rtk rg -n "approximately halved|roughly half|Virtual / International|Conference presentation|to be added|@gmail\.com" _pages _portfolio _publications _talks _includes
rtk rg -n "\+852 4434 6668|tel:\+85244346668" _pages _portfolio _publications _talks _includes
rtk rg -n "theme-toggle|data-theme=|_dark" _layouts _includes assets/css/main.scss assets/js/_main.js
```

Expected phone matches: `_pages/cv.md` and `_pages/contact.md` only. Expected matches for every other search: none.

- [ ] Serve the built site locally and use the in-app browser for visual QA:

```bash
rtk /opt/homebrew/opt/ruby/bin/bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Inspect homepage, Projects, all five project details, Publications, Talks, CV, and Contact at approximately 1440×900, 768×1024, and 390×844. Verify no overlap or horizontal scrolling, the portrait remains prominent, headings are visibly distinct from metadata, figures/captions are legible, links have focus states, and the footer is neutral/compact.

- [ ] Inspect the browser console on representative pages for missing assets, Liquid-generated broken URLs, and JavaScript errors. Confirm `/research/` resolves to `/portfolio/`.

- [ ] Review every title, institution, date, status, and talk type against the approved specification. Review every figure at rendered size for crop, caption, and alt text. Fix defects and rerun build/tests after each fix.

- [ ] Commit the final validation harness and any QA corrections:

```bash
rtk git add tests/test_generated_site.py
# If QA required a correction, inspect `rtk git diff --name-only` and add only each reviewed path explicitly.
rtk git commit -m "test: validate redesigned academic site"
```

- [ ] Confirm the final working tree contains no accidentally staged `.superpowers/`, `_site/`, temporary PDF renders, `node_modules/`, or `package-lock.json`, and report the build/test results without deploying:

```bash
rtk git status --short
rtk git log --oneline -10
```
