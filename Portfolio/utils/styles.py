import reflex as rx
from enum import Enum

# Contenido de styles/colors.py


class Color(Enum):
    """Colores principales de la aplicación."""
    ACCENT = "#a78bfa"
    PRIMARY_BG = "#121127"
    SECONDARY_BG = "#1e1b4b"
    CONTENT_BG = "#181633"
    BORDER = "#2d2d3a"


class TextColor(Enum):
    """Colores de texto."""
    PRIMARY = "#ffffff"
    SECONDARY = "#d1d5db"
    TERTIARY = "#9ca3af"
    ACCENT = "#a78bfa"
    AGAINST_ACCENT = "#ffffff"


class GradientColor(Enum):
    """Colores para gradientes."""
    NAVBAR_START = Color.PRIMARY_BG.value
    NAVBAR_END = Color.SECONDARY_BG.value
    LOGO_TEXT_START = Color.ACCENT.value
    LOGO_TEXT_END = TextColor.PRIMARY.value


class StatusColor(Enum):
    SUCCESS = "#10b981"
    WARNING = "#f59e0b"
    ERROR = "#ef4444"
    INFO = "#3b82f6"

# Contenido de styles/fonts.py


class Font(Enum):
    DEFAULT = "'Inter', sans-serif"
    TITLE = "'Exo 2', sans-serif"
    LOGO = "'Exo 2', sans-serif"


# Contenido de styles/styles.py (parcial)
MAX_WIDTH = "1200px"


class Size(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "2"
    MEDIUM = "3"
    DEFAULT = "4"
    LARGE = "6"
    BIG = "7"
    VERY_BIG = "9"


class FontSize(Enum):
    SMALL = "2"
    MEDIUM = "3"
    LARGE = "4"
    XLARGE = "7"
    XXLARGE = "8"
    VERY_BIG = "9"
    LOGO = "28px"


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Exo+2:wght@400;700&family=Inter:wght@400;500;700&display=swap",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_size": FontSize.MEDIUM.value,
    "color": TextColor.PRIMARY.value,
    "background_color": Color.PRIMARY_BG.value,
    "line_height": "1.6",
    rx.heading: {
        "font_family": Font.TITLE.value,
        "font_weight": "700",
        "color": TextColor.ACCENT.value,
    },
    rx.link: {
        "text_decoration": "none",
        "color": TextColor.SECONDARY.value,
        "_hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none"
        }
    },
    rx.text: {
        "font_family": Font.DEFAULT.value,
        "color": TextColor.SECONDARY.value,
    },
    rx.button: {
        "font_family": Font.DEFAULT.value,
        "font_weight": "500",
        "padding_x": Size.DEFAULT.value,
        "padding_y": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
        "background_color": Color.ACCENT.value,
        "color": TextColor.AGAINST_ACCENT.value,
        "_hover": {
            "opacity": "0.9",
        }
    },
    ".page-container": {
        "padding_top": Size.VERY_BIG.value,
        "padding_bottom": Size.VERY_BIG.value,
        "width": "100%",
        "max_width": MAX_WIDTH,
        "margin_x": "auto",
        "padding_x": Size.BIG.value,
    }
}


def load_script(script_source):
    """Load a script from the given source URL."""
    return rx.script(src=script_source)


def create_styled_link(link_url, link_content):
    """Create a styled anchor element with hover effects and transitions."""
    return rx.el.a(
        link_content,
        href=link_url,
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        color=TextColor.SECONDARY.value,  # Usar TextColor
        _hover={"color": TextColor.ACCENT.value},  # Usar TextColor
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )


def create_styled_heading(font_size, line_height, heading_text, **kwargs):
    """Create a styled heading with customizable font size and line height."""
    return rx.heading(
        heading_text,
        font_family=Font.TITLE.value,  # Usar Font
        font_weight="600",  # Mantener o ajustar según BASE_STYLE
        margin_bottom="1rem",  # Puede ser reemplazado por Size
        font_size=font_size,  # Puede ser reemplazado por FontSize
        line_height=line_height,
        color=TextColor.ACCENT.value,  # Usar TextColor
        as_="h3",
        **kwargs
    )


def create_paragraph(margin_bottom, paragraph_text, **kwargs):
    """Create a paragraph with a specified bottom margin."""
    return rx.text(
        paragraph_text,
        font_family=Font.DEFAULT.value,  # Usar Font
        color=TextColor.SECONDARY.value,  # Usar TextColor
        margin_bottom=margin_bottom,  # Puede ser reemplazado por Size
        **kwargs
    )


def create_text(text_content):
    """Create a simple text element."""
    return rx.text(text_content)


def create_icon(alt_text, icon_height, icon_tag, icon_width):
    """Create an icon with specified dimensions and alt text."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height=icon_height,
        display="inline",
        width=icon_width,
    )


def create_section_heading(heading_text: str, text_align: str = "left"):
    """Create a section heading with fade-in animation."""
    return rx.heading(
        heading_text,
        custom_attrs={"data-aos": "fade-right"},
        font_family=Font.TITLE.value,
        font_weight="700",
        margin_bottom="3rem",
        font_size=FontSize.XLARGE.value,
        line_height="2.25rem",
        color=TextColor.ACCENT.value,
        as_="h2",
        text_align=text_align,
    )


def create_link_with_icon(link_text, icon_alt, icon_tag, href, is_external: bool = False):
    """Create a link with an icon and hover effects."""
    return rx.link(
        link_text,
        create_icon(
            alt_text=icon_alt,
            icon_height="1rem",  # Puede ser reemplazado por Size
            icon_tag=icon_tag,
            icon_width="1rem",  # Puede ser reemplazado por Size
        ),
        href=href,
        is_external=is_external,  # Añadido el argumento is_external
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        _hover={"color": TextColor.ACCENT.value},  # Usar TextColor
        color=TextColor.SECONDARY.value,  # Usar TextColor
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )
