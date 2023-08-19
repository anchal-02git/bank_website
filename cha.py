from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class chat:
    def __init__(self, root):
        self.root = root
        self.root.title("chatbot")
        self.root.geometry("1050x380+235+250")


if __name__ == "_main_":
    root = Tk()
    obj = chat(root)
    root.mainloop()
