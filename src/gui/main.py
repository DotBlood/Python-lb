from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root['bg'] = "#F183F1"
combo = Combobox(root)

root.title("ZOV")
root.geometry("720x720")

l1 = Label(text="Label", font="Arial 60", background="#F183F1")
l1.place(x=250, y=275)

e = Entry(root, background="#E29DE2")
e.place(x=250, y=360, width=195, height=25)
buttonOK = Button(root, text="OK", background="#E29DE2")
buttonOK.place(x=450, y=360, width=50, height=25)

pythonX = ['USD', 'EUR']
lbox1 = Combobox(root, values=pythonX)
lbox1.place(x=300, y=390, width=50, height=25)
lbox2 = Combobox(root, values=pythonX)
lbox2.place(x=360, y=390, width=50, height=25)

root.mainloop()