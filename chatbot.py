from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random





class blogin:
    def __init__(self, root):
        self.root = root
        self.root.title("chatbot ")
        self.root.geometry("1050x380+235+250")


        label1 = Label(self.root, text="Chat with us", font=("Times", 30, "bold"), bg="blue", fg="white",
                       bd=2, )
        label1.place(x=0, y=0, width=1050, height=50)

        img2 = Image.open("C:\\Users\\HP\OneDrive\\Desktop\\bankmanagement\\chatbot.png")
        img2 = img2.resize((200, 80))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=200, height=80)
        # main frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=65, width=1050, height=320)



if __name__ == "__main__":
    root = Tk()
    obj = blogin(root)
    root.mainloop()


