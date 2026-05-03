from tkinter import  Frame, Button, Label

from settings import Settings

class DifficultyScreen(Frame):    
   def __init__(self, master, back, start_game):
      super().__init__(master)

      self.settings = Settings()
      self.back_callback = back
      self.start_game = start_game

      self.pack()

      self.back_button = Button(self, text="← Back", font=self.settings.label_font, command=self.back_callback, bd=0)
      self.back_button.pack(anchor='nw', pady=(10, 0), padx=(10, 0))

      self.game_title = Label(self, text=self.settings.title, font=self.settings.title_font)
      self.game_title.pack(pady=(100, 10))

      self.select_difficulty_label = Label(self, text="Select level of difficulty", font=self.settings.label_font)
      self.select_difficulty_label.pack(pady=(0, 50))

      self.easy_level_button = Button(
         self,
         text="EASY",
         width=self.settings.difficulty_button_width,
         font=self.settings.button_font,
         background=self.settings.GREY,
         command=lambda: self.start_game("easy")
      )
      self.easy_level_button.pack(pady=(30, 10))

      self.normal_level_button = Button(
         self,
         text="NORMAL",
         width=self.settings.difficulty_button_width,
         font=self.settings.button_font,
         background=self.settings.GREY,
         command=lambda: self.start_game("normal")
      )
      self.normal_level_button.pack(pady=(30, 30))

      self.hard_level_button = Button(
         self,
         text="HARD",
         width=self.settings.difficulty_button_width,
         font=self.settings.button_font,
         background=self.settings.GREY,
         command=lambda: self.start_game("hard")
      )
      self.hard_level_button.pack(pady=(10, 100))