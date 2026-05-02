from tkinter import Frame, Button, Label, Entry

from settings import Settings
from words import get_random_word_data
from game_logic import check_guess

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
        self.current_row = 0

        self.riddle_label = Label(self, text=self.riddle, font=self.settings.riddle_font, wraplength=400, justify="center")
        self.riddle_label.pack(pady=(0, 20))

        self.frame = Frame(self)
        self.frame.pack()

        self.inputs = []
        
        self.create_grid()

        self.submit_button = Button(self, text="Submit", width=self.settings.submit_button_width, font=self.settings.button_font, command=self.check_row)
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

    def check_row(self):
        row_inputs = self.inputs[self.current_row]
        guess = [entry.get().upper() for entry in row_inputs]

        result = check_guess(guess, self.letters)

        for i, entry in enumerate(row_inputs):
            color = result[i]

            if color == "green":
                entry.config(state='disabled', disabledbackground=self.settings.GREEN)
            elif color == "yellow":
                entry.config(state='disabled', disabledbackground=self.settings.YELLOW)
            else:
                entry.config(state='disabled', disabledbackground=self.settings.GREY)

        if guess == self.letters:
            self.submit_button.config(state="disabled")
            print("You Guess the Word!")
            return
 
        self.current_row += 1

        if self.current_row >= len(self.inputs):
            self.submit_button.config(state="disabled")
            print("You Lose, Game Over!")
        else:
            for entry in self.inputs[self.current_row]:
                entry.config(state='normal')