from tkinter import Frame, Button, Label, Entry, END

from settings import Settings
from game_controller import GameController
from words import get_random_word_data
from grid import create_grid

class EasyScreen(Frame):
    def __init__(self, master, restart_callback):
        super().__init__(master)

        self.settings = Settings()
        self.controller = GameController(self, self.settings, self.master, restart_callback)
        self.pack()

        self.word, self.riddle, self.letters = get_random_word_data("easy")

        self.current_row = 0
        self.inputs = []

        self.game_title = Label(self, text=self.settings.title, font=self.settings.title_font)
        self.game_title.pack(pady=(30, 0))

        self.difficulty_label = Label(self, text="EASY", font=self.settings.label_font)
        self.difficulty_label.pack(pady=(0, 20))

        self.riddle_label = Label(self, text=self.riddle, font=self.settings.riddle_font, wraplength=400, justify="center")
        self.riddle_label.pack(pady=(0, 20))

        self.frame = Frame(self)
        self.frame.pack()
        
        create_grid(self.frame, self.settings, self.inputs)

        self.submit_button = Button(self, text="Submit", width=self.settings.submit_button_width, font=self.settings.button_font, command=self.controller.check_row)
        self.submit_button.pack(pady=20)

        for entry in self.inputs[0]:
            entry.config(state='normal')