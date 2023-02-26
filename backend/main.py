import keyboard, threading

class KeyboardEvent:
    def __init__(self):
        # Start a new thread to detect keyboard events
        t = threading.Thread(target=self.wait_for_key)
        t.start()
        
    def on_key_press(self, event, root=None):
        if event.name=="caps lock":
            root.showFrame('CL', root.is_capslock_on(0x14))
        elif event.name=="num lock":
            root.showFrame("NL", root.is_capslock_on(0x90))
        elif event.name=="scroll lock":
            root.showFrame("SL", root.is_capslock_on(0x91))
            
    def wait_for_key(self):
        keyboard.wait()