import reflex as rx
from ..utils.styles import create_styled_link


def create_list_item_link(link_url, link_text):
    """Create a list item containing a styled link."""
    return rx.el.li(
        create_styled_link(link_url=link_url, link_content=link_text)
    )


# Main navigation menu with logo and links.
def create_navigation_menu():
    """Create the main navigation menu with logo and links."""
    return rx.flex(
        rx.el.a(
            "Víctor Vega",  # Updated name
            href="#",
            transition_duration="300ms",
            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
            font_weight="700",
            _hover={"color": "#60A5FA"},
            font_size="1.5rem",
            line_height="2rem",
            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        ),
        rx.list(
            create_list_item_link(link_url="#home", link_text="Home"),
            create_list_item_link(link_url="#about", link_text="About Me"),
            create_list_item_link(link_url="#projects", link_text="Projects"),
            create_list_item_link(link_url="#blog", link_text="Blog"),
            create_list_item_link(link_url="#contact", link_text="Contact"),
            display="flex",
            column_gap="1.5rem",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )
