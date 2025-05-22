from enum import Enum


class Color(Enum):
    ACCENT = "#6366f1"      # Vibrant purple for buttons and highlights
    PRIMARY = "#0f0f23"     # Very dark purple/black as main background
    SECONDARY = "#1a1a2e"   # Dark purple-gray for secondary elements/cards
    TERTIARY = "#2d2d3a"    # Medium purple-gray for borders/dividers


class TextColor(Enum):
    ACCENT = "#8b5cf6"      # Light purple for highlighted/important text
    PRIMARY = "#ffffff"     # White for main text
    SECONDARY = "#a1a1aa"   # Light gray for secondary text/descriptions
    TERTIARY = "#6b6b6b"    # Dark gray for subtle text elements

# Additional colors for the portfolio theme


class GradientColor(Enum):
    PURPLE_START = "#6366f1"    # Gradient start
    PURPLE_END = "#8b5cf6"      # Gradient end
    BACKGROUND_OVERLAY = "rgba(15, 15, 35, 0.95)"  # Semi-transparent overlay


class StatusColor(Enum):
    SUCCESS = "#10b981"     # Green for success states
    WARNING = "#f59e0b"     # Amber for warnings
    ERROR = "#ef4444"       # Red for errors
    INFO = "#3b82f6"        # Blue for info
