import reflex as rx
from ..components.navigation import create_navigation_menu
from ..components.hero import create_hero_section
from ..components.about import create_about_section
from ..components.projects import create_projects_section
from ..components.blog import create_blog_section
from ..components.contact import create_contact_section
from ..components.footer import create_footer
from ..utils.styles import load_script


# Create the main content of the page, including all sections.
def create_main_content():
    """Create the main content of the page, including all sections."""
    return rx.box(
        create_hero_section(),
        rx.box(
            create_about_section(),
            id="about",
            background_color="#1F2937",
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        create_projects_section(),
        rx.box(
            create_blog_section(),
            id="blog",
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        rx.box(
            create_contact_section(),
            id="contact",
            background_color="#1F2937",
            padding_top="1rem",
            padding_bottom="1rem",
        ),
    )


# Render the complete portfolio page with all necessary scripts and styles.
def index() -> rx.Component:
    """Render the complete portfolio page with all necessary scripts and styles."""
    return rx.box(
        rx.box(
            create_navigation_menu(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1rem",
            padding_right="1rem",
            padding_top="2rem",
            padding_bottom="2rem",
        ),
        create_main_content(),
        background_color="#111827",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        color="#F3F4F6",
    )
