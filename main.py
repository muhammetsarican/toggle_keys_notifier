from ui.main import uiCreate
from backend.main import KeyboardEvent
import keyboard

if __name__=="__main__":
    root=uiCreate()
    keyboardkey=KeyboardEvent()
    keyboard.on_press(lambda event:keyboardkey.on_key_press(event, root))
    root.mainloop()