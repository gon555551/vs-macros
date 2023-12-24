try:
    from sys import _MEIPASS as meipass
except ImportError:
    from os import getcwd

    meipass = getcwd()
from keyboard import add_hotkey as MAKE
from threading import Thread
from keyboard import wait
import win32con, win32gui
from os import system
import infi.systray
import json


# System Icon Tray
infi.systray.SysTrayIcon(
    icon=rf"{meipass}\p_icon.ico",
    hover_text="Macros",
).start()


# Helper Functions
def LOOP():
    Thread(target=wait, daemon=True).start()


def MACRO(*args):
    return "+".join([k for k in args])


# Macro Functions
def START(p: str):
    system(rf"start /b {p}")


def CLOSE():
    win32gui.PostMessage(win32gui.GetForegroundWindow(), win32con.WM_CLOSE, 0, 0)


# Keys, might be different depending on KB language
windows = "windows esquerda"
shift = "shift"
ctrl = "ctrl"


# Paths
def get_paths() -> dict:
    _paths = {}
    with open("paths.json", "rb") as p:
        _paths = json.loads(p.read())
    return _paths


PATHS = get_paths()
