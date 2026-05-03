from tkinter import Frame, Button, Label

from settings import Settings
from grid import create_grid
from words import get_random_word_data
from game_controller import GameController

class GameScreen(Frame):
    def __init__(self, master, back, difficulty, restart_callback):
        super().__init__(master)

        self.settings = Settings()
        self.back_callback = back
        self.difficulty = difficulty
        self.controller = GameController(self, self.settings, self.master, restart_callback)

        self.pack()

        self.word, self.riddle, self.letters = get_random_word_data(difficulty)

        self.inputs = []
        self.current_row = 0

        self.back_button = Button(self, text="← Back", font=self.settings.label_font, command=self.back_callback, bd=0)
        self.back_button.pack(anchor='nw', pady=(10, 0), padx=(10, 0))

        self.game_title = Label(self, text=self.settings.title, font=self.settings.title_font)
        self.game_title.pack(pady=(10, 10))

        self.difficulty_label = Label(self, text=difficulty.upper(), font=self.settings.label_font)
        self.difficulty_label.pack(pady=(0, 10))

        self.riddle_label = Label(self,text=self.riddle, font=self.settings.riddle_font, wraplength=400, justify="center")
        self.riddle_label.pack(pady=(0, 20))

        self.frame = Frame(self)
        self.frame.pack()

        create_grid(self.frame, self.settings, self.inputs, self.difficulty)

        self.submit_button = Button(
            self,
            text="Submit",
            width=self.settings.submit_button_width,
            font=self.settings.button_font,
            command=self.controller.check_row
        )
        self.submit_button.pack(pady=20)

        for entry in self.inputs[0]:
            entry.config(state='normal')