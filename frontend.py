from tkinter import StringVar
import customtkinter

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("green")

root=customtkinter.CTk()
root.geometry("500*350")

label1=customtkinter.CTkLabel(root,text="Title" )
label1.grid(row=0,column=0)

label2=customtkinter.CTkLabel(root,text="Author" )
label2.grid(row=0,column=2)

label3=customtkinter.CTkLabel(root,text="Year" )
label3.grid(row=1,column=0)

label4=customtkinter.CTkLabel(root,text="ISBN" )
label4.grid(row=1,column=2) 

title_text=StringVar()
e1= customtkinter.CTkEntry(root, textvariable=title_text, placeholder_text="Book Title")
e1.grid(row=0, column=1)

author_text=StringVar()
e2= customtkinter.CTkEntry(root, textvariable=author_text, placeholder_text="Book Author")
e2.grid(row=0, column=3)

year_text=StringVar()
e3= customtkinter.CTkEntry(root, textvariable=year_text, placeholder_text="Book Year")
e3.grid(row=1, column=1)


isbn_text=StringVar()
e4= customtkinter.CTkEntry(root, textvariable=isbn_text, placeholder_text="Book ISBN")
e4.grid(row=1, column=3)

list1=customtkinter.CTkScrollableFrame(root,height=5, width=180 )
list1.grid(row=2,column=0, rowspan=6, columnspan=3)

b1 = customtkinter.CTkButton(root,text="View All", width=12)
b1.grid(row=2,column=3)

b2 = customtkinter.CTkButton(root,text="Search Book", width=12)
b2.grid(row=3,column=3)

b3 = customtkinter.CTkButton(root,text="Add Book", width=12)
b3.grid(row=4,column=3)

b4 = customtkinter.CTkButton(root,text="Update", width=12)
b4.grid(row=5,column=3)

b5 = customtkinter.CTkButton(root,text="Delete", width=12)
b5.grid(row=6,column=3)

b6 = customtkinter.CTkButton(root,text="Close", width=12)
b6.grid(row=7,column=3)

root.mainloop()