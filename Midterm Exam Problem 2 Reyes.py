from tkinter import *

class MyWindow:

    def __init__(self, win):
        self.lbl1 = Label (win, text='Centimeter', font=('Verdana', 12), fg='blue')
        self.lbl1.place(x=50,y=50)

        self.txt1= Entry(win,bd=1)
        self.txt1.place(x=200,y=50)

        self.lbl2 = Label(win, text='Meters', font=('Verdana', 12), fg='blue')
        self.lbl2.place(x=50, y=100)

        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=200, y=100)

        self.lbl3 = Label(win, text='Kilometer', font=('Verdana', 12), fg='blue')
        self.lbl3.place(x=50, y=150)

        self.txt3 = Entry(win, bd=1)
        self.txt3.place(x=200, y=150)

        self.btnadd = Button(win, text='Convert')
        self.btnadd.place(x=200, y=250)
        self.btnadd.bind('<Button-1>', self.convert)

    def convert(self, event):
        self.txt1.delete(0,'end')
        num1= int(self.txt1.get())
        resultmeter = num1 / 100
        resultkilometer = num1 / 100000
        self.txt2.insert(END, str(resultmeter))
        self.txt3.insert(END,str(resultkilometer))

window = Tk()
mywin = MyWindow(window)
window.geometry('400x300+10+10')
window.title('Convertion')
window.mainloop()