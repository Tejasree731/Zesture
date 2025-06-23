from controllers.youtube_controller import handle_youtube_gesture
from controllers.system_controller import handle_system_gesture
from controllers.spotify_controller import handle_spotify_gesture
from core.mode_manager import getmode


CURRENT_MODE = getmode()

def handle_gesture(fingers):
    CURRENT_MODE = getmode()
    if CURRENT_MODE == "youtube":
        return handle_youtube_gesture(fingers)
    elif CURRENT_MODE == "system":
        return handle_system_gesture(fingers)
    elif CURRENT_MODE == "spotify":
        return handle_spotify_gesture(fingers)
    return ""
