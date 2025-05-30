import reflex as rx
from ..utils.styles import (
    create_styled_heading,
    create_paragraph,
    create_section_heading,
    create_link_with_icon
)


# Create the 'Blog' section linking to Medium profile.
def create_blog_section():
    """Create the 'Blog' section linking to Medium profile."""
    return rx.box(
        create_section_heading(heading_text="Blog - Articles on Medium"),
        rx.vstack(
            create_paragraph(
                paragraph_text="Although I haven’t published any articles here yet, I’m gearing up to launch a series on Medium. My work delves into the cutting-edge intersection of Formula 1 and Artificial Intelligence, examining how AI-driven insights can transform race strategies, optimize performance, and elevate the fan experience in this exhilarating sport.",
                margin_bottom="1rem"  # Added the margin_bottom argument
            ),
            create_link_with_icon(
                link_text="Visit my Medium profile",
                icon_alt="Medium Logo",  # Or a more generic icon if you don't have the Medium logo
                icon_tag="external-link",  # Or an appropriate icon tag
                href="https://medium.com/@VforVitorio",
                is_external=True  # To open in a new tab
            ),
            spacing="4",
            align_items="start",
            width="100%",
        ),
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
        id="blog",  # Add ID if you are going to link from navigation
    )
