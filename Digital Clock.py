import tkinter as tk
import tkinter
from tkinter import *
import time as tm


def about():
    about_window = tkinter.Toplevel(app)
    about_window.title("À propos")
    about_window.geometry("250x70+900+350")
    about_window.config(background="gray")
    lb = tkinter.Label(about_window, text="\nHorloge numérique\n\n Version 1.0\n", font=("Courrier", 11),
                       bg="gray", fg="white")
    lb.pack()


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.current_time = None
        self.clock_label = None
        self.title("Digital Clock")
        self.geometry("358x35+150+25")
        self.minsize(358, 35)
        self.maxsize(358, 35)
        self.clock_display()
        self.display_time()
        self.createmenu()

    def createmenu(self):
        menubar = Menu(self)
        self.config(menu=menubar)

        files_menu = tkinter.Menu(menubar, tearoff=0)
        files_menu.add_command(label="Quitter", activebackground="red", command=quit)
        options_menu = tkinter.Menu(menubar, tearoff=0)
        options_menu.add_cascade(label="Black", command=self.clock_display)
        options_menu.add_cascade(label="Red", command=self.clock_display1)
        options_menu.add_cascade(label="Blue", command=self.clock_display2)
        options_menu.add_cascade(label="Green", command=self.clock_display3)
        options_menu.add_cascade(label="Gray", command=self.clock_display4)
        options_menu.add_cascade(label="Purple", command=self.clock_display5)
        options_menu.add_cascade(label="Orange", command=self.clock_display6)
        options_menu.add_cascade(label="Hello Kitty", command=self.clock_display7)
        options_menu.add_cascade(label="L-Blue", command=self.clock_display8)
        help_menu = tkinter.Menu(menubar, tearoff=0)
        help_menu.add_command(label="À propos", command=about)

        menubar.add_cascade(label="Fichier", menu=files_menu)
        menubar.add_cascade(label="Options", menu=options_menu)
        menubar.add_cascade(label="?", menu=help_menu)

    def clock_display(self):
        self.clock_label = tk.Label(self, font="ariel 21", bg="black", fg="red")
        self.clock_label.grid(row=0, column=0)

    def display_time(self):
        self.current_time = tm.strftime("%a, %d %b %Y  %H:%M:%S")
        self.clock_label["text"] = self.current_time
        self.after(200, self.display_time)

    def clock_display1(self):
        self.clock_label = tk.Label(self, font="ariel 21", bg="red", fg="black")
        self.clock_label.grid(row=0, column=0)

    def clock_display2(self):
        self.clock_label = tk.Label(self, font="ariel 21", bg="blue", fg="gray")
        self.clock_label.grid(row=0, column=0)

    def clock_display3(self):
        self.clock_label = tk.Label(self, font="ariel 21", bg="green", fg="black")
        self.clock_label.grid(row=0, column=0)

    def clock_display4(self):
        self.clock_label = tk.Label(self, font="ariel 21", bg="gray", fg="black")
        self.clock_label.grid(row=0, column=0)

    def clock_display5(self):
        self.clock_label = tk.Label(self, font="ariel 21", bg="DarkOrchid1", fg="black")
        self.clock_label.grid(row=0, column=0)

    def clock_display6(self):
        self.clock_label = tk.Label(self, font="ariel 21", bg="orange", fg="black")
        self.clock_label.grid(row=0, column=0)

    def clock_display7(self):
        self.clock_label = tk.Label(self, font="ariel 21", bg="PaleVioletRed1", fg="DarkOrange4")
        self.clock_label.grid(row=0, column=0)

    def clock_display8(self):
        self.clock_label = tk.Label(self, font="ariel 21", bg="light blue", fg="black")
        self.clock_label.grid(row=0, column=0)


app = App()
app.mainloop()
