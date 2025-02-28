#coding:utf-8
import customtkinter
from customtkinter import *
import tkinter
from tkinter import ttk
import mysql.connector

addfen = customtkinter.CTk()
addfen.geometry("800x400")
addfen.title("Add Student")

def sean():
    donnee = rech.get()
    print(donnee)


def voir():
    tab = tableau.selection()
    print(tab)


rech = customtkinter.CTkEntry(master=addfen,placeholder_text="Chercher quelque chose ici",width=400)


btn = customtkinter.CTkButton(addfen,text="valider",command=sean)

rech.pack(pady=10)
btn.place(x=650,y=10)




con = mysql.connector.connect(host="localhost",database="pagination",user = "root", password = "")
curos = con.cursor()
curos.execute("SELECT * FROM personne")
results = curos.fetchall()
    
    


tableau = ttk.Treeview(master=addfen,columns=(1,2,3,4),height=5,show="headings",cursor="hand2")

tableau.heading(1,text="Id",anchor="center")
tableau.heading(2,text="Nom",anchor="center")
tableau.heading(3,text="Prenom",anchor="center")
tableau.heading(4,text="Adresse",anchor="center")


tableau.column(1,width=50,anchor="center")



for row in results:
    tableau.insert("",END,values=row)

tableau.pack(padx=10,pady=20,ipadx=5,ipady=5)



tableau.bind("<Return>",lambda e:voir())


con.commit()
con.close()


if __name__ == '__main__':
    addfen.mainloop()
    
