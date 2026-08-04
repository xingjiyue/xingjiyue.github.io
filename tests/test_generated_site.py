from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import unittest


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.images = []
        self.links = []
        self.figure_count = 0
        self.figcaption_count = 0

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        elif tag == "img":
            self.images.append(data)
        elif tag == "a" and data.get("href"):
            self.links.append(data["href"])
        elif tag == "figure":
            self.figure_count += 1
        elif tag == "figcaption":
            self.figcaption_count += 1


def parse(relative: str) -> PageParser:
    parser = PageParser()
    parser.feed((SITE / relative).read_text(encoding="utf-8"))
    return parser


def internal_target_exists(path: str) -> bool:
    clean = unquote(path).lstrip("/")
    target = SITE / clean
    candidates = [target]
    if path.endswith("/"):
        candidates.append(target / "index.html")
    elif not target.suffix:
        candidates.extend((target.with_suffix(".html"), target / "index.html"))
    return any(candidate.exists() for candidate in candidates)


class GeneratedSiteTests(unittest.TestCase):
    REQUIRED = (
        "index.html",
        "portfolio/index.html",
        "publications/index.html",
        "talks/index.html",
        "cv/index.html",
        "contact/index.html",
    )

    PROJECTS = (
        "portfolio/2024-08-01-cloudy-manga/index.html",
        "portfolio/2024-10-01-3pcf-fast-algorithm/index.html",
        "portfolio/2024-12-01-frdeep-xai/index.html",
        "portfolio/2025-03-01-cspn-multimodal/index.html",
        "portfolio/2026-05-01-ai-workflow-automation/index.html",
    )

    def test_required_pages_have_one_h1_and_all_images_have_alt(self):
        for relative in self.REQUIRED + self.PROJECTS:
            parser = parse(relative)
            self.assertEqual(parser.h1_count, 1, relative)
            for image in parser.images:
                self.assertTrue(image.get("alt", "").strip(), (relative, image))

    def test_project_figures_all_have_visible_captions(self):
        for relative in self.PROJECTS:
            parser = parse(relative)
            self.assertGreaterEqual(parser.figure_count, 1, relative)
            self.assertEqual(parser.figure_count, parser.figcaption_count, relative)

    def test_internal_absolute_links_resolve(self):
        failures = []
        for html in SITE.rglob("*.html"):
            parser = PageParser()
            parser.feed(html.read_text(encoding="utf-8"))
            for href in parser.links:
                parsed = urlparse(href)
                if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
                    continue
                if not internal_target_exists(parsed.path):
                    failures.append((html.relative_to(SITE).as_posix(), href))
        self.assertEqual(failures, [])

    def test_primary_pages_have_no_sidebar_or_theme_toggle(self):
        for relative in self.REQUIRED:
            source = (SITE / relative).read_text(encoding="utf-8")
            self.assertNotIn('id="theme-toggle"', source, relative)
            self.assertNotIn('class="sidebar', source, relative)


if __name__ == "__main__":
    unittest.main()
