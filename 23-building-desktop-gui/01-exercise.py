from tkinter import *

def convert_from_kg():
    val= float(e1_value.get())
    grams=val*1000
    pounds=val*2.20462
    ounces=val*35.274

    t_g.delete("1.0", END)
    t_p.delete("1.0", END)
    t_o.delete("1.0", END)

    t_g.insert(END, grams)
    t_p.insert(END, pounds)
    t_o.insert(END, ounces)

window = Tk()

b1 = Button(window, text='Convert', command=convert_from_kg)
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

l1 = Label(window, text="Kg").grid(row=0, column=0)

t_g = Text(window, height=1, width=2)
t_g.grid(row=1, column=0)

t_p = Text(window, height=1, width=2)
t_p.grid(row=1, column=1)

t_o = Text(window, height=1, width=2)
t_o.grid(row=1, column=2)

window.mainloop()