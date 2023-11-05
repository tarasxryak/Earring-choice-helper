from tkinter import *
from tkinter import Tk
from tkinter import ttk
import random as r
from tkinter.messagebox import showinfo
from collections import Counter
import os


app = Tk()
enabled = IntVar()
enabled2 = IntVar()

# Earrings list
nabor_seryog = [
    "KPECT (для хуесосов)",
    "Обычная точка...",
    "Бритва(порежься)",
    "СЛОН",
    "Горилла для Хабиба",
    "Птичка",
    "Порватое за птичку ухо"
]


# Random choice func
def rand_sergya():
    sp = []
    if enabled.get() == 1:
        for i in range(int(entry_field.get())):
            sp.append(nabor_seryog[r.randint(0, 6)])
        spd = dict(Counter(sp))
        for i in spd:
            if spd.get(i) == max(dict(Counter(sp)).values()):
                showinfo(message=f'Серьга на сегодня: {i}({max(dict(Counter(sp)).values())})', title='СЕРЬГА')
                sp.clear()
                return
    else:
        showinfo(message=f'Серьга на сегодня: {nabor_seryog[r.randint(0, 6)]}', title='СЕРЬГА')
        sp.clear()
        return


def create_entry():
    if enabled.get() == 1:
        entry_field.place(x=0, y=20)
    elif enabled.get() == 0:
        entry_field.place_forget()


def musik():
    if enabled2.get() == 1:
        file = 'megaImba.mp3'
        os.system(file)


# App config
app.title("Сережки для Андрея")
app.geometry('480x360')
app.resizable(False, False)
app.iconbitmap(default="lgbt.ico")


# Widgets
entry_field = Entry()

check_btn = ttk.Checkbutton(text="Использовать несколько вводов", variable=enabled, command=create_entry)
check_btn.place(x=0, y=0)

funcone_btn = ttk.Button(text='Крутить', command=rand_sergya)
funcone_btn.pack(fill=X, pady=150)

musik_butn = ttk.Checkbutton(text='Включить расслабляющую музыку', variable=enabled2, command=musik)
musik_butn.place(x=140, y=180)


app.mainloop()
