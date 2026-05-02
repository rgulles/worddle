from tkinter import messagebox

class ResultHandler:
    def __init__(self, root, restart_callback):
        self.root = root
        self.restart_callback = restart_callback

    def game_won(self):
        self._show_result("You guessed the word!")

    def game_lost(self):
        self._show_result("You lose, game over!")

    def _show_result(self, message):
        messagebox.showinfo("Word Riddle", message)

        retry = messagebox.askquestion("Word Riddle", "Do you want to try again?")

        if retry == "yes":
            self._reset_game()
        else:
            self.root.quit()

    def _reset_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.restart_callback()