import reflex as rx
from ..utils.styles import create_styled_heading

# Directly defined constants in the file
LINKEDIN_URL = "https://www.linkedin.com/in/victorvegasobral/"
GITHUB_URL = "https://github.com/VforVitorio"
# EMAIL_ADDRESS = "your_email@example.com" # Uncomment and update if you want to use a constant for the email


def create_logo_image(alt_text, image_src):
    """Create a logo image with specified dimensions and alt text."""
    return rx.image(
        alt=alt_text,
        src=image_src,
        height="3rem",
        margin_right="1rem",
        object_fit="contain",
        width="3rem",
    )


def create_subheading(content):
    """Create a subheading with custom styling."""
    return rx.heading(
        content,
        font_weight="600",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h4",
    )


def create_info_box(title, subtitle, description):
    """Create an information box with title, subtitle, and description."""
    return rx.box(
        create_subheading(content=title),
        rx.text(subtitle, color="#60A5FA"),
        rx.text(description)
    )


def create_skill_item(icon_src: str, skill_text: str):
    """Create a skill item with an icon and text."""
    return rx.hstack(
        rx.image(
            src=icon_src,
            height="1.5rem",
            width="1.5rem",
            object_fit="contain",
            alt=f"{skill_text} icon",
        ),
        rx.text(skill_text),
        spacing="3",
        align_items="center",
    )


def highlight_text(text: str) -> str:
    """Add color spans to highlighted keywords."""
    keywords = {
        "Python": "rgb(96, 165, 250)",
        "PyTorch": "rgb(239, 68, 68)",
        "TensorFlow": "rgb(255, 128, 0)",
        "Deep Learning": "rgb(139, 92, 246)",
        "AI": "rgb(0, 150, 150)",
        "Intelligent Systems Engineering": "rgb(45, 155, 245)",
        "Engineering Summer Programme alumnus at Girton College, Cambridge University": "rgb(0, 84, 166)",
        "IELTS 8": "rgb(0, 84, 166)",
        "F1": "rgb(255, 0, 0)",
    }

    for keyword, color in keywords.items():
        text = text.replace(
            keyword,
            f'<span style="color: {color}; font-weight: 600;">{keyword}</span>'
        )
    return text


