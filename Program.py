import ctypes
import time

mouse_event = ctypes.windll.user32.mouse_event
MOUSE_EVENT_MOVE = 0x0001
print("Press Ctrl-C to end Mouse Shaker")
try:
    while True:
        mouse_event(MOUSE_EVENT_MOVE, 25, 0, 0, 0)
        time.sleep(240)
        mouse_event(MOUSE_EVENT_MOVE, 0, 25, 0, 0)
        time.sleep(240)
        mouse_event(MOUSE_EVENT_MOVE, -25, 0, 0, 0)
        time.sleep(240)
        mouse_event(MOUSE_EVENT_MOVE, 0, -25, 0, 0)
        time.sleep(240)
except KeyboardInterrupt:
    pass
