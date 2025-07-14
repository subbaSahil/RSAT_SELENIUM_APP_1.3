import pytest
import os
from pytest_html import extras
 
def get_latest_file(folder, extension):
    try:
        files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(extension)]
        files.sort(key=os.path.getmtime, reverse=True)
        return files[0] if files else None
    except:
        return None
 
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
 
    if report.when == "call":
        # ✅ Screenshot Link
        screenshot = get_latest_file("reports/screens", ".png")
        if screenshot and os.path.exists(screenshot):
            rel_screenshot = os.path.relpath(screenshot, start="reports")
            extra.append(extras.url(rel_screenshot, name="📸 Screenshot"))
 
        # ✅ Recording Link
        recording = get_latest_file("reports/recordings", ".mp4")
        if recording and os.path.exists(recording):
            rel_recording = os.path.relpath(recording, start="reports")
            extra.append(extras.url(rel_recording, name="🎥 Recording"))
 
        report.extra = extra
 