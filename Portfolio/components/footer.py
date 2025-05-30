import reflex as rx
from ..utils.styles import create_text

# Create the footer with copyright information.


def create_footer():
    """Create the footer with copyright information."""
    return rx.box(
        rx.box(
            create_text(
                text_content="© 2025 Harim Kang. All rights reserved."
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
            text_align="center",
        ),
        background_color="#1F2937",
        padding_top="2rem",
        padding_bottom="2rem",
    )
