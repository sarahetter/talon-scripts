from talon import actions, app, ui

_was_in_meet = False


def _is_google_meet(window) -> bool:
    if window is None:
        return False
    app_name = (window.app.name or "").lower()
    if app_name == "google meet":
        return True
    title = (window.title or "").lower()
    return (
        "google meet" in title
        or title.startswith("meet -")
        or " - meet -" in title
    )


def _react(*_args):
    global _was_in_meet
    focused = ui.active_window()
    is_meet = _is_google_meet(focused)
    if is_meet and not _was_in_meet:
        actions.speech.disable()
        app.notify("Talon sleeping (Google Meet)")
    _was_in_meet = is_meet


ui.register("win_focus", _react)
ui.register("win_title", _react)
