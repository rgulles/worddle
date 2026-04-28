from tkinter import *

from settings import Settings
from welcome_screen import WelcomeScreen

class Worddle:
    def __init__(self, master):
        self.master = master
        self.settings = Settings()

        self.master.title(self.settings.title)
        self.master.geometry(f'{self.settings.screen_width}x{self.settings.screen_height}')
        self.master.resizable(False, False)

        self.container = Frame(self.master)
        self.container.pack()

        self.show_welcome_screen()

    def show_welcome_screen(self):
        for widget in self.container.winfo_children():
            widget.pack_forget()
       
        self.welcome_screen = WelcomeScreen(self.container, self.show_difficulty_screen)
    
    def show_difficulty_screen(self):
        pass

if __name__ == "__main__":
    root = Tk()
    game = Worddle(root)
    root.mainloop()