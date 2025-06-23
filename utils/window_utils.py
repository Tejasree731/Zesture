import time
import pygetwindow as gw
import pyautogui

def snap_browser_to_side(browser_title_contains, side="right"):
    time.sleep(2)  # Give the browser time to open
    windows = gw.getWindowsWithTitle(browser_title_contains)
    if windows:
        browser_win = windows[0]
        browser_win.activate()
        pyautogui.hotkey('win', side)
        return True
    return False

def snap_opencv_window(window_title="Spotify Gesture Controller", side="left"):
    time.sleep(1.5)  # Wait for OpenCV window to fully appear
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        win = windows[0]
        win.activate()
        pyautogui.hotkey('win', side)
