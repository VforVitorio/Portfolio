import reflex as rx
from ..utils.styles import (
    create_styled_heading,
    create_paragraph,
    create_section_heading,
    create_link_with_icon
)
from ..state.project_state import ProjectState


def create_technologies_label():
    """Create a 'Technologies:' label in strong text."""
    return rx.text.strong("Technologies:")


def create_technologies_section(technologies):
    """Create a section displaying technologies used."""
    return rx.text(
        create_technologies_label(),
        technologies,
        margin_bottom="0.5rem",
    )


def create_project_details(project_id: str, project_details: dict = None):
    """Create the detailed content section of a project."""
    if project_details is None:
        project_details = {
            "detailed_description": "",
            "key_features": [],
            "development_contributions": [],
            "research_contributions": [],
            "image": None,
            "research_image": None,
        }

    return rx.vstack(
        # Project Details with Image
        rx.hstack(
            rx.box(
                create_styled_heading(
                    font_size="1.5rem",
                    line_height="2rem",
                    heading_text="Project Details",
                ),
                create_paragraph(
                    margin_bottom="1.5rem",
                    paragraph_text=project_details.get(
                        "detailed_description", ""),
                ),
                flex="1",
            ),
            rx.cond(
                project_details.get("image") is not None,
                rx.image(
                    src=project_details.get("image"),
                    alt="Project visualization",
                    height="auto",
                    min_height="200px",
                    max_height="400px",
                    width="40%",
                    max_width="600px",
                    object_fit="contain",
                    border_radius="0.5rem",
                ),
            ),
            width="100%",
            spacing="4",
            align_items="center",
        ),

        # Key Features
        rx.box(
            rx.text.strong("Key Features:", font_size="1.2rem"),
            rx.unordered_list(
                *[rx.list_item(feature)
                  for feature in project_details.get("key_features", [])],
                padding_left="1.5rem",
                margin_top="0.5rem",
                margin_bottom="1.5rem",
            ),
        ),

        # Development Highlights
        rx.box(
            rx.text.strong("Development Key Contributions:",
                           font_size="1.2rem"),
            rx.unordered_list(
                *[rx.list_item(highlight)
                  for highlight in project_details.get("development_contributions", [])],
                padding_left="1.5rem",
                margin_top="0.5rem",
                margin_bottom="1.5rem",
            ),
        ),

        # Research Contributions with Image
        rx.box(
            rx.text.strong("Research Contributions:", font_size="1.2rem"),
            rx.hstack(
                rx.box(
                    rx.unordered_list(
                        *[rx.list_item(contribution)
                          for contribution in project_details.get("research_contributions", [])],
                        padding_left="1.5rem",
                        margin_top="0.5rem",
                        margin_bottom="1.5rem",
                    ),
                    flex="1",
                ),
                rx.cond(
                    project_details.get("research_image") is not None,
                    rx.image(
                        src=project_details.get("research_image"),
                        alt="Research visualization",
                        height="auto",
                        min_height="200px",
                        max_height="400px",
                        width="40%",
                        max_width="600px",
                        object_fit="contain",
                        border_radius="0.5rem",
                    ),
                ),
                width="100%",
                spacing="4",
                align_items="center",
            ),
        ),
        align_items="start",
        width="100%",
        spacing="4",
        id=f"project-{project_id}-details",
        display=rx.cond(
            ProjectState.selected_project == project_id,
            "block",
            "none"
        ),
    )


def create_project_card(
    animation_attrs,
    project_id: str,
    project_title: str,
    project_description: str,
    technologies_used: str,
    href: str,
    project_details: dict = None,
    link_text="GitHub Repository "
):
    """Create an expandable project card."""
    return rx.box(
        rx.vstack(
            rx.box(
                create_styled_heading(
                    font_size="1.25rem",
                    line_height="1.75rem",
                    heading_text=project_title,
                ),
                create_paragraph(
                    margin_bottom="1rem",
                    paragraph_text=project_description,
                ),
                create_technologies_section(technologies=technologies_used),
            ),
            rx.spacer(),
            rx.vstack(
                create_link_with_icon(
                    link_text=link_text,
                    icon_alt="External Link",
                    icon_tag="external-link",
                    href=href,
                ),
                rx.button(
                    rx.hstack(
                        rx.cond(
                            ProjectState.selected_project == project_id,
                            rx.icon(tag="chevron-up"),
                            rx.icon(tag="info"),
                        ),
                        rx.text(
                            rx.cond(
                                ProjectState.selected_project == project_id,
                                "Show Less",
                                "View Details",
                            )
                        ),
                    ),
                    on_click=ProjectState.toggle_project(project_id),
                    background_color="#1F2937",
                    color="white",
                    padding="0.5rem 1rem",
                    border_radius="0.375rem",
                    border="1px solid rgba(99, 102, 241, 0.2)",
                    _hover={
                        "background_color": "rgba(99, 102, 241, 0.1)",
                        "border_color": "rgba(99, 102, 241, 0.5)",
                    },
                ),
                spacing="3",
                align_items="start",
                width="100%",
            ),
            rx.cond(
                ProjectState.selected_project == project_id,
                rx.divider(margin_y="1.5rem"),
            ),
            rx.cond(
                (ProjectState.selected_project == project_id) & (
                    project_details is not None),
                create_project_details(project_id, project_details),
            ),
            height="100%",
            spacing="4",
        ),
        class_name="transform",
        custom_attrs=animation_attrs,
        background_color="#1F2937",
        transition="all 0.3s ease-in-out",
        _hover={"transform": rx.cond(
            ProjectState.selected_project != project_id,
            "scale(1.05)",
            "none"
        )},
        padding="1.5rem",
        border_radius="0.5rem",
        width="100%",
        height="100%",
    )


