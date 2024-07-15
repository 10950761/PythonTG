import tkinter as tk
import tkinter as ttk
win = tk.Tk()
win.title('GUI')
alable = ttk.Label(win , text = "Godfred's Lable" )
alable.grid(column= 0, row = 0)
def ClickHere():
    action.configure(text = 'Hi '  +  name.get())


ttk.Label(win, text = "Enter your name " ).grid(column= 0, row = 0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable = name)
nameEntered.grid(column=0 , row =1)

action = ttk.Button(win, text='Click Here!', command=ClickHere)
action.grid(column=2,row=1)

win.mainloop()