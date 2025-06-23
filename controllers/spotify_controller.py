import pyautogui

def handle_spotify_gesture(fingers):
    if fingers == [0, 1, 0, 0, 0]:
        pyautogui.press('playpause')
        return "Play/Pause"
    elif fingers == [0, 1, 0, 0, 1]:
        pyautogui.hotkey('ctrl', 'right')
        return "Next Song"
    elif fingers == [1, 1, 0, 0, 1]:
        pyautogui.hotkey('ctrl', 'left')
        return "Previous Song"
    return ""
