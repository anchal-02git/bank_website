import sqlite3

import main
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

account = sqlite3.connect('accounts.db')
curacc = account.cursor()


class manacc:
    def __init__(self, root):
        self.root = root
        self.root.title(" Manage Account ")
        self.root.geometry("1050x380+235+250")
        # variables
        self.name = StringVar()
        self.acc_no = StringVar()
        self.sal = StringVar()
        self.address = StringVar()
        self.phone = StringVar()

        self.occupation = StringVar()
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

        entry_upo = Entry(main_frame, textvariable=self.occupation, width=40, font=("Times", 10, "bold"))
        entry_upo.place(x=0, y=195)

        bt3 = Button(main_frame, text="update occupation", command=self.occupation_update, font=("arial", 16), height=1,
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

    def occupation_update(self):
        if self.occupation.get() == "" or self.acc_no.get=="":
            messagebox.showerror("Error", "empty field")
        else:
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()
            curacc.execute("update account set occupation =? where acc_no=?", (self.occupation.get(), self.acc_no.get()))
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
    obj = manacc(root)
    root.mainloop()
