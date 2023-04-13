from tkinter import *
class MyFullName:
    def __init__(self, win):

        self.lbl1 = Label(win, text="My Full Name", fg="Red")
        self.lbl1.place(x=175, y=10)

        self.lbl2 = Label(win, text="First name:", fg="Red")
        self.lbl2.place(x=100, y=50)
        self.given_name = Entry(win, bd=1)
        self.given_name.place(x=220, y=50)

        self.lbl3 = Label(win, text="Middle name:", fg="Red")
        self.lbl3.place(x=100, y=100)
        self.middle_name = Entry(win, bd=2)
        self.middle_name.place(x=220, y=100)

        self.lbl4 = Label(win, text="Last name:", fg="Red")
        self.lbl4.place(x=100, y=150)
        self.last_name = Entry(win, bd=3)
        self.last_name.place(x=220, y=150)

        self.lbl5 = Label(win, text="Full name is:", fg="Red")
        self.lbl5.place(x=100, y=200)
        self.full_name = Entry(win, bd=4)
        self.full_name.place(x=220, y=200)

        self.full = Button(win, text="Show Full name", fg="Black")
        self.full.place(x=175, y=250)
        self.full.bind('<Button-1>', self.FullName)

        self.clear = Button(win, text="Clear Full name", fg="Black")
        self.clear.place(x=175, y=280)
        self.clear.bind('<Button-1>', self.clear_all)




    def FullName(self, Full):
        LastName = str(self.last_name.get())

        Firstname = str(self.given_name.get())

        MiddleName = str(self.middle_name.get())

        FullName = Firstname + " " + MiddleName + " " + LastName
        self.full_name.insert(END, str(FullName),)

    def clear_all(self, Clear):
        self.given_name.delete()
        self.middle_name.delete()
        self.last_name.delete()
        self.full_name.delete()



FullName = Tk()
mywin = MyFullName(FullName)
FullName.geometry("600x400+10+10")
FullName.title("Midterm Exam Problem 2")
FullName.mainloop()
