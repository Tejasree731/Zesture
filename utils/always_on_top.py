
import ctypes
import sys

def set_always_on_top(window_name):
    if sys.platform == "win32":
        hwnd = ctypes.windll.user32.FindWindowW(None, window_name)
        if hwnd:
            ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 1 | 2)
