from tkinter import Frame, Button, Label, Entry

from settings import Settings
from words import get_random_word_data

class EasyScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.settings = Settings()
        self.pack()

        self.game_title = Label(self, text=self.settings.title, font=self.settings.title_font)
        self.game_title.pack(pady=(30, 0))

        self.difficulty_label = Label(self, text="EASY", font=self.settings.label_font)
        self.difficulty_label.pack(pady=(0, 20))

        self.word, self.riddle, self.letters = get_random_word_data("easy")

        self.riddle_label = Label(self, text=self.riddle, font=self.settings.riddle_font, wraplength=400, justify="center")
        self.riddle_label.pack(pady=(0, 20))

        self.frame = Frame(self)
        self.frame.pack()

        self.inputs = []
        
        self.create_grid()

        self.submit_button = Button(self, text="Submit", width=self.settings.submit_button_width, font=self.settings.button_font)
        self.submit_button.pack(pady=20)

    def create_grid(self):
        rows = 6
        cols = 4

        for row in range(rows):
            row_inputs = []
            for col in range(cols):
                entry = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
                entry.grid(row=row, column=col, padx=2, pady=2)

                row_inputs.append(entry)

            self.inputs.append(row_inputs)