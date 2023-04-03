from tkinter import *
import customtkinter
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)
        
def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
    
def delete_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
      
    

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("green")

app=customtkinter.CTk()
app.geometry("500*350")

label1=customtkinter.CTkLabel(app,text="Title" )
label1.grid(row=0,column=0)

label2=customtkinter.CTkLabel(app,text="Author" )
label2.grid(row=0,column=2)

label3=customtkinter.CTkLabel(app,text="Year" )
label3.grid(row=1,column=0)

label4=customtkinter.CTkLabel(app,text="ISBN" )
label4.grid(row=1,column=2) 

title_text=StringVar()
e1= customtkinter.CTkEntry(app, textvariable=title_text, placeholder_text="Book Title")
e1.grid(row=0, column=1)

author_text=StringVar()
e2= customtkinter.CTkEntry(app, textvariable=author_text, placeholder_text="Book Author")
e2.grid(row=0, column=3)

year_text=StringVar()
e3= customtkinter.CTkEntry(app, textvariable=year_text, placeholder_text="Book Year")
e3.grid(row=1, column=1)


isbn_text=StringVar()
e4= customtkinter.CTkEntry(app, textvariable=isbn_text, placeholder_text="Book ISBN")
e4.grid(row=1, column=3)

list1=Listbox(app,height=15, width=45 )
list1.grid(row=3,column=0, rowspan=6, columnspan=2)

sb1=customtkinter.CTkScrollbar(app,hover=True)
sb1.grid(row=2,column=2,rowspan=7)


list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = customtkinter.CTkButton(app,text="View All", width=12, command=view_command)
b1.grid(row=3,column=3)

b2 = customtkinter.CTkButton(app,text="Search Book", width=12, command=search_command)
b2.grid(row=4,column=3)

b3 = customtkinter.CTkButton(app,text="Add Book", width=12, command=add_command)
b3.grid(row=5,column=3)

b4 = customtkinter.CTkButton(app,text="Update", width=12)
b4.grid(row=6,column=3)

b5 = customtkinter.CTkButton(app,text="Delete", width=12)
b5.grid(row=7,column=3)

b6 = customtkinter.CTkButton(app,text="Close", width=12)
b6.grid(row=8,column=3)

app.mainloop()