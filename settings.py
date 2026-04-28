import tkinter.font as tkFont

class Settings: 
    def __init__(self):

        # Screen
        self.title = "Worddle"
        self.screen_width = 500
        self.screen_height = 700

        # Colors
        self.GREY = '#C1C7C2'

        # Fonts
        self.font_family = "Courier New"
        self.title_font = tkFont.Font(family=self.font_family, size=45, weight="bold")
        self.label_font = tkFont.Font(family=self.font_family, size=14)
        self.button_font = tkFont.Font(family=self.font_family, size=24, weight="bold")
        self.entry_font = tkFont.Font(family=self.font_family, size=40, weight="bold")

        # Buttons
        self.button_width = 10
