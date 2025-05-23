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
        create_section_heading(heading_text="My Projects"),
        rx.box(
            rx.cond(
                ProjectState.selected_project != "",
                # Layout when a project is selected
                rx.box(
                    rx.cond(
                        ProjectState.selected_project == "f1_strat_manager_ai",
                        create_project_card(
                            animation_attrs={
                                "data-aos": "fade-up", "data-aos-delay": "200"},
                            project_id="f1_strat_manager_ai",
                            project_title="F1 Strategy AI Manager",
                            project_description="An AI-powered, open-source system for recommending optimal race strategies in Formula 1, developed as an ongoing final project for the 3rd year of UIE Intelligent Systems Engineering. The models are trained on real-world data from the 2023 Barcelona Grand Prix, leveraging machine learning to enhance race decision-making. This project is under active and continuous development.",
                            technologies_used="Jupyter Notebook, Python, Machine Learning, FastF1, Data Analysis",
                            href="https://github.com/VforVitorio/F1_Strat_Manager",
                            link_text="View on GitHub",
                            project_details={
                                "detailed_description": (
                                    "The F1 Strategy AI Manager is an advanced, open-source tool designed to assist Formula 1 teams and enthusiasts in making data-driven strategic decisions during races. Utilizing extensive data from the 2023 Barcelona Grand Prix, the project implements machine learning models to simulate and predict race outcomes based on various strategic choices such as pit stops, tire selections, and weather conditions. "
                                    "Developed primarily in Jupyter Notebook and Python, the project demonstrates the application of AI techniques in the high-stakes environment of Formula 1 racing. The system integrates with the FastF1 library to extract and preprocess telemetry and timing data, providing a robust foundation for model training and evaluation. The outcome is a user-friendly platform capable of generating actionable strategy recommendations tailored to real-time race scenarios. "
                                    "This project is open source and remains under constant development, welcoming community contributions and ongoing improvements."
                                ),
                                "key_features": [
                                    "AI-powered strategy recommendations for Formula 1 races.",
                                    "Trained and validated on real data from the 2023 Barcelona Grand Prix.",
                                    "Integration with FastF1 for automated telemetry and timing data extraction.",
                                    "Comprehensive analysis of pit stop timing, tire choices, and race conditions.",
                                    "Interactive Jupyter Notebooks for experimentation and results visualization.",
                                    "Open-source and continuously evolving with new features and improvements."
                                ],
                                "development_contributions": [
                                    "Developed machine learning models to simulate and optimize F1 race strategies.",
                                    "Built data pipelines for preprocessing and feature engineering with FastF1 and pandas.",
                                    "Implemented a modular, extensible codebase in Python and Jupyter Notebook.",
                                    "Created detailed documentation and visualization notebooks to interpret results.",
                                    "Maintained ongoing development and integration of new features based on user and community feedback."
                                ],
                                "research_contributions": [
                                    "Analyzed the impact of strategic decisions in F1 using historical race data.",
                                    "Benchmarked multiple AI models to identify the best predictors of race outcomes.",
                                    "Explored the application of data-driven techniques in motorsport analytics.",
                                    "Authored a scientific paper documenting the methodology, experiments, and findings, which is included in the repository for reference."
                                ],
                                "image": None,
                                "research_image": None,
                            },
                        ),
                    ),
                    rx.cond(
                        ProjectState.selected_project == "f1_ai_team_detection",
                        create_project_card(
                            animation_attrs={
                                "data-aos": "fade-up", "data-aos-delay": "400"},
                            project_id="f1_ai_team_detection",
                            project_title="F1 AI Team Detection & Race Analysis",
                            project_description=(
                                "A specialized computer vision system that evolved from the F1 Strategy AI Manager project. "
                                "Built with YOLOv12, it automatically detects and classifies Formula 1 teams in race footage, "
                                "estimates real-time distances and time gaps between cars, enabling advanced race analytics."
                            ),
                            technologies_used="YOLOv12, OpenCV, Python, Jupyter Notebook, Machine Learning, Computer Vision",
                            href="https://github.com/VforVitorio/F1_AI_team_detection",
                            link_text="View on GitHub",
                            project_details={
                                "detailed_description": (
                                    "F1 AI Team Detection originated as a computer vision module within the F1 Strategy AI Manager project and has evolved into "
                                    "a standalone, specialized system for Formula 1 analysis. This project represents a significant advancement from the original "
                                    "YOLOv8 implementation to the more powerful YOLOv12 architecture, specifically fine-tuned for Formula 1 environments. "
                                    "The separated workflow allows for deeper exploration of computer vision techniques and more focused optimization for F1-specific "
                                    "challenges such as high-speed tracking, team livery recognition, and precise gap calculations. Unlike general motorsport detection "
                                    "systems, this tool is exclusively tailored for Formula 1, taking into account the unique characteristics of F1 cars, teams, and "
                                    "racing dynamics to provide unparalleled accuracy in team detection and race analysis."
                                ),
                                "key_features": [
                                    "Advanced YOLOv12 implementation specifically trained for Formula 1 team detection.",
                                    "Real-time estimation of precise distances and time gaps between F1 cars.",
                                    "Dedicated workflow separation from the main strategy project for enhanced modularity.",
                                    "F1-specific optimizations including team livery recognition and high-speed tracking.",
                                    "Interactive visualization of positional data overlayed on race footage.",
                                    "Specialized detection for all current F1 teams with continuous model updates."
                                ],
                                "development_contributions": [
                                    "Upgraded detection pipeline from YOLOv8 to YOLOv12 for improved accuracy and speed.",
                                    "Separated and refactored computer vision workflow from the parent F1 Strategy project.",
                                    "Implemented F1-specific training data augmentation for better team recognition.",
                                    "Developed custom distance estimation algorithms calibrated for F1 track dimensions.",
                                    "Created modular architecture allowing easy integration with strategy analysis tools.",
                                    "Optimized inference pipeline for real-time processing of broadcast footage."
                                ],
                                "research_contributions": [
                                    "Conducted comparative analysis between YOLOv8 and YOLOv12 for F1-specific detection tasks.",
                                    "Developed novel approaches for team classification based on livery patterns and colors.",
                                    "Investigated Formula 1-specific challenges in computer vision including motion blur and varying lighting.",
                                    "Created custom F1 dataset with precise annotations for team detection model training.",
                                    "Documented performance improvements and best practices for sports-specific object detection."
                                ],
                                "image": None,
                                "research_image": None,
                            },
                        ),
                    ),
                    rx.cond(
                        ProjectState.selected_project == "transformacion",
                        create_project_card(
                            animation_attrs={
                                "data-aos": "fade-up", "data-aos-delay": "600"},
                            project_id="transformacion",
                            project_title="Digital Transformation Assessment Tool",
                            project_description="A comprehensive tool built with Reflex (Pynecone) to evaluate the digital transformation maturity of companies. This project was originally conceived as a class assignment, and I took the opportunity to explore the Reflex framework, which allows for building web applications using pure Python. My goal was to strengthen my foundation as a full stack developer and gain practical experience in both frontend and backend disciplines, preparing myself for future projects where these skills may be essential.",
                            technologies_used="Python, Reflex (Pynecone), Web Development",
                            href="https://github.com/VforVitorio/Transformacion",
                            link_text="View on GitHub",
                            project_details={
                                "detailed_description": (
                                    "This project is a digital transformation assessment tool designed for companies aiming to understand and improve their digital maturity. Developed as part of an academic course, I leveraged the Reflex (Pynecone) framework to create an interactive and user-friendly web application entirely in Python. "
                                    "Through this project, I explored the intricacies of full stack development, implementing both the frontend and backend logic myself. Reflex enabled me to write Python code for every aspect of the application, from user interface to data processing, helping me bridge the gap between software engineering and web development. "
                                    "The tool guides users through a structured evaluation, providing insights and recommendations based on their responses. This hands-on experience has not only deepened my understanding of modern web technologies but also provided me with the confidence to tackle similar challenges in future professional projects."
                                ),
                                "key_features": [
                                    "Interactive web interface built entirely with Python using Reflex (Pynecone).",
                                    "Structured digital transformation assessment tailored for companies.",
                                    "Automatic generation of recommendations based on user input.",
                                    "Intuitive navigation and modern UI/UX design.",
                                    "Modular codebase, facilitating future expansions or customizations."
                                ],
                                "development_contributions": [
                                    "Designed and implemented the entire application architecture using Reflex.",
                                    "Developed custom UI components and managed state transitions in Python.",
                                    "Wrote backend logic to process and evaluate assessment data.",
                                    "Integrated best practices in both frontend and backend development.",
                                    "Deployed and maintained the project on GitHub for open-source collaboration."
                                ],
                                "research_contributions": [
                                    "Researched methodologies for assessing digital transformation in organizations.",
                                    "Evaluated the capabilities and limitations of Reflex (Pynecone) for Python web development.",
                                    "Explored full stack development workflows and best practices.",
                                    "Documented findings and shared insights for future student projects."
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
                        project_id="f1_strat_manager_ai",
                        project_title="F1 Strategy AI Manager",
                        project_description="An AI-powered, open-source system for recommending optimal race strategies in Formula 1, developed as an ongoing final project for the 3rd year of UIE Intelligent Systems Engineering. The models are trained on real-world data from the 2023 Barcelona Grand Prix, leveraging machine learning to enhance race decision-making. This project is under active and continuous development.",
                        technologies_used="Jupyter Notebook, Python, Machine Learning, FastF1, Data Analysis",
                        href="https://github.com/VforVitorio/F1_Strat_Manager",
                        link_text="View on GitHub",
                    ),
                    create_project_card(
                        animation_attrs={"data-aos": "fade-up",
                                         "data-aos-delay": "400"},
                        project_id="f1_ai_team_detection",
                        project_title="F1 AI Team Detection & Race Analysis",
                        project_description=(
                            "A specialized computer vision system that evolved from the F1 Strategy AI Manager project. "
                            "Built with YOLOv12, it automatically detects and classifies Formula 1 teams in race footage, "
                            "estimates real-time distances and time gaps between cars, enabling advanced race analytics."
                        ),
                        technologies_used="YOLOv12, OpenCV, Python, Jupyter Notebook, Machine Learning, Computer Vision",
                        href="https://github.com/VforVitorio/F1_AI_team_detection",
                        link_text="View on GitHub",
                    ),
                    create_project_card(
                        animation_attrs={"data-aos": "fade-up",
                                         "data-aos-delay": "600"},
                        project_id="transformacion",
                        project_title="Digital Transformation Assessment Tool",
                        project_description="A comprehensive tool built with Reflex (Pynecone) to evaluate the digital transformation maturity of companies. This project was originally conceived as a class assignment, and I took the opportunity to explore the Reflex framework, which allows for building web applications using pure Python. My goal was to strengthen my foundation as a full stack developer and gain practical experience in both frontend and backend disciplines, preparing myself for future projects where these skills may be essential.",
                        technologies_used="Python, Reflex (Pynecone), Web Development",
                        href="https://github.com/VforVitorio/Transformacion",
                        link_text="View Repository",
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
