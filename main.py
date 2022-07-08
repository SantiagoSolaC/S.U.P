from tkinter import *
from tk_study import Window


class Principal():

    def __init__(self, windows):
        self.root_principal = windows
        Window(self.root_principal)


if __name__ == "__main__":
    root = Tk()
    obj = Principal(root)
    root.mainloop()
