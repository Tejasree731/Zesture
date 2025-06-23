import pyautogui

#control youtube
def handle_youtube_gesture(fingers):
    if fingers == [0, 1, 0, 0, 0]:
        pyautogui.press('space')
        return "Play / Pause"
    elif fingers == [1, 0, 0, 0, 0]:
        pyautogui.press('j')
        return "Rewind 10s"
    elif fingers == [0, 1, 1, 0, 0]:
        pyautogui.press('l')
        return "Forward 10s"
    elif fingers == [1, 1, 1, 1, 1]:
        pyautogui.press('f')
        return "Fullscreen"
    elif fingers == [0, 1, 0, 0, 1]:
        pyautogui.hotkey('shift', 'n')
        return "Next Video"
    elif fingers == [1, 1, 0, 0, 1]:
        pyautogui.hotkey('shift', 'p')
        return "Previous Video"
    elif fingers == [0, 0, 1, 1, 1]:
        pyautogui.press('m')
        return "Mute / Unmute"
    elif fingers == [0, 0, 0, 0, 0]:
        pyautogui.press('space')
        return "Pause"
    return ""
