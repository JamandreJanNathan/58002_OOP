from tkinter import *
class MyWindow:
    def __init__(self,win):
        self.lbl1 = Label(win, text="TempConversion")
        self.lbl1.place(x=250, y=30)
        self.lbl1 = Label(win,text="Enter Temparature:")
        self.lbl1.place(x=100,y=80)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100,y=150)
        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=210,y=80)
        self.txt2 = Entry(win,bd=3)
        self.txt2.place(x=200,y=150)
        self.btnfahrtocel = Button(win,text="Fahrenheit to Celsius", fg = "Black")
        self.btnfahrtocel.place(x=100,y=200)
        self.btnfahrtocel.bind('<Button-1>',self.fahrtocel)
        self.btnkelvtocel = Button(win,text="Kelvin to Celsius", fg = "Black",command = self.kelvtocel)
        self.btnkelvtocel.place(x=300,y=200)
        self.btnclr = Button(win,text="Clear",fg = "Black",command= self.clr)
        self.btnclr.place(x=400,y=100)
        self.btnfahrtokel = Button(win, text="Fahrenheit to Kelvin", fg="Black")
        self.btnfahrtokel.place(x=100, y=230)
        self.btnfahrtokel.bind('<Button-1>', self.fahrtokel)
        self.keltofah = Button(win, text="Kelvin to Fahrenheit", fg="Black")
        self.keltofah.place(x=300, y=230)
        self.keltofah.bind('<Button-1>', self.keltofahr)
        self.celtokelv = Button(win, text="Celsius to Kelvin", fg="Black")
        self.celtokelv.place(x=300, y=260)
        self.celtokelv.bind('<Button-1>', self.celtokel)
        self.btnceltofahr = Button(win, text="Celsius to Fahrenheit", fg="Black")
        self.btnceltofahr.place(x=100, y=260)
        self.btnceltofahr.bind('<Button-1>', self.celtofahr)



    def celtofahr(self,celtofahr):
        self.txt2.delete(0, 'end')
        num1 = int(self.txt1.get())
        result = (num1*9/5)+32
        self.txt2.insert(END, str(result))



    def celtokel(self,celtokel):
        self.txt2.delete(0, 'end')
        num1 = int(self.txt1.get())
        result = (num1+273.15)
        self.txt2.insert(END, str(result))



    def keltofahr(self, keltofahr):
        self.txt2.delete(0, 'end')
        num1 = int(self.txt1.get())
        result = (num1-273.15)*9/5+32
        self.txt2.insert(END, str(result))



    def fahrtokel(self,fahrtokel):
        self.txt2.delete(0,'end')
        num1 = int(self.txt1.get())
        result = (num1-32)*5/9+273.15
        self.txt2.insert(END,str(result))

    def fahrtocel(self,fahrtocel):
        self.txt2.delete(0,'end')
        num1 = int(self.txt1.get())
        result = (num1-32)*.556
        self.txt2.insert(END,str(result))

    def kelvtocel(self):
        self.txt2.delete(0, 'end')
        num1 = int(self.txt1.get())
        result = num1-273.15
        self.txt2.insert(END, str(result))

    def clr(self):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')



window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Conversion Methods")
window.mainloop()