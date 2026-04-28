from tkinter import Frame, Label, Button

from settings import Settings

class WelcomeScreen(Frame):
    def __init__(self, master, start):
        super().__init__(master)
        self.master = master

        self.settings = Settings()
        self.start_callback = start

        self.pack()

        self.game_title = Label(self, text=self.settings.title, font=self.settings.title_font)
        self.game_title.pack(pady=(150, 180))

        self.start_label = Label(self, text="Press start to begin:", font=self.settings.label_font, justify='center')
        self.start_label.pack()

        self.start_button = Button(self, text="START", width=self.settings.button_width, font=self.settings.button_font, background=self.settings.GREY, command=self.start_callback)
        self.start_button.pack(pady=(30, 150))