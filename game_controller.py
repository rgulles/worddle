from game_logic import check_guess

class GameController:
    def __init__(self, ui, settings):
        self.ui = ui
        self.settings = settings

    def check_row(self):
        row_inputs = self.ui.inputs[self.ui.current_row]
        guess = [entry.get().upper() for entry in row_inputs]

        if "" in guess:
            return

        result = check_guess(guess, self.ui.letters)

        for i, entry in enumerate(row_inputs):
            color = result[i]

            if color == "green":
                entry.config(state='disabled', disabledbackground=self.settings.GREEN)
            elif color == "yellow":
                entry.config(state='disabled', disabledbackground=self.settings.YELLOW)
            else:
                entry.config(state='disabled', disabledbackground=self.settings.GREY)

        if guess == self.ui.letters:
            self.ui.submit_button.config(state="disabled")
            print("You Guess the Word!")
            return

        for entry in row_inputs:
            entry.config(state='disabled')

        self.ui.current_row += 1

        if self.ui.current_row >= len(self.ui.inputs):
            self.ui.submit_button.config(state="disabled")
            print("You Lose, Game Over!")
            return

        for entry in self.ui.inputs[self.ui.current_row]:
            entry.config(state='normal')