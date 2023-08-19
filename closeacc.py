import sqlite3

import main
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
from addacc import acc


def main():
    win = Tk()
    obj = clogin(win)
    win.mainloop


class clogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Account login ")
        self.root.geometry("1050x380+235+250")
        self.pin = StringVar()
        self.acc_no = StringVar()
        self.bal = StringVar()

        label1 = Label(self.root, text="New Account Registration ", font=("Times", 30, "bold"), bg="blue", fg="white",
                       bd=2, )
        label1.place(x=0, y=0, width=1050, height=50)

        img2 = Image.open("C:\\Users\\HP\OneDrive\\Desktop\\bankmanagement\\logobank.png")
        img2 = img2.resize((200, 60))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=200, height=60)
        # main frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=65, width=1050, height=320)
        label_acc_no = Label(main_frame, text="Account No.", font=("Times New Roman", 12, "bold"), padx=2,
                             pady=6)
        label_acc_no.place(x=400, y=55)

        entry_acc_no = Entry(main_frame, textvariable=self.acc_no, width=30, font=("Times", 10, "bold"))

        entry_acc_no.place(x=370, y=80)

        label_pin = Label(main_frame, text="pin", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_pin.place(x=400, y=100)

        entry_pin = Entry(main_frame, textvariable=self.pin, width=20, font=("Times", 10, "bold"))
        entry_pin.place(x=370, y=130)

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=380, y=170, width=70, height=50)

        bt1 = Button(btn_frame, text="login", command=self.log_data, font=("arial", 16), height=1,
                     bg="black", fg="gold", cursor="hand1")
        bt1.grid(row=0, column=0, padx=1)

        bt2 = Button(main_frame, text="new user register", command=self.new_acc, font=("arial", 16), height=1,
                     bg="black", fg="gold", cursor="hand1")
        bt2.place(x=350, y=240)

    def new_acc(self):
        self.new_window = Toplevel(self.root)
        self.app = acc(self.new_window)

    def log_data(self):
        if self.acc_no.get() == "" or self.pin.get() == "":
            messagebox.showerror("Error", "all fields are required")
        else:
            pass
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()
            curacc.execute("select * from account where acc_no =? and pin_no=?", (self.acc_no.get(), self.pin.get()))
            row = curacc.fetchone()
            if row is None:
                messagebox.showerror("Error", "User not registered")
            else:
                self.new_window = Toplevel(self.root)
                self.app = close(self.new_window)

            account.commit()
            account.close()


class close:
    def __init__(self, root):
        self.root = root
        self.root.title("Account Manage ")
        self.root.geometry("1050x380+235+250")
        # variables
        self.name = StringVar()
        self.acc_no = StringVar()
        self.sal = StringVar()
        self.address = StringVar()
        self.phone = StringVar()

        self.occupation = StringVar()
        self.email = StringVar()

        label1 = Label(self.root, text="Account Details", font=("Times", 30, "bold"), bg="blue", fg="white",
                       bd=2, )
        label1.place(x=0, y=0, width=1050, height=50)

        img2 = Image.open("C:\\Users\\HP\OneDrive\\Desktop\\bankmanagement\\logobank.png")
        img2 = img2.resize((200, 60))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=200, height=60)
        # main frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=65, width=1050, height=320)
        label_acc_no = Label(main_frame, text="Account No", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_acc_no.grid(row=0, column=0, sticky=W)
        # entry  boxes

        entry_acc_no = Entry(main_frame, textvariable=self.acc_no, width=30, font=("Times", 10, "bold"))
        entry_acc_no.grid(row=0, column=1)

        bt2 = Button(main_frame, text="check balance", command=self.close_account, font=("arial", 16), height=1,
                     fg="blue", cursor="hand1")
        bt2.place(x=00, y=140)

    def close_account(self):
        if self.acc_no.get == "":
            messagebox.showerror("Error", "empty field")
        else:
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()
            curacc.execute("delete  from account where acc_no =? ", ( self.acc_no.get()))
            messagebox.showinfo("success", "account is closed", parent=self.root)

            account.commit()
            account.close()


if __name__ == "__main__":
    root = Tk()
    obj = clogin(root)
    root.mainloop()
