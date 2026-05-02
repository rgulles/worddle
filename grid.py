from tkinter import Entry, END

def handle_grid_input(event):
    entry = event.widget
    value = entry.get()

    parent = entry.master
    entries = parent.grid_slaves()
    entries = sorted(entries, key=lambda e: (e.grid_info()["row"], e.grid_info()["column"]))

    index = None
    for i, e in enumerate(entries):
        if e == entry:
            index = i
            break

    if event.keysym == "BackSpace":
        if value == "":
            if index is not None and index > 0:
                prev_entry = entries[index - 1]
                prev_entry.delete(0, END)
                prev_entry.focus_set()
        else:
            entry.delete(0, END)
        return

    if value:
        value = value[-1].upper()
        entry.delete(0, END)
        entry.insert(0, value)

        if index is not None and index + 1 < len(entries):
            next_entry = entries[index + 1]
            next_entry.focus_set()

def validate_input(P):
    if P == "":
        return True
    return P.isalpha() and len(P) == 1

def create_grid(frame, settings, inputs):
    rows = settings.rows
    cols = settings.easy_cols

    vcmd = frame.register(validate_input)

    for row in range(rows):
        row_inputs = []

        for col in range(cols):
            entry = Entry(
                frame,
                width=settings.entry_width,
                font=settings.entry_font,
                justify="center",
                state='disabled',
                validate="key",
                validatecommand=(vcmd, "%P")
            )

            entry.grid(row=row, column=col, padx=2, pady=2)
            entry.bind("<KeyRelease>", handle_grid_input)

            row_inputs.append(entry)

        inputs.append(row_inputs)