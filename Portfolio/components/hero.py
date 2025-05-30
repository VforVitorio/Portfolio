import reflex as rx
from ..utils.styles import create_paragraph, create_icon

# Directly defined constants in the file
LINKEDIN_URL = "https://www.linkedin.com/in/victorvegasobral/"
GITHUB_URL = "https://github.com/VforVitorio"
# Assume you want this name here as well
SITE_NAME = "Hello! I´m Víctor Vega Sobral"
AVATAR_URL = "https://avatars.githubusercontent.com/VforVitorio"


def create_social_icon_link(icon_alt, icon_tag, href):
    """Create a social media icon link with hover effects."""
    return rx.el.a(
        create_icon(
            alt_text=icon_alt,
            icon_height="1.5rem",
            icon_tag=icon_tag,
            icon_width="1.5rem",
        ),
        class_name="transform",
        href=href,
        is_external=True,  # Open in a new tab
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        _hover={
            "transform": "scale(1.1)",
            "color": "#93C5FD",
        },
        color="#60A5FA",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )


def create_profile_image():
    """Create a circular profile image with hover effect."""
    return rx.image(
        alt=SITE_NAME,  # Use SITE_NAME for alt text
        class_name="transform",
        src=AVATAR_URL,  # Use the new AVATAR_URL
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        height="16rem",
        _hover={"transform": "scale(1.05)"},
        margin_right="2rem",
        object_fit="cover",
        border_radius="9999px",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        width="16rem",
    )


def create_bio_section():
    """Create a biographical section with name, title, description, and social links."""
    return rx.box(
        rx.heading(
            SITE_NAME,  # Use SITE_NAME for the name
            font_weight="700",
            margin_bottom="1rem",
            font_size="2.25rem",
            line_height="2.5rem",
            as_="h1",
        ),
        rx.text(
            "AI & Intelligent Systems Software Engineer",
            margin_bottom="1.5rem",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        create_paragraph(
            margin_bottom="1.5rem",
            paragraph_text="4th-year Intelligent Systems Engineering student at UIE Campus Coruña and AI Software Engineer: I design and deploy AI solutions for highly complex, data-driven environments, and I’m passionate about applying AI to Formula 1.",
        ),
        rx.flex(
            create_social_icon_link(
                icon_alt="GitHub", icon_tag="github", href=GITHUB_URL),  # Use GITHUB_URL
            create_social_icon_link(
                icon_alt="LinkedIn", icon_tag="linkedin", href=LINKEDIN_URL),  # Use LINKEDIN_URL
            # create_social_icon_link(icon_alt="Twitter", icon_tag="twitter", href="https://x.com/harimkang"),
            display="flex",
            column_gap="1rem",
        ),
    )


def create_hero_section():
    """Create the hero section with profile image and bio."""
    return rx.box(
        rx.flex(
            create_profile_image(),
            create_bio_section(),
            custom_attrs={
                "data-aos": "fade-up",
                "data-aos-duration": "1000",
            },
            display="flex",
            align_items="center",
        ),
        id="home",
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
        padding_top="4rem",
        padding_bottom="4rem",
    )
