from tkinter import Frame, Button, Label, Entry

from settings import Settings

class EasyScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.settings = Settings()

        self.pack()

        self.game_title = Label(self, text=self.settings.title, font=self.settings.title_font)
        self.game_title.pack(pady=(30, 0))

        self.difficulty_label = Label(self, text="EASY", font=self.settings.label_font)
        self.difficulty_label.pack(pady=(0, 20))

        self.frame = Frame(self)
        self.frame.pack()

        self.row_1()
        self.row_2()
        self.row_3()
        self.row_4()
        self.row_5()
        self.row_6()

        self.submit_button = Button(self, text="Submit", width=self.settings.submit_button_width, font=self.settings.button_font)
        self.submit_button.pack(pady=20)

    def row_1(self):
        self.input_1 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_1.grid(row=0, column=0, padx=2, pady=2)

        self.input_2 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_2.grid(row=0, column=1, padx=2, pady=2)

        self.input_3 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_3.grid(row=0, column=2, padx=2, pady=2)

        self.input_4 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_4.grid(row=0, column=3, padx=2, pady=2)

    def row_2(self):
        self.input_5 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_5.grid(row=1, column=0, padx=2, pady=2)

        self.input_6 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_6.grid(row=1, column=1, padx=2, pady=2)

        self.input_7 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_7.grid(row=1, column=2, padx=2, pady=2)

        self.input_8 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_8.grid(row=1, column=3, padx=2, pady=2)

    def row_3(self):
        self.input_9 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_9.grid(row=2, column=0, padx=2, pady=2)

        self.input_10 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_10.grid(row=2, column=1, padx=2, pady=2)

        self.input_11 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_11.grid(row=2, column=2, padx=2, pady=2)

        self.input_12= Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_12.grid(row=2, column=3, padx=2, pady=2)

    def row_4(self):
        self.input_13 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_13.grid(row=3, column=0, padx=2, pady=2)

        self.input_14 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_14.grid(row=3, column=1, padx=2, pady=2)

        self.input_15 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_15.grid(row=3, column=2, padx=2, pady=2)

        self.input_16 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_16.grid(row=3, column=3, padx=2, pady=2)

    def row_5(self):
        self.input_17 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_17.grid(row=4, column=0, padx=2, pady=2)

        self.input_18 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_18.grid(row=4, column=1, padx=2, pady=2)

        self.input_19 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_19.grid(row=4, column=2, padx=2, pady=2)

        self.input_20 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_20.grid(row=4, column=3, padx=2, pady=2)

    def row_6(self):
        self.input_21 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_21.grid(row=5, column=0, padx=2, pady=2)

        self.input_22 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_22.grid(row=5, column=1, padx=2, pady=2)

        self.input_23 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_23.grid(row=5, column=2, padx=2, pady=2)

        self.input_24 = Entry(self.frame, width=self.settings.entry_width, font=self.settings.entry_font, justify="center")
        self.input_24.grid(row=5, column=3, padx=2, pady=2)