def create_about_summary():
    """Create the professional summary and expertise section for the About Me page."""
    return rx.box(
        create_styled_heading(
            font_size="1.5rem",
            line_height="2rem",
            heading_text="Professional Summary",
        ),
        rx.html(
            highlight_text(
                "4th-year Intelligent Systems Engineering student at UIE Coruña, Engineering Summer Programme alumnus at Girton College, Cambridge University (2023), and Deep Learning Specialization by DeepLearning.AI. Passionate about applying AI (Deep Learning, NLP, expert systems, predictive modeling) to optimize F1 race strategies. Developing an integrated F1 Strategy Assistant and open to collaborations with racing teams and AI innovators."
            ),
            margin_bottom="1rem",
        ),
        rx.heading(
            "Skills & Tools",
            font_weight="600",
            margin_bottom="1rem",
            margin_top="1.5rem",
            font_size="1.5rem",
            line_height="2rem",
            as_="h3",
        ),
        rx.box(
            rx.vstack(
                create_skill_item(
                    "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
                    "Python"
                ),
                create_skill_item(
                    "https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg",
                    "Pandas"
                ),
                create_skill_item(
                    "https://raw.githubusercontent.com/devicons/devicon/master/icons/streamlit/streamlit-original.svg",
                    "Streamlit"
                ),
                create_skill_item(
                    # PyTorch has its own icon in devicons
                    "https://raw.githubusercontent.com/devicons/devicon/master/icons/pytorch/pytorch-original.svg",
                    "PyTorch"
                ),
                create_skill_item(
                    "https://raw.githubusercontent.com/devicons/devicon/master/icons/tensorflow/tensorflow-original.svg",
                    "TensorFlow"
                ),
                create_skill_item(
                    "https://cdn-lfs.hf.co/repos/96/a2/96a2c8468c1546e660ac2609e49404b8588fcf5a748761fa72c154b2836b4c83/e24efa64f0482c4484c47bf9394e8b46182a2a3b66fd017c9293bef8754abb66?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27hf-logo.svg%3B+filename%3D\"hf-logo.svg\"%3B&response-content-type=image%2Fsvg%2Bxml&Expires=1747937607&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzkzNzYwN319LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5oZi5jby9yZXBvcy85Ni9hMi85NmEyYzg0NjhjMTU0NmU2NjBhYzI2MDllNDk0MDRiODU4OGZjZjVhNzQ4NzYxZmE3MmMxNTRiMjgzNmI0YzgzL2UyNGVmYTY0ZjA0ODJjNDQ4NGM0N2JmOTM5NGU4YjQ2MTgyYTJhM2I2NmZkMDE3YzkyOTNiZWY4NzU0YWJiNjY~cmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qJnJlc3BvbnNlLWNvbnRlbnQtdHlwZT0qIn1dfQ__&Signature=MgItVMuikszf4ww~X3GtsHeEoUVBWY0NwoUgAOagD0FDOyw-oHTPvFDduefLOM5jajmdTftNkYU5-aScHX67JIWJJzt0ZRNGGKQy4PnmE8SGwCt75VEgbkLl8rHssDaTenF4RzpfTuzZ8ePHgAooBhUo4vf6uQIilBSwNVmV2OD9llNDyWfAv5S9jeUmoC6mmaneqJABrx2z8vPY5E3XjDBMU2aF6fvt3f1Xy2Th3Covg-3Le8Rt2~VKWVUOxxqAXRojPen5QlVb~mY~G--hAyMc88MaGnoC9GlDS1HOGtLn9PsiRVTGsQCUxjRlrT4JN2WVcJWQoYhAp5zS3~BaPA__&Key-Pair-Id=K3RPWS32NSSJCE",
                    "Hugging Face"
                ),
                create_skill_item(
                    "https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg",
                    "Git | GitHub"
                ),
                create_skill_item(
                    "https://cdn-icons-png.flaticon.com/512/2103/2103633.png",  # Existing icon for DL/AI
                    "Deep Learning | AI"
                ),
                create_skill_item(
                    # Existing icon for languages
                    "https://cdn-icons-png.flaticon.com/512/484/484633.png",
                    "Spanish: Native | English: IELTS 8"
                ),
                align_items="start",
                spacing="3",
                width="100%",
            ),
        ),
        rx.divider(
            margin_y="2rem",
            opacity="0.2",
        ),
        custom_attrs={
            "data-aos": "fade-up",
            "data-aos-delay": "200",
        },
    )


def create_work_experience():
    """Create the work experience section with multiple job entries."""
    return rx.box(
        rx.text("While I haven't had formal work experience yet, I have worked on several hands-on projects that reflect my abilities."),
        rx.text("Open to opportunities in Formula 1 and beyond with companies developing innovative AI solutions for complex problem-solving environments."),
        display="flex",
        flex_direction="column",
        gap="1.5rem",
    )


def create_education():
    return rx.box(
        rx.flex(
            create_logo_image(
                alt_text="UIE Logo",  # Updated
                # Generic logo URL, update if a specific one is available
                image_src="https://www.afundacion.org/images/fundacion_publicaciones/LOGO_UIE_CUADRADO-01.jpg",
            ),
            create_info_box(
                title="UIE, Universidad Intercontinental de la Empresa",  # Updated
                subtitle="Fourth-year student of Intelligent Systems Engineering.",  # Updated
                description="A Coruña Campus.",  # Updated
            ),
            display="flex",
            align_items="flex-start",
        ),
        display="flex",
        flex_direction="column",
        gap="1.5rem",
    )


def create_section_heading(heading_text):
    """Create a section heading with fade-in animation."""
    return rx.heading(
        heading_text,
        custom_attrs={"data-aos": "fade-right"},
        font_weight="700",
        margin_bottom="2rem",
        font_size="1.875rem",
        line_height="2.25rem",
        as_="h2",
    )


def create_list_item(item_text):
    """Create a simple list item."""
    return rx.el.li(item_text)


def create_about_section():
    """Create the 'About Me' section with expertise and professional journey."""
    return rx.box(
        create_section_heading(heading_text="About Me"),
        rx.box(
            create_about_summary(),
            rx.box(
                create_styled_heading(
                    font_size="1.5rem",
                    line_height="2rem",
                    heading_text="Work Experience",
                ),
                create_work_experience(),
                create_styled_heading(
                    font_size="1.5rem",
                    margin_top="2rem",
                    line_height="2rem",
                    heading_text="Education",
                ),
                create_education(),
                custom_attrs={
                    "data-aos": "fade-up",
                    "data-aos-delay": "400",
                },
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
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
    )
