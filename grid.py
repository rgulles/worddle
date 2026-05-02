from tkinter import Entry, END

def force_uppercase(event):
    entry = event.widget
    value = entry.get()

    if value:
        value = value[-1].upper()
        entry.delete(0, END)
        entry.insert(0, value)


def create_grid(frame, settings, inputs):
    rows = settings.rows
    cols = settings.easy_cols

    for row in range(rows):
        row_inputs = []

        for col in range(cols):
            entry = Entry(
                frame,
                width=settings.entry_width,
                font=settings.entry_font,
                justify="center",
                state='disabled'
            )

            entry.grid(row=row, column=col, padx=2, pady=2)
            entry.bind("<KeyRelease>", force_uppercase)

            row_inputs.append(entry)

        inputs.append(row_inputs)