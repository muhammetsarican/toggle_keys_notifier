import customtkinter as ctk, threading, ctypes
from threading import Timer
from PIL import Image 

class uiCreate(ctk.CTk):
    # __init__ method create an ui and at first it shows developer info
    def __init__(self):
        super().__init__()
        icon_path="final_main/keyboard.ico"
        
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        
        width=(screen_width/2)-(150/2)
        height=screen_height-175
        
        self.geometry(f"150x125+{int(width)}+{int(height)}")
        self.overrideredirect(True)
        
        self.title("Toggle Keys Notifier")
        # self.iconbitmap(icon_path)
        
        self._set_appearance_mode("dark")

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0), weight=1)
                
        ctk.CTkLabel(self, text="",
                    image=self.imageGenerator("default", (70, 70), state=None)
                    ).grid(padx=5, pady=5, row=0, column=0, sticky="ew")
        
        ctk.CTkLabel(self, text="Developed\nby Muhammet Sarican\nversion: Beta 1.0",font=("Consolas", 10)
                    ).grid(padx=5, pady=5, row=1, column=0, sticky="ew")
                
        self.after(3000, self.withdraw)
        
    def showFrame(self, key=None, state=None):
        # We get the threads list in this code, because If we don't get this list key frame will close before 3 second.      
        threads = threading.enumerate()
        # We hide frame one time, because previous frame not be closed.
        self.withdraw()
        # Image can shown with label
        ctk.CTkLabel(self, text="",
                    image=self.imageGenerator(key, (100, 100), state=state)
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
        path="./icons/final/white/"
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

    def is_capslock_on(self, keyState):
        return True if ctypes.WinDLL("User32.dll").GetKeyState(keyState)==1 or ctypes.WinDLL("User32.dll").GetKeyState(keyState)==65409 else False
