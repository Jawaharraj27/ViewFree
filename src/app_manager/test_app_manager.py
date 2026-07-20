import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)



from src.app_manager.app_manager import ApplicationManager
from src.app_manager.apps import CAMERA, FILES, NOTES

app = ApplicationManager()

print("Current:", app.get_current_app())

app.switch_app(CAMERA)
print("Current:", app.get_current_app())

app.switch_app(FILES)
print("Current:", app.get_current_app())

app.switch_app(NOTES)
print("Current:", app.get_current_app())