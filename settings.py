import tkinter.font as tkFont

class Settings: 
    def __init__(self):

        # Screen
        self.title = "Worddle"
        self.screen_width = 500
        self.screen_height = 750

        # Colors
        self.GREY = '#C1C7C2'
        self.YELLOW = '#EFFF14'
        self.GREEN = '#00F721'

        # Fonts
        self.font_family = "Courier New"
        self.title_font = tkFont.Font(family=self.font_family, size=45, weight="bold")
        self.label_font = tkFont.Font(family=self.font_family, size=14)
        self.riddle_font = tkFont.Font(family=self.font_family, size=12)
        self.button_font = tkFont.Font(family=self.font_family, size=24, weight="bold")
        self.entry_font = tkFont.Font(family=self.font_family, size=40, weight="bold")

        # Buttons
        self.button_width = 10
        self.difficulty_button_width = 15
        self.submit_button_width = 10

        # Entry
        self.entry_width = 2

        # Rows and Columns
        self.rows = 6
        self.easy_cols = 4