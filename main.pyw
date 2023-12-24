from setup import *


MAKE(MACRO(windows, "c"), lambda: START(PATHS["VSCODIUM"]))
MAKE(MACRO(ctrl, shift, "w"), lambda: CLOSE())
LOOP()
