"""
ViewFree Application Manager
"""

from src.app_manager.apps import AI

from src.apps.ai_app import run as ai_run
from src.apps.files_app import run as files_run
from src.apps.notes_app import run as notes_run
from src.apps.camera_app import run as camera_run
from src.apps.settings_app import run as settings_run


class ApplicationManager:

    def __init__(self):
        self.current_app = AI

    def switch_app(self, app_name):
        self.current_app = app_name

    def get_current_app(self):
        return self.current_app

    def render(self, frame):

        if self.current_app == "AI":
            ai_run(frame)

        elif self.current_app == "Files":
            files_run(frame)

        elif self.current_app == "Notes":
            notes_run(frame)

        elif self.current_app == "Camera":
            camera_run(frame)

        elif self.current_app == "Settings":
            settings_run(frame)