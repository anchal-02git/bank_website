import sqlite3

import main
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random


class acc:
    def __init__(self, root):

        self.root = root
        self.root.title("Account login ")
        self.root.geometry("1050x380+235+250")
        # variables
        self.name = StringVar()
        self.age = StringVar()
        self.sal = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.nationality = StringVar()
        self.type = StringVar()
        self.gender = StringVar()
        self.occupation = StringVar()
        self.email = StringVar()
        self.aadharnumber = StringVar()
        self.pin = StringVar()
        self.cpin = StringVar()
        self.bal = StringVar()
        self.acc_no = StringVar()
        x = random.randint(10000000, 99999999)
        self.acc_no.set(str(x))

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
        label_name = Label(main_frame, text="Name", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_name.grid(row=0, column=0, sticky=W)
        # entry  boxes

        entry_name = Entry(main_frame, textvariable=self.name, width=30, font=("Times", 10, "bold"))
        entry_name.grid(row=0, column=1)

        label_age = Label(main_frame, text="age", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_age.grid(row=1, column=0, sticky=W)

        entry_age = Entry(main_frame, textvariable=self.age, width=30, font=("Times", 10, "bold"))
        entry_age.grid(row=1, column=1)

        label_salary = Label(main_frame, text="salary", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_salary.grid(row=2, column=0, sticky=W)

        entry_salary = Entry(main_frame, textvariable=self.sal, width=30, font=("Times", 10, "bold"))
        entry_salary.grid(row=2, column=1)

        label_type = Label(main_frame, text="account type", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_type.place(x=480, y=78)

        sacc_type = Checkbutton(main_frame, text="Savings account", onvalue="Savings account", variable=self.type,
                                font=("Times", 10, "bold"))
        sacc_type.place(x=570, y=78)
        sacc_type.deselect()
        facc_type = Checkbutton(main_frame, text="Fixed deposit account", onvalue="Fixed deposit account",
                                variable=self.type,
                                font=("Times", 10, "bold"))
        facc_type.place(x=700, y=78)
        facc_type.deselect()
        racc_type = Checkbutton(main_frame, text="Recurring deposit account", onvalue="Recurring deposit account",
                                variable=self.type,
                                font=("Times", 10, "bold"))
        racc_type.place(x=850, y=78)
        racc_type.deselect()
        cacc_type = Checkbutton(main_frame, text="Current account", onvalue="Current account", variable=self.type,
                                font=("Times", 10, "bold"))
        cacc_type.place(x=600, y=97)
        cacc_type.deselect()
        nacc_type = Checkbutton(main_frame, text="NRI account", onvalue="NRI account", variable=self.type,
                                font=("Times", 10, "bold"))
        nacc_type.place(x=800, y=98)
        nacc_type.deselect()

        label_gender = Label(main_frame, text="gender", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_gender.place(x=480, y=3)
        # radio button

        r1 = Radiobutton(main_frame, text="male", value="male", variable=self.gender, font=("Times", 10, "bold"))
        r1.select()
        r2 = Radiobutton(main_frame, text="female", value="female", variable=self.gender, font=("Times", 10, "bold"))
        r2.deselect()
        r1.place(x=540, y=4)
        r2.place(x=600, y=4)

        label_occupation = Label(main_frame, text="occupation", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_occupation.grid(row=5, column=0, sticky=W)

        entry_occupation = Entry(main_frame, textvariable=self.occupation, width=30, font=("Times", 10, "bold"))
        entry_occupation.grid(row=5, column=1)

        label_nationality = Label(main_frame, text="nationality", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_nationality.grid(row=6, column=0, sticky=W)

        entry_nationality = Entry(main_frame, textvariable=self.nationality, width=30, font=("Times", 10, "bold"))
        entry_nationality.grid(row=6, column=1)

        label_address = Label(main_frame, text="Residential Address", font=("Times New Roman", 12, "bold"), padx=2,
                              pady=6)
        label_address.place(x=440, y=147)

        entry_address = Entry(main_frame, textvariable=self.address, width=55, font=("Times", 10, "bold"))

        entry_address.place(x=610, y=150)

        label_phone = Label(main_frame, text="phone number", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_phone.grid(row=7, column=0, sticky=W)

        entry_phone = Entry(main_frame, textvariable=self.phone, width=30, font=("Times", 10, "bold"))
        entry_phone.grid(row=7, column=1)

        label_email = Label(main_frame, text="email id", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_email.place(x=480, y=183)

        entry_email = Entry(main_frame, textvariable=self.email, width=30, font=("Times", 10, "bold"))
        entry_email.place(x=550, y=186)

        label_aadharnumber = Label(main_frame, text="Aadhar card number", font=("Times New Roman", 12, "bold"), padx=2,
                                   pady=6)
        label_aadharnumber.grid(row=8, column=0, sticky=W)

        entry_aadharnumber = Entry(main_frame, textvariable=self.aadharnumber, width=30, font=("Times", 10, "bold"))
        entry_aadharnumber.grid(row=8, column=1)

        label_acc_no = Label(main_frame, text="account No.", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_acc_no.place(x=460, y=210)

        entry_acc_no = Entry(main_frame, textvariable=self.acc_no, width=30, font=("Times", 10, "bold"))
        entry_acc_no.place(x=550, y=220)

        label_pin_no = Label(main_frame, text="pin No.", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_pin_no.place(x=0, y=240)

        entry_pin_no = Entry(main_frame, textvariable=self.pin, width=20, font=("Times", 10, "bold"))
        entry_pin_no.place(x=70, y=250)

        label_cpin_no = Label(main_frame, text="Confirm pin No.", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_cpin_no.place(x=240, y=240)

        entry_cpin_no = Entry(main_frame, textvariable=self.cpin, width=20, font=("Times", 10, "bold"))
        entry_cpin_no.place(x=350, y=250)

        label_balance = Label(main_frame, text="Balance", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        label_balance.place(x=520, y=240)

        entry_balance = Entry(main_frame, textvariable=self.bal, width=20, font=("Times", 10, "bold"))
        entry_balance.place(x=580, y=250)

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=800, y=250, width=185, height=50)

        bt1 = Button(btn_frame, text="Add new account", command=self.add_data, font=("arial", 16), height=1,
                     bg="black", fg="gold", cursor="hand1")
        bt1.grid(row=0, column=0, padx=1)

    # add account
    def add_data(self):
        if self.name.get() == "" or self.age.get() == "" or self.sal.get() == "" or self.bal.get() == "" or self.occupation.get() == "" or self.nationality.get() == "" or self.phone.get() == "" or self.address.get() == "" or self.aadharnumber.get() == "" or self.type.get() == "":
            messagebox.showerror("Error", "all fields are required")


        else:

            pass
            account = sqlite3.connect('accounts.db')
            curacc = account.cursor()

            query = "select * from account where phone_no=? and account_type=?"
            value = (self.phone.get(), self.type.get())
            curacc.execute(query, value)
            row = curacc.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists")
            elif self.pin.get() != self.cpin.get():
                messagebox.showerror("Error", "both pin doesn't match")

            else:

                curacc.execute("INSERT INTO account values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                    self.name.get(), self.age.get(), self.sal.get(), self.gender.get(), self.occupation.get(),
                    self.nationality.get(), self.phone.get(), self.address.get(), self.email.get(),
                    self.aadharnumber.get(),
                    self.type.get(), self.acc_no.get(), self.pin.get(), self.bal.get()))

                account.commit()
                account.close()

                messagebox.showinfo("success", "account created", parent=self.root)


if __name__ == "_main_":
    root = Tk()
    obj = acc(root)
    root.mainloop()
