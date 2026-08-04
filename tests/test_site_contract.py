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
            "education-row.html",
            "news-row.html",
            "paper-row.html",
            "project-summary.html",
            "talk-entry.html",
        ):
            self.assertTrue((ROOT / "_includes" / "academic" / name).is_file())


class ProjectFigureContractTests(unittest.TestCase):
    FIGURES = (
        "3pcf-method.png",
        "3pcf-validation.png",
        "frdeep-method.png",
        "frdeep-results.png",
        "siii-method.png",
        "siii-results.png",
        "cspn-workflow.svg",
        "ai-workflow.svg",
    )

    def test_project_figure_manifest(self):
        for name in self.FIGURES:
            path = ROOT / "images" / "projects" / name
            self.assertTrue(path.is_file(), name)
            self.assertGreater(path.stat().st_size, 200, name)
            if path.suffix == ".png":
                self.assertEqual(path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")

    def test_project_sources_do_not_reference_temporary_directories(self):
        for path in (ROOT / "_portfolio").glob("*.md"):
            source = path.read_text(encoding="utf-8")
            for temporary in ("tmp/", "_site/", ".superpowers/"):
                self.assertNotIn(temporary, source, path.name)


if __name__ == "__main__":
    unittest.main()