def create_projects_section():
    """Create the 'Projects' section with expandable project cards filled with Lorem Ipsum."""
    return rx.box(
        create_section_heading(heading_text="Lorem Ipsum Projects"),
        rx.box(
            rx.cond(
                ProjectState.selected_project != "",
                # Layout when a project is selected
                rx.box(
                    rx.cond(
                        ProjectState.selected_project == "openvino",
                        create_project_card(
                            animation_attrs={
                                "data-aos": "fade-up", "data-aos-delay": "200"},
                            project_id="openvino",
                            project_title="Lorem Ipsum Dolor",
                            project_description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                            technologies_used="Lorem, Ipsum, Dolor",
                            href="https://github.com/openvinotoolkit/training_extensions",
                            link_text="Lorem Link",
                            project_details={
                                "detailed_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                                "key_features": [
                                    "Lorem ipsum dolor sit amet.",
                                    "Consectetur adipiscing elit.",
                                    "Sed do eiusmod tempor incididunt."
                                ],
                                "development_contributions": [
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing.",
                                    "Eiusmod tempor incididunt ut labore dolore.",
                                    "Magna aliqua ut enim ad minim veniam."
                                ],
                                "research_contributions": [
                                    "Lorem ipsum dolor sit amet research.",
                                    "Consectetur adipiscing elit research.",
                                    "Sed do eiusmod tempor research."
                                ],
                                "image": None,
                                "research_image": None,
                            },
                        ),
                    ),
                    rx.cond(
                        ProjectState.selected_project == "geti",
                        create_project_card(
                            animation_attrs={
                                "data-aos": "fade-up", "data-aos-delay": "400"},
                            project_id="geti",
                            project_title="Dolor Sit Amet",
                            project_description="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                            technologies_used="Ipsum, Dolor, Sit",
                            href="https://geti.intel.com/",
                            link_text="Lorem Link",
                            project_details={
                                "detailed_description": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                                "key_features": [
                                    "Ut enim ad minim veniam.",
                                    "Quis nostrud exercitation ullamco.",
                                    "Laboris nisi ut aliquip ex ea commodo."
                                ],
                                "development_contributions": [
                                    "Ut enim ad minim veniam development.",
                                    "Quis nostrud exercitation development.",
                                    "Laboris nisi ut aliquip development."
                                ],
                                "research_contributions": [
                                    "Ut enim research contributions.",
                                    "Quis nostrud research contributions.",
                                    "Laboris nisi research contributions."
                                ],
                                "image": None,
                                "research_image": None,
                            },
                        ),
                    ),
                    rx.cond(
                        ProjectState.selected_project == "anomalib",
                        create_project_card(
                            animation_attrs={
                                "data-aos": "fade-up", "data-aos-delay": "600"},
                            project_id="anomalib",
                            project_title="Amet Consectetur",
                            project_description="Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
                            technologies_used="Dolor, Sit, Amet",
                            href="https://github.com/openvinotoolkit/anomalib",
                            link_text="Lorem Link",
                            project_details={
                                "detailed_description": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
                                "key_features": [
                                    "Duis aute irure dolor.",
                                    "In reprehenderit in voluptate.",
                                    "Velit esse cillum dolore."
                                ],
                                "development_contributions": [
                                    "Duis aute development.",
                                    "In reprehenderit development.",
                                    "Velit esse development."
                                ],
                                "research_contributions": [
                                    "Duis aute research.",
                                    "In reprehenderit research.",
                                    "Velit esse research."
                                ],
                                "image": None,
                                "research_image": None,
                            },
                        ),
                    ),
                    width="100%",
                ),
                # Default grid layout
                rx.box(
                    create_project_card(
                        animation_attrs={"data-aos": "fade-up",
                                         "data-aos-delay": "200"},
                        project_id="openvino",
                        project_title="Lorem Ipsum Dolor",
                        project_description="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                        technologies_used="Lorem, Ipsum, Dolor",
                        href="https://github.com/openvinotoolkit/training_extensions",
                        link_text="Lorem Link",
                    ),
                    create_project_card(
                        animation_attrs={"data-aos": "fade-up",
                                         "data-aos-delay": "400"},
                        project_id="geti",
                        project_title="Dolor Sit Amet",
                        project_description="Ut enim ad minim veniam, quis nostrud ullamco.",
                        technologies_used="Ipsum, Dolor, Sit",
                        href="https://geti.intel.com/",
                        link_text="Lorem Link",
                    ),
                    create_project_card(
                        animation_attrs={"data-aos": "fade-up",
                                         "data-aos-delay": "600"},
                        project_id="anomalib",
                        project_title="Amet Consectetur",
                        project_description="Duis aute irure dolor in reprehenderit.",
                        technologies_used="Dolor, Sit, Amet",
                        href="https://github.com/openvinotoolkit/anomalib",
                        link_text="Lorem Link",
                    ),
                    gap="2rem",
                    display="grid",
                    grid_template_columns=rx.breakpoints({
                        "0px": "repeat(1, minmax(0, 1fr))",
                        "768px": "repeat(2, minmax(0, 1fr))",
                        "1024px": "repeat(3, minmax(0, 1fr))",
                    }),
                ),
            ),
            width="100%",
            transition="all 0.3s ease-in-out",
        ),
        id="projects",
        width="100%",
        style=rx.breakpoints({
            "640px": {"max-width": "640px"},
            "768px": {"max-width": "768px"},
            "1024px": {"max-width": "1024px"},
            "1280px": {"max-width": "1280px"},
            "1536px": {"max-width": "1536px"},
        }),
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="4rem",
        padding_bottom="4rem",
    )
