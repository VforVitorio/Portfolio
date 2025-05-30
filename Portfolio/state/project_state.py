from reflex import State

# State for managing project details visibility.


class ProjectState(State):
    """State for managing project details visibility."""

    # Which project's details are currently shown
    selected_project: str = ""

    # Which tab is selected (development/research)
    selected_tab: str = "development"

    class Config:
        client_connect = False
        prevent_initial_call = True

    def toggle_project(self, project_id: str):
        """Toggle project expansion."""
        if self.selected_project == project_id:
            self.selected_project = ""
        else:
            self.selected_project = project_id

    def set_tab(self, tab: str):
        """Set the active tab."""
        self.selected_tab = tab
