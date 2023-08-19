
from tkinter import *

from PIL import Image, ImageTk
from addacc import acc
from login import mlogin
from balance import blogin
from closeacc import clogin


class bankmanagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Website")
        self.root.geometry("1550x100+0+0")
        self.root.state('zoomed')

        img1 = Image.open("C:\\Users\\HP\OneDrive\\Desktop\\bankmanagement\\bankimg.png")
        img1 = img1.resize((1550, 160))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=160)
        # ********
        img2 = Image.open("C:\\Users\\HP\OneDrive\\Desktop\\bankmanagement\\logobank.png")
        img2 = img2.resize((300, 160))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=300, height=160)

        label1 = Label(self.root, text="BANK WEBSITE ", font=("Times", 40, "bold"), bg="black", fg="gold", bd=4,
                       relief=RIDGE)
        label1.place(x=0, y=160, width=1500, height=50)

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=210, width=1500, height=620)
        # ******menu*********
        label_menu = Label(main_frame, text="options", font=("Times", 20, "bold"), bg="black", fg="gold", bd=4,
                           relief=RIDGE)
        label_menu.place(x=0, y=0, width=230)

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=40, width=228, height=250)

        bt1 = Button(btn_frame, text="Add new account", command=self.new_acc, font=("Times", 16), height=2, width=17,
                     bg="blue", fg="gold", cursor="hand1")
        bt1.grid(row=0, column=0)

        bt2 = Button(btn_frame, text="Manage Account",command=self.mlog_acc, font=("Times", 16), height=2, width=17, bg="blue", fg="gold",
                     cursor="hand1")
        bt2.grid(row=1, column=0)

        bt3 = Button(btn_frame, text="Balance Update",command=self.blog_acc, font=("Times", 16), height=2, width=17, bg="blue", fg="gold",
                     cursor="hand1")
        bt3.grid(row=2, column=0)

        bt4 = Button(btn_frame, text="Close Account",command=self.clog_acc, font=("Times", 16), height=2, width=17, bg="blue", fg="gold",
                     cursor="hand1")
        bt4.grid(row=3, column=0, pady="1")

        img3 = Image.open("C:\\Users\\HP\OneDrive\\Desktop\\bankmanagement\\family.png")
        img3 = img3.resize((1310, 520))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=235, y=0, width=1050, height=420)

        img4 = Image.open("C:\\Users\\HP\OneDrive\\Desktop\\bankmanagement\\onlinebank.png")
        img4 = img4.resize((228, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=300, width=228, height=130)

    def new_acc(self):
          self.new_window=Toplevel(self.root)
          self.app=acc(self.new_window)


    def mlog_acc(self):
        self.mlog_window = Toplevel(self.root)
        self.man = mlogin(self.mlog_window)


    def blog_acc(self):
        self.blog_window = Toplevel(self.root)
        self.bal = blogin(self.blog_window)

    def clog_acc(self):
        self.blog_window = Toplevel(self.root)
        self.bal = clogin(self.blog_window)









if __name__ == "__main__":
    root = Tk()
    obj = bankmanagement(root)
    root.mainloop()
