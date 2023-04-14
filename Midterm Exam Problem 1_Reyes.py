from tkinter import *

class MyWindow:

    def __init__(self, win):
        self.lbl1 = Label(win, text='Given Name:', font=('Verdana', 12), fg='red', anchor='center')
        self.lbl1.place(x=50, y=50)

        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=200, y=50)

        self.lbl2 = Label(win, text='Middle Name:', font=('Verdana', 12), fg='red', anchor='center')
        self.lbl2.place(x=50, y=100)

        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=200, y=100)

        self.lbl3 = Label(win, text='Last Name:', font=('Verdana', 12), fg='red', anchor='center')
        self.lbl3.place(x=50, y=150)

        self.txt3 = Entry(win, bd=1)
        self.txt3.place(x=200, y=150)

        self.lbl4 = Label(win, text='Full Name:', font=('Verdana', 12), fg='red', anchor='center')
        self.lbl4.place(x=50, y=200)

        self.txt4 = Entry(win, bd=1)
        self.txt4.place(x=200, y=200)

        self.btnadd = Button(win, text='Show Full Name')
        self.btnadd.place(x=200, y=250)
        self.btnadd.bind('<Button-1>', self.add)

    def add(self, event):
        self.txt4.delete(0, 'end')
        num1 = str(self.txt1.get())
        num2 = str(self.txt2.get())
        num3 = str(self.txt3.get())
        result = num1 + ' ' + num2 + ' ' + num3
        self.txt4.insert(END, str(result))

window = Tk()
mywin = MyWindow(window)
window.geometry('400x300+10+10')
window.title('My Full Name')
window.mainloop()


