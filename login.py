import sqlite3

import main
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
from addacc import acc



def main():
    win = Tk()
    obj = mlogin(win)
    win.mainloop


class mlogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Account login ")
        self.root.geometry("1050x380+235+250")
        self.pin = StringVar()
        self.acc_no = StringVar()

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
                self.app = manacc(self.new_window)

            account.commit()
            account.close()






class manacc:
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
        self.bal=StringVar()
        self.email = StringVar()

        label1 = Label(self.root, text="Manage Account", font=("Times", 30, "bold"), bg="blue", fg="white",
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

        entry_upn = Entry(main_frame, textvariable=self.name, width=40, font=("Times", 10, "bold"))
        entry_upn.place(x=0, y=50)

        bt1 = Button(main_frame, text="update name", command=self.name_update, font=("arial", 16), height=1,
                     fg="blue", cursor="hand1")
        bt1.place(x=70, y=70)

        entry_ups = Entry(main_frame, textvariable=self.sal, width=40, font=("Times", 10, "bold"))
        entry_ups.place(x=0, y=120)

        bt2 = Button(main_frame, text="update salary", command=self.sal_update, font=("arial", 16), height=1,
                     fg="blue", cursor="hand1")
        bt2.place(x=70, y=140)

        entry_upo = Entry(main_frame, textvariable=self.bal, width=40, font=("Times", 10, "bold"))
        entry_upo.place(x=0, y=195)

        bt3 = Button(main_frame, text="update balance", command=self.bal_update, font=("arial", 16), height=1,
                     fg="blue", cursor="hand1")
        bt3.place(x=70, y=220)

        entry_upp = Entry(main_frame, textvariable=self.phone, width=50, font=("Times", 10, "bold"))
        entry_upp.place(x=480, y=45)

        bt4 = Button(main_frame, text="update phone No.", command=self.phone_update, font=("arial", 16), height=1,
                     fg="blue", cursor="hand1")
        bt4.place(x=560, y=63)

        entry_upa = Entry(main_frame, textvariable=self.address, width=50, font=("Times", 10, "bold"))
        entry_upa.place(x=480, y=120)

        bt5 = Button(main_frame, text="update address", command=self.address_update, font=("arial", 16), height=1,
                     fg="blue", cursor="hand1")
        bt5.place(x=560, y=140)

        entry_upe = Entry(main_frame, textvariable=self.email, width=50, font=("Times", 10, "bold"))
        entry_upe.place(x=480, y=195)

        bt6 = Button(main_frame, text="update email id", command=self.email_update, font=("arial", 16), height=1,
                     fg="blue", cursor="hand1")
        bt6.place(x=560, y=220)

    def name_update(self):
        if self.name.get() == "" or self.acc_no.get == "":
            messagebox.showerror("Error", "empty field")
        else:
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()
            curacc.execute("update account set account_name =? where acc_no=?", (self.name.get(), self.acc_no.get()))
            account.commit()
            account.close()
            messagebox.showinfo("success", "updated", parent=self.root)

    def sal_update(self):
        if self.sal.get() == "" or self.acc_no.get == "":
            messagebox.showerror("Error", "empty field")
        else:
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()
            curacc.execute("update account set salary =? where acc_no=?", (self.sal.get(), self.acc_no.get()))
            account.commit()
            account.close()
            messagebox.showinfo("success", "updated", parent=self.root)

    def bal_update(self):
        if self.occupation.get() == "" or self.acc_no.get=="":
            messagebox.showerror("Error", "empty field")
        else:
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()
            curacc.execute("update account set balance =? where acc_no=?", (self.bal.get(), self.acc_no.get()))
            account.commit()
            account.close()
            messagebox.showinfo("success", "updated", parent=self.root)

    def phone_update(self):
        if self.phone.get() == "" or self.acc_no.get=="":
            messagebox.showerror("Error", "empty field")
        else:
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()
            curacc.execute("update account set phone_no =? where acc_no=?", (self.phone.get(), self.acc_no.get()))
            account.commit()
            account.close()
            messagebox.showinfo("success", "updated", parent=self.root)

    def address_update(self):
        if self.address.get() == "" or self.acc_no.get=="":
            messagebox.showerror("Error", "empty field")
        else:
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()
            curacc.execute("update account set address =? where acc_no=?", (self.address.get(), self.acc_no.get()))
            account.commit()
            account.close()
            messagebox.showinfo("success", "updated", parent=self.root)

    def email_update(self):
        if self.email.get() == "" or self.acc_no.get=="":
            messagebox.showerror("Error", "empty field")
        else:
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()
            curacc.execute("update account set email =? where acc_no=?", (self.email.get(), self.acc_no.get()))
            account.commit()
            account.close()
            messagebox.showinfo("success", "updated", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = mlogin(root)
    root.mainloop()
