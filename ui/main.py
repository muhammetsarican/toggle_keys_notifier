import customtkinter as ctk, threading, ctypes
from threading import Timer
from PIL import Image 
import glob
from screeninfo import get_monitors
import os

class uiCreate(ctk.CTk):
    # __init__ method create an ui and at first it shows developer info
    keysFirstState={
        "capslock":False,
        "numlock":False,
        "scrolllock":False
    }
    
    dark_hex="#242424"
    light_hex="#EBEBEB"
    
    themePreference="dark"

    def theme(self):
        if self.themePreference =="dark":
            return {
                "iconPath":"light",
                "text":self.light_hex,
                "bg":self.dark_hex
            }
        else:
            return {
                "iconPath":"dark",
                "text":self.dark_hex,
                "bg":self.light_hex
            }

    def __init__(self):
        super().__init__()
        icon_path="final_main/keyboard.ico"

        monitors = get_monitors()

        def setFirstState(key_name):
            paths = glob.glob(f"/sys/class/leds/*::{key_name}/brightness")
            for path in paths:
                try:
                    with open(path) as f:
                        if f.read().strip() == '1':
                            self.keysFirstState[key_name]=True
                except Exception:
                    continue
            else: 
                self.keysFirstState[key_name]=False
        
        for key in self.keysFirstState.keys():
            setFirstState(key)
        
        def getScreenSize():
            width=monitors[0].width 
            height=0
            for monitor in monitors:
                if monitor.height>height:
                    height=monitor.height
            return {"width":width,"height":height}

        screenSize=getScreenSize()
        
        screen_width=screenSize["width"]
        screen_height=screenSize["height"]
        # screen_width=self.winfo_screenwidth()
        # screen_height=self.winfo_screenheight()
        
        width=(screen_width/2)-(150/2)
        height=screen_height-175
        
        self.geometry(f"150x125+{int(width)}+{int(height)}")
        self.overrideredirect(True)
        
        self.title("Toggle Keys Notifier")
        # self.iconbitmap(icon_path)
        
        self._set_appearance_mode(self.themePreference)

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0), weight=1)
                
        ctk.CTkLabel(self, text="",
                    image=self.imageGenerator("default", (70, 70), state=None), bg_color=(self.theme()["bg"])
                    ).grid(padx=5, pady=5, row=0, column=0, sticky="ew")
        
        ctk.CTkLabel(self, text="Developed\nby Muhammet Sarican\nversion: Beta 1.0",font=("Consolas", 10), bg_color=(self.theme()["bg"]), text_color=(self.theme()["text"])
                    ).grid(padx=5, pady=5, row=1, column=0, sticky="ew")
                
        self.after(3000, self.withdraw)
        
    def showFrame(self, key=None, state=None):
        # We get the threads list in this code, because If we don't get this list key frame will close before 3 second.      
        threads = threading.enumerate()
        # We hide frame one time, because previous frame not be closed.
        self.withdraw()
        # Image can shown with label
        ctk.CTkLabel(self, text="",
                    image=self.imageGenerator(key, (100, 100), state=state),bg_color=(self.theme()["bg"])
                    ).grid(padx=5, pady=5, rowspan=2, row=0, column=0, sticky="nsew")
        self.deiconify()
        # In here, We found the previous times threads that used to hide notification frame, If we cant do that previous timer closes new frame
        for thread in threads:
            if threads.index(thread)>1:
                try:
                    thread.cancel()
                except:
                    pass
        
        Timer(3.0, self.withdraw, ()).start()
    # Image generator uses for getting image from storage
    def imageGenerator(self, key, size, state):
        SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(SCRIPT_DIR,"../", "icons", "final",self.theme()["iconPath"],"")
        # path="./icons/final/dark/"
        if state is not None:
            if state:
                path+="open/"
            else:
                path+="close/"
        if key is not None:
            if key=="CL":
                path+="caps-lock-finally.png"
            elif key=="NL":
                path+="num-lock-finally.png"
            elif key=="SL":
                path+="scroll-lock-finally.png"
            else:
                path+="default.png"
        image =Image.open(path)
        return ctk.CTkImage(
            #light_image=Image.open("icons/man.png"),
            dark_image=image,
            size=size,
        )
    
    def find_keyboard_device(self):
        base = "/dev/input/by-id/"
        if not os.path.exists(base):
            return None

        for name in os.listdir(base):
            if "kbd" in name:  # looks for "-event-kbd"
                path = os.path.join(base, name)
                if os.path.exists(path):
                    return path
        return None

    def LinuxKeyState(self, key_name):
            if self.keysFirstState[key_name]:
                self.keysFirstState[key_name]=False
            else:
                self.keysFirstState[key_name]=True
            return self.keysFirstState[key_name]
            

    def is_capslock_on(self, keyState, os):
        if os=="Linux":
              return self.LinuxKeyState(keyState["name"])
        if os=="Windows":
            return True if ctypes.WinDLL("User32.dll").GetKeyState(keyState.code)==1 or ctypes.WinDLL("User32.dll").GetKeyState(keyState.code)==65409 else False
