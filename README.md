# Shiyu Yue — Academic Personal Website

Source for [xingjiyue.github.io](https://xingjiyue.github.io), built with [Academic Pages](https://github.com/academicpages/academicpages.github.io) (Jekyll + GitHub Pages).

## Editing

### Content files

All personal content is in Markdown files with YAML front matter:

| Directory | What to edit |
|---|---|
| `_config.yml` | Site name, URL, sidebar author info, social links |
| `_data/navigation.yml` | Top menu bar links and order |
| `_pages/about.md` | Homepage content |
| `_pages/cv.md` | CV page (includes auto-generated publication/talk lists) |
| `_portfolio/` | One `.md` file per project |
| `_publications/` | One `.md` file per publication |
| `_talks/` | One `.md` file per talk or presentation |
| `files/` | PDFs and other downloadable assets |
| `images/profile.png` | Sidebar profile photo (250×250 px recommended) |

## Building locally

Requires Ruby ≥ 2.7 and Bundler.

```bash
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000` to preview. The site rebuilds automatically on file changes.

## Deploying

Push to the `main` branch of `xingjiyue/xingjiyue.github.io`. GitHub Pages builds and deploys automatically.

## Based on

[Academic Pages](https://github.com/academicpages/academicpages.github.io), a Jekyll template forked from [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/).
