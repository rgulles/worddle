from tkinter import *

class Worddle:
    def __init__(self, master):
        self.master = master

        self.master.title('Wordle')
        self.master.geometry('500x700')

if __name__ == "__main__":
    root = Tk()
    game = Worddle(root)
    root.mainloop()