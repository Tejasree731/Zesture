import pyautogui

def handle_system_gesture(fingers):
    if fingers == [0, 1, 0, 0, 0]:
        pyautogui.press('volumeup')
        return "Volume Up"
    elif fingers == [0, 1, 1, 0, 0]:
        pyautogui.press('volumedown')
        return "Volume Down"
    return ""
