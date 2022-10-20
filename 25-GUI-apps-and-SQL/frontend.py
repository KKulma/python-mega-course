from tkinter import *
import backend

def command_view():
    screen.delete(0, END)
    for row in backend.view():
        screen.insert(END, row)

def command_search():
    screen.delete(0, END)
    for row in backend.search(title=e_title_value.get(), author=e_author_value.get(), year=e_year_value.get(), isbn=e_isbn_value.get()):
        screen.insert(END,row)

def command_add():
    backend.insert(title=e_title_value.get(), author=e_author_value.get(), year=e_year_value.get(), isbn=e_isbn_value.get())
    screen.delete(0, END)
    screen.insert(END, (e_title_value.get(), e_author_value.get(), e_year_value.get(), e_isbn_value.get()))

def get_selected_row(event):
    global selected_tuple

    if len(screen.curselection())>0:
        index=screen.curselection()[0]
        selected_tuple=screen.get(index)
        e_title.delete(0, END)
        e_title.insert(END, selected_tuple[1])

        e_author.delete(0, END)
        e_author.insert(END, selected_tuple[2])

        e_year.delete(0, END)
        e_year.insert(END, selected_tuple[3])

        e_isbn.delete(0, END)
        e_isbn.insert(END, selected_tuple[4])

def command_delete():
    backend.delete(selected_tuple[0])

def command_update():
    backend.update(selected_tuple[0], e_title_value.get(), e_author_value.get(), e_year_value.get(), e_isbn_value.get())



window=Tk()

# Labels
l_title = Label(window, text='Title')
l_title.grid(row=0, column=0)

l_year = Label(window, text='Year')
l_year.grid(row=1, column=0)

l_author = Label(window, text='Author')
l_author.grid(row=0, column=2)

l_isbn = Label(window, text='ISBN')
l_isbn.grid(row=1, column=2)


## Buttons
b_view = Button(window, text='View All', width=12, command=command_view)
b_view.grid(row=2, column=3)

b_search = Button(window, text='Search entry', width=12, command=command_search)
b_search.grid(row=3, column=3)

b_add=Button(window, text='Add entry', width=12, command=command_add)
b_add.grid(row=4, column=3)

b_update=Button(window, text='Update', width=12, command=command_update)
b_update.grid(row=5, column=3)

b_delete=Button(window, text='Delete', width=12, command=command_delete)
b_delete.grid(row=6, column=3)

b_close=Button(window, text='Close', width=12, command=window.destroy)
b_close.grid(row=7, column=3)

# Entries
e_title_value = StringVar()
e_title = Entry(window, textvariable=e_title_value)
e_title.grid(row=0, column=1)

e_year_value = StringVar()
e_year = Entry(window, textvariable=e_year_value)
e_year.grid(row=1, column=1)

e_author_value = StringVar()
e_author = Entry(window, textvariable=e_author_value)
e_author.grid(row=0, column=3)

e_isbn_value = StringVar()
e_isbn = Entry(window, textvariable=e_isbn_value)
e_isbn.grid(row=1, column=3)


# listbox
screen=Listbox(window, height=6, width=35)
screen.grid(row=2, column=0, rowspan=6, columnspan=2)
screen.bind('<<ListboxSelect>>', get_selected_row)

scroll=Scrollbar(window)
scroll.grid(row=2, column=2)

screen.configure(yscrollcommand=scroll.set)
scroll.configure(command=screen.yview)


window.mainloop()

