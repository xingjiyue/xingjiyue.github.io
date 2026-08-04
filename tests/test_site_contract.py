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


class HomepageContractTests(unittest.TestCase):
    def test_homepage_uses_academic_hero_and_three_paper_rows(self):
        homepage = read("_pages/about.md")
        self.assertIn("layout: academic", homepage)
        self.assertIn("hide_title: true", homepage)
        self.assertIn("/images/photo.jpg", homepage)
        self.assertIn("Aug 2024–Oct 2026 (expected)", homepage)
        self.assertIn("Sep 2020–Jul 2024", homepage)
        self.assertIn("yshiyu@link.cuhk.edu.hk", homepage)
        self.assertEqual(homepage.count("include academic/paper-row.html"), 3)

    def test_homepage_omits_private_or_redundant_content(self):
        homepage = read("_pages/about.md")
        self.assertNotIn("+852 4434 6668", homepage)
        self.assertNotIn("## Research interests", homepage)
        self.assertNotIn("approximately halved", homepage)


class PortfolioContractTests(unittest.TestCase):
    REQUIRED_KEYS = (
        "title",
        "category",
        "institution",
        "role",
        "period",
        "status",
        "research_question",
        "built",
        "validation",
        "result",
        "thumbnail",
        "thumbnail_alt",
        "figures",
    )

    def test_all_projects_have_structured_metadata(self):
        projects = sorted((ROOT / "_portfolio").glob("*.md"))
        self.assertEqual(len(projects), 5)
        for path in projects:
            source = path.read_text(encoding="utf-8")
            front_matter = source.split("---", 2)[1]
            for key in self.REQUIRED_KEYS:
                self.assertRegex(front_matter, rf"(?m)^{key}:", (path.name, key))

    def test_paper_projects_have_two_figures_and_other_projects_have_one(self):
        expected = {
            "2024-08-01-cloudy-manga.md": 2,
            "2024-10-01-3pcf-fast-algorithm.md": 2,
            "2024-12-01-frdeep-xai.md": 2,
            "2025-03-01-cspn-multimodal.md": 1,
            "2026-05-01-ai-workflow-automation.md": 1,
        }
        for filename, count in expected.items():
            source = read(f"_portfolio/{filename}")
            front_matter = source.split("---", 2)[1]
            self.assertEqual(front_matter.count("  - src:"), count, filename)

    def test_projects_page_renders_four_research_and_one_engineering_summary(self):
        landing = read("_pages/portfolio.html")
        self.assertIn("Research Projects", landing)
        self.assertIn("Engineering Project", landing)
        self.assertEqual(landing.count("include academic/project-summary.html"), 5)


class ProjectDetailContractTests(unittest.TestCase):
    EXPECTED_HEADINGS = (
        "Research question",
        "My role",
        "At a glance",
        "What I built",
        "Method",
        "Validation",
        "Results",
        "Outputs",
    )

    def test_all_project_details_use_the_same_heading_order(self):
        for path in sorted((ROOT / "_portfolio").glob("*.md")):
            body = path.read_text(encoding="utf-8").split("---", 2)[2]
            headings = tuple(re.findall(r"(?m)^## (.+)$", body))
            self.assertEqual(headings, self.EXPECTED_HEADINGS, path.name)

    def test_each_project_renders_every_declared_figure(self):
        expected = {
            "2024-08-01-cloudy-manga.md": 2,
            "2024-10-01-3pcf-fast-algorithm.md": 2,
            "2024-12-01-frdeep-xai.md": 2,
            "2025-03-01-cspn-multimodal.md": 1,
            "2026-05-01-ai-workflow-automation.md": 1,
        }
        for filename, count in expected.items():
            body = read(f"_portfolio/{filename}").split("---", 2)[2]
            self.assertEqual(body.count("include academic/figure.html"), count, filename)

    def test_stale_project_claims_are_removed(self):
        source = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "_portfolio").glob("*.md"))
        self.assertNotIn("approximately halved", source)
        self.assertNotIn("reduces this discrepancy by roughly half", source)
        self.assertNotIn("ongoing IPHAS", source)


class PublicationContractTests(unittest.TestCase):
    REQUIRED_KEYS = (
        "title",
        "citation",
        "publication_status",
        "display_status",
        "contribution",
        "project_url",
        "thumbnail",
        "thumbnail_alt",
    )

    def test_publications_have_scan_first_metadata(self):
        publications = sorted((ROOT / "_publications").glob("*.md"))
        self.assertEqual(len(publications), 4)
        for path in publications:
            front_matter = path.read_text(encoding="utf-8").split("---", 2)[1]
            for key in self.REQUIRED_KEYS:
                self.assertRegex(front_matter, rf"(?m)^{key}:", (path.name, key))

    def test_only_verified_public_outputs_have_paper_urls(self):
        with_urls = {
            path.name
            for path in (ROOT / "_publications").glob("*.md")
            if re.search(r"(?m)^paperurl:", path.read_text(encoding="utf-8").split("---", 2)[1])
        }
        self.assertEqual(
            with_urls,
            {
                "2023-08-01-local-interpretation-radio-galaxy.md",
                "2024-12-01-pair-counting-without-binning.md",
            },
        )

    def test_publication_copy_has_no_placeholders_or_stale_claims(self):
        source = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "_publications").glob("*.md"))
        self.assertNotIn("to be added", source)
        self.assertNotIn("approximately halved", source)
        self.assertNotIn("Presented results", source)

    def test_publications_page_renders_all_four_rows(self):
        landing = read("_pages/publications.html")
        self.assertEqual(landing.count("include academic/paper-row.html"), 4)


if __name__ == "__main__":
    unittest.main()
