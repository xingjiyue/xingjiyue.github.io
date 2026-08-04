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
