import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH = "1000px"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    MEDIUM = "3"
    DEFAULT = "4"
    BIG = "8"
    BUTTON = "11"
    VERY_BIG = "16"


STYLESHEETS = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css",
    "https://fonts.googleapis.com/css?family=Inter&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,

    rx.heading: {
        "font_family": Font.DEFAULT.value,
        "color": TextColor.ACCENT.value,
    },

    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none"
        }
    },

    rx.text.span: {
        "font_size": Size.MEDIUM.value
    },

    rx.button: {
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BUTTON.value,
        "color": TextColor.PRIMARY.value,
        "_hover": {
            "color": TextColor.TERTIARY.value
        }
    }
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)
