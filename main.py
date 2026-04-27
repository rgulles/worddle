from tkinter import *
from settings import Settings

class Worddle:
    def __init__(self, master):
        self.master = master
        self.settings = Settings()

        self.master.title(self.settings.title)
        self.master.geometry(f'{self.settings.screen_width}x{self.settings.screen_height}')

if __name__ == "__main__":
    root = Tk()
    game = Worddle(root)
    root.mainloop()