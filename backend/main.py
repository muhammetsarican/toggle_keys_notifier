import keyboard, threading
import platform

class KeyboardEvent:
    def __init__(self):
        # Start a new thread to detect keyboard events
        t = threading.Thread(target=self.wait_for_key)
        t.start()

    os_name = platform.system()
        
    def on_key_press(self, event, root=None):
        if event.name=="caps lock":
            root.showFrame('CL', root.is_capslock_on({"name":"capslock","code":0x14}, self.os_name))
        elif event.name=="num lock":
            root.showFrame("NL", root.is_capslock_on({"name":"numlock", "code":0x90}, self.os_name))
        elif event.name=="scroll lock":
            root.showFrame("SL", root.is_capslock_on({"name":"scrolllock","code":0x91}, self.os_name))
            
    def wait_for_key(self):
        keyboard.wait()