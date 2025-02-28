#coding:utf-8
import tkinter
import tkinter.ttk
import customtkinter
from tkinter import *
import PIL
from PIL import *
from PIL import Image,ImageTk
from customtkinter import *
import mysql.connector
import couleur
from tkinter import messagebox,ttk,Frame
import os
from os import *
import pdf2docx
import connexionbase

app = tkinter.Tk()
app.title("Bienevenue sur Minesoft")
app.resizable(True,False)
app.geometry("1200x650")
app.config(bg=couleur.white_bac)

#icon du logiciel
imgico = PhotoImage(file="image/book.png")
app.iconphoto(False,imgico)
#fin du logo du lociel


"""debut des fonction pour notre application de buraeu c a d que tous les fonction seront stocter en bas de cette commentaire
"""
def quitter():
    tester = messagebox.askquestion("Etez-Vous sur ?","Vous etez sur de quitter....?")
    if tester == "yes":
        app.quit()
    else:
        pass
    

def faculte_un():
    addfen = customtkinter.CTk()
    addfen.geometry("800x600")
    addfen.title("Add Student")
    addfen.config(background="#fff")

    #fonction de validation
    def valid():
        nom_fac = str(nom_entry.get())
        prenom_fac = str(prenom_entry.get())
        matricule_fac = str(matricule_entry.get())
        campus_fac = str(campus.get())
        departement_fac = str(departement_entry.get())
        facult_fac = str(faculte_entry.get())
        annee = 1
        tra1 = 'non'
        tra2 = 'non'
        tra3 = 'non'
        if nom_fac == "" or prenom_fac == "" or matricule_fac == "":
            print("veiller completer les cases vides")
        else:
            print("script commence... a execute")
            conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
            ajout = conn.cursor()
            
            rep = "INSERT INTO faculte_un(nom,prenom,matricule,campus,departement,faculte,annee,tra1,tra2,tra3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            ajout.execute(rep,(nom_fac,prenom_fac,matricule_fac,campus_fac,departement_fac,facult_fac,annee,tra1,tra2,tra3))
            if ajout:
                messagebox.showinfo("Valider",'Etudiant ajoute')
                #supprension des donnees dans les entrees
                nom_entry.delete(0,END)
                prenom_entry.delete(0,END)
                matricule_entry.delete(0,END)

            

            conn.commit()
            conn.close()
            
            
        
    #en bas de la fonction de validation


    labe = customtkinter.CTkLabel(master=addfen,text="Add Student in Fac 1",fg_color="#fff",text_color="#809A50",font=('sans-serif',20),
                              )

    nom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Nom..",width=400,height=40,bg_color="#fff",
                                   fg_color="#fff",text_color="#000")
    prenom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Prenom...",width=400,height=40,bg_color="#fff",
                                      fg_color="#fff",text_color="#000")
    matricule_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Matricule",width=400,height=40,bg_color="#fff",
                                         fg_color="#fff",text_color="#000")

    
    campus_values = [connexionbase.showcampus[1]]
    campus = customtkinter.CTkComboBox(master=addfen,values=campus_values,width=400,height=40,bg_color="#fff",fg_color="#fff",
                                   text_color="#000")
    
    departement_values = [dep[1] for dep in connexionbase.depres]
    departement_entry = customtkinter.CTkComboBox(master=addfen,values=departement_values,width=400,height=40,bg_color="#fff",
                                              fg_color="#fff",text_color="#000")

    faculte_values = [resu[1] for resu in connexionbase.result]
    faculte_entry = customtkinter.CTkComboBox(master=addfen,values=faculte_values,width=400,height=40,bg_color="#fff",
                                          fg_color="#fff",text_color="#000")


    campus.bind("<<comboboxSelected>>",valid)
    departement_entry.bind("<<comboboxSelected>>",valid)
    faculte_entry.bind("<<comboboxSelected>>",valid)

    valider_btn = customtkinter.CTkButton(master=addfen,text="Add student",fg_color="#809A50",text_color="#fff",height=40,
                                      bg_color="#fff",cursor="hand2",command=valid)


    #initialisation des label et inpiyt plus bouton
    labe.pack(pady=20)
    nom_entry.pack(pady=10)
    prenom_entry.pack(pady=10)
    matricule_entry.pack(pady=10)
    campus.pack(pady=10)
    departement_entry.pack(pady=10)
    faculte_entry.pack(pady=10)
    valider_btn.pack(pady=10)

    if __name__ == '__main__':
        addfen.mainloop()
    


def faculte_deux():
    addfen = customtkinter.CTk()
    addfen.geometry("800x600")
    addfen.title("Add Student")
    addfen.config(background="#fff")

    #fonction de validation
    def valid():
        nom_fac = str(nom_entry.get())
        prenom_fac = str(prenom_entry.get())
        matricule_fac = str(matricule_entry.get())
        campus_fac = str(campus.get())
        departement_fac = str(departement_entry.get())
        facult_fac = str(faculte_entry.get())
        annee = 2
        tra1 = 'non'
        tra2 = 'non'
        tra3 = 'non'
        if nom_fac == "" or prenom_fac == "" or matricule_fac == "":
            print("veiller completer les cases vides")
        else:
            print("script commence... a execute")
            conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
            ajout = conn.cursor()
            
            rep = "INSERT INTO faculte_deux(nom,prenom,matricule,campus,departement,faculte,annee,tra1,tra2,tra3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            ajout.execute(rep,(nom_fac,prenom_fac,matricule_fac,campus_fac,departement_fac,facult_fac,annee,tra1,tra2,tra3))
            if ajout:
                messagebox.showinfo("Valider",'Etudiant ajoute')
                #supprension des donnees dans les entrees
                nom_entry.delete(0,END)
                prenom_entry.delete(0,END)
                matricule_entry.delete(0,END)

            

            conn.commit()
            conn.close()
    #en bas de la fonction de validation


    labe = customtkinter.CTkLabel(master=addfen,text="Add Student in Fac 2",fg_color="#fff",text_color=couleur.orange_color,font=('sans-serif',20),
                              )

    nom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Nom..",width=400,height=40,bg_color="#fff",
                                   fg_color="#fff",text_color="#000")
    prenom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Prenom...",width=400,height=40,bg_color="#fff",
                                      fg_color="#fff",text_color="#000")
    matricule_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Matricule",width=400,height=40,bg_color="#fff",
                                         fg_color="#fff",text_color="#000")


    campus_values = [connexionbase.showcampus[1]]
    campus = customtkinter.CTkComboBox(master=addfen,values=campus_values,width=400,height=40,bg_color="#fff",fg_color="#fff",
                                   text_color="#000")

    departement_values = [dep[1] for dep in connexionbase.depres]
    departement_entry = customtkinter.CTkComboBox(master=addfen,values=departement_values,width=400,height=40,bg_color="#fff",
                                              fg_color="#fff",text_color="#000")

    faculte_values = [resu[1] for resu in connexionbase.result]
    faculte_entry = customtkinter.CTkComboBox(master=addfen,values=faculte_values,width=400,height=40,bg_color="#fff",
                                          fg_color="#fff",text_color="#000")


    campus.bind("<<comboboxSelected>>",valid)
    departement_entry.bind("<<comboboxSelected>>",valid)
    faculte_entry.bind("<<comboboxSelected>>",valid)

    valider_btn = customtkinter.CTkButton(master=addfen,text="Add student",fg_color=couleur.orange_color,text_color="#fff",height=40,
                                      bg_color="#fff",cursor="hand2",command=valid)


    #initialisation des label et inpiyt plus bouton
    labe.pack(pady=20)
    nom_entry.pack(pady=10)
    prenom_entry.pack(pady=10)
    matricule_entry.pack(pady=10)
    campus.pack(pady=10)
    departement_entry.pack(pady=10)
    faculte_entry.pack(pady=10)
    valider_btn.pack(pady=10)

    if __name__ == '__main__':
        addfen.mainloop()
       


def faculte_trois():
    addfen = customtkinter.CTk()
    addfen.geometry("800x600")
    addfen.title("Add Student")
    addfen.config(background="#fff")

    #fonction de validation
    def valid():
        nom_fac = str(nom_entry.get())
        prenom_fac = str(prenom_entry.get())
        matricule_fac = str(matricule_entry.get())
        campus_fac = str(campus.get())
        departement_fac = str(departement_entry.get())
        facult_fac = str(faculte_entry.get())
        annee = 3
        tra1 = 'non'
        tra2 = 'non'
        tra3 = 'non'
        if nom_fac == "" or prenom_fac == "" or matricule_fac == "":
            print("veiller completer les cases vides")
        else:
            print("script commence... a execute")
            conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
            ajout = conn.cursor()
            
            rep = "INSERT INTO faculte_trois(nom,prenom,matricule,campus,departement,faculte,annee,tra1,tra2,tra3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            ajout.execute(rep,(nom_fac,prenom_fac,matricule_fac,campus_fac,departement_fac,facult_fac,annee,tra1,tra2,tra3))
            if ajout:
                messagebox.showinfo("Valider",'Etudiant ajoute')
                #supprension des donnees dans les entrees
                nom_entry.delete(0,END)
                prenom_entry.delete(0,END)
                matricule_entry.delete(0,END)

            

            conn.commit()
            conn.close()
    #en bas de la fonction de validation


    labe = customtkinter.CTkLabel(master=addfen,text="Add Student in Fac 3",fg_color="#fff",text_color="#120",font=('sans-serif',20),
                              )

    nom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Nom..",width=400,height=40,bg_color="#fff",
                                   fg_color="#fff",text_color="#000")
    prenom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Prenom...",width=400,height=40,bg_color="#fff",
                                      fg_color="#fff",text_color="#000")
    matricule_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Matricule",width=400,height=40,bg_color="#fff",
                                         fg_color="#fff",text_color="#000")


    campus_values = [connexionbase.showcampus[1]]
    campus = customtkinter.CTkComboBox(master=addfen,values=campus_values,width=400,height=40,bg_color="#fff",fg_color="#fff",
                                   text_color="#000")

    departement_values = [dep[1] for dep in connexionbase.depres]
    departement_entry = customtkinter.CTkComboBox(master=addfen,values=departement_values,width=400,height=40,bg_color="#fff",
                                              fg_color="#fff",text_color="#000")

    faculte_values = [resu[1] for resu in connexionbase.result]
    faculte_entry = customtkinter.CTkComboBox(master=addfen,values=faculte_values,width=400,height=40,bg_color="#fff",
                                          fg_color="#fff",text_color="#000")


    campus.bind("<<comboboxSelected>>",valid)
    departement_entry.bind("<<comboboxSelected>>",valid)
    faculte_entry.bind("<<comboboxSelected>>",valid)

    valider_btn = customtkinter.CTkButton(master=addfen,text="Add student",fg_color="#120",text_color="#fff",height=40,
                                      bg_color="#fff",cursor="hand2",command=valid)


    #initialisation des label et inpiyt plus bouton
    labe.pack(pady=20)
    nom_entry.pack(pady=10)
    prenom_entry.pack(pady=10)
    matricule_entry.pack(pady=10)
    campus.pack(pady=10)
    departement_entry.pack(pady=10)
    faculte_entry.pack(pady=10)
    valider_btn.pack(pady=10)

    if __name__ == '__main__':
        addfen.mainloop()
    
    
    
def institut_un():
    addfen = customtkinter.CTk()
    addfen.geometry("800x600")
    addfen.title("Add Student")
    addfen.config(background="#fff")

    #fonction de validation
    def valid():
       nom_institut = str(nom_entry.get())
       prenom_institut = str(prenom_entry.get())
       matricule_institut = str(matricule_entry.get())
       campus_institut = str(campus.get())
       institut_ins = str(institut_entry.get())
       tra1 = 'non'
       tra2 = 'non'
       tra3 = 'non'
       annee = 1
       if nom_institut == "" or prenom_institut == "" or matricule_institut == "":
           print("completer les case vides")
       else:
           print("script commence... a execute")
           conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
           ajout = conn.cursor()
            
           rep = "INSERT INTO institut_un(nom,prenom,matricule,campus,institut,annee,tra1,tra2,tra3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           ajout.execute(rep,(nom_institut,prenom_institut,matricule_institut,campus_institut,institut_ins,annee,tra1,tra2,tra3))
           if ajout:
                messagebox.showinfo("Valider",'Etudiant ajoute')
                #supprension des donnees dans les entrees
                nom_entry.delete(0,END)
                prenom_entry.delete(0,END)
                matricule_entry.delete(0,END)

            

           conn.commit()
           conn.close()
           


       #en bas de la fonction de validation 


    labe = customtkinter.CTkLabel(master=addfen,text="Add Student in institut 1",fg_color="#fff",text_color="#300",
                                  font=('sans-serif',20),)

    nom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Nom..",width=400,height=40,bg_color="#fff",
                                   fg_color="#fff",text_color="#000")
    prenom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Prenom...",width=400,height=40,bg_color="#fff",
                                      fg_color="#fff",text_color="#000")
    matricule_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Matricule",width=400,height=40,bg_color="#fff",
                                         fg_color="#fff",text_color="#000")


    campus_values = [connexionbase.showcampus[1]]
    campus = customtkinter.CTkComboBox(master=addfen,values=campus_values,width=400,height=40,bg_color="#fff",fg_color="#fff",
                                   text_color="#000")


    institut_values = [resu[1] for resu in connexionbase.showinstitut]
    institut_entry = customtkinter.CTkComboBox(master=addfen,values=institut_values,width=400,height=40,bg_color="#fff",
                                          fg_color="#fff",text_color="#000")


    campus.bind("<<comboboxSelected>>",valid)
    institut_entry.bind("<<comboboxSelected>>",valid)

    valider_btn = customtkinter.CTkButton(master=addfen,text="Add student",fg_color="#300",text_color="#fff",height=40,
                                      bg_color="#fff",cursor="hand2",command=valid)


    #initialisation des label et inpiyt plus bouton
    labe.pack(pady=20)
    nom_entry.pack(pady=10)
    prenom_entry.pack(pady=10)
    matricule_entry.pack(pady=10)
    campus.pack(pady=10)

    institut_entry.pack(pady=10)
    valider_btn.pack(pady=10)

    if __name__ == '__main__':
        addfen.mainloop()
    

def institut_deux():
    addfen = customtkinter.CTk()
    addfen.geometry("800x600")
    addfen.title("Add Student")
    addfen.config(background="#fff")

    #fonction de validation
    def valid():
       nom_institut = str(nom_entry.get())
       prenom_institut = str(prenom_entry.get())
       matricule_institut = str(matricule_entry.get())
       campus_institut = str(campus.get())
       institut_ins = str(institut_entry.get())
       tra1 = 'non'
       tra2 = 'non'
       tra3 = 'non'
       annee = 2
       if nom_institut == "" or prenom_institut == "" or matricule_institut == "":
           print("completer les case vides")
       else:
           print("script commence... a execute")
           conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
           ajout = conn.cursor()
            
           rep = "INSERT INTO institut_deux(nom,prenom,matricule,campus,institut,annee,tra1,tra2,tra3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           ajout.execute(rep,(nom_institut,prenom_institut,matricule_institut,campus_institut,institut_ins,annee,tra1,tra2,tra3))
           if ajout:
                messagebox.showinfo("Valider",'Etudiant ajoute')
                #supprension des donnees dans les entrees
                nom_entry.delete(0,END)
                prenom_entry.delete(0,END)
                matricule_entry.delete(0,END)

            

           conn.commit()
           conn.close()
       #en bas de la fonction de validation


    labe = customtkinter.CTkLabel(master=addfen,text="Add Student in institut 2",fg_color="#fff",text_color="blue",
                                  font=('sans-serif',20),)

    nom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Nom..",width=400,height=40,bg_color="#fff",
                                   fg_color="#fff",text_color="#000")
    prenom_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Prenom...",width=400,height=40,bg_color="#fff",
                                      fg_color="#fff",text_color="#000")
    matricule_entry = customtkinter.CTkEntry(master=addfen,placeholder_text="Matricule",width=400,height=40,bg_color="#fff",
                                         fg_color="#fff",text_color="#000")


    campus_values = [connexionbase.showcampus[1]]
    campus = customtkinter.CTkComboBox(master=addfen,values=campus_values,width=400,height=40,bg_color="#fff",fg_color="#fff",
                                   text_color="#000")


    institut_values = [resu[1] for resu in connexionbase.showinstitut]
    institut_entry = customtkinter.CTkComboBox(master=addfen,values=institut_values,width=400,height=40,bg_color="#fff",
                                          fg_color="#fff",text_color="#000")


    campus.bind("<<comboboxSelected>>",valid)
    institut_entry.bind("<<comboboxSelected>>",valid)

    valider_btn = customtkinter.CTkButton(master=addfen,text="Add student",fg_color="blue",text_color="#fff",height=40,
                                      bg_color="#fff",cursor="hand2",command=valid)


    #initialisation des label et inpiyt plus bouton
    labe.pack(pady=20)
    nom_entry.pack(pady=10)
    prenom_entry.pack(pady=10)
    matricule_entry.pack(pady=10)
    campus.pack(pady=10)

    institut_entry.pack(pady=10)
    valider_btn.pack(pady=10)

    if __name__ == '__main__':
        addfen.mainloop()


def aide():
    aidefen = tkinter.Tk()
    aidefen.title('Apropos du logiciel')

    labaide = customtkinter.CTkLabel(master=aidefen,text="Minesoft developper par Jersy Igiraneza",text_color='#000')
    
    vers = customtkinter.CTkLabel(master=aidefen,text="Minesoft Version 1.1.0",text_color='#000')
    dat = customtkinter.CTkLabel(master=aidefen,text='Le 14-11-2024 par Ingobe.Dev',text_color='#000')
    labaide.pack(padx=10,pady=10)
    vers.pack(padx=10,pady=3)
    dat.pack(padx=10,pady=10)
    


    if __name__ == '__main__':
        aidefen.mainloop()


#bouton recherhcer ou fonction du page gestion etudiant
def chercher():
    print("hello word")
    conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
    
    conteneu_rep = 'SELECT * FROM faculte_un WHERE prenom LIKE "%''%"'
    aff = conn.cursor()
    aff.execute(conteneu_rep)
    for result in aff:
        print(result[0],' ',result[1])
    conn.commit()
    conn.close()


#donne pour faire une recherche sur gestion des etudiant page
def donnfac1():
    nouveaufen = tkinter.Tk()
    nouveaufen.title('Faculte-1')
    nouveaufen.geometry('1200x670')
    lbEffectiftotal = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs Total : 230")
    lbEffectifPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs paye : 12",text_color='#180')
    lbEffectifnonPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs non paye : 20",text_color='#100')
    tablegestion = ttk.Treeview(master=nouveaufen,columns=(1,2,3,4,5,6,7,8,9,10,11),height=24,show="headings")

    #initialisation du conteneu page gestion etudiant
    lbEffectiftotal.place(x=830,y=5)
    lbEffectifPaye.place(x=10,y=600)
    lbEffectifnonPaye.place(x=10,y=620)

    tablegestion.place(x=2,y=100)
    tablegestion.heading(1,text="#")
    tablegestion.heading(2,text='Nom')
    tablegestion.heading(3,text='Prenom')
    tablegestion.heading(4,text='Matricule')
    tablegestion.heading(5,text='Campus')
    tablegestion.heading(6,text='Departement')
    tablegestion.heading(7,text='Faculte/Instiut')
    tablegestion.heading(8,text='Annee')
    tablegestion.heading(9,text='Tra-1')
    tablegestion.heading(10,text='Tra-2')
    tablegestion.heading(11,text='Tra-3')

    tablegestion.column(1,width=10)
    tablegestion.column(2,width=180)
    tablegestion.column(3,width=110)
    tablegestion.column(4,width=100)
    tablegestion.column(5,width=100)
    tablegestion.column(6,width=180)
    tablegestion.column(7,width=210)
    tablegestion.column(8,width=60)
    tablegestion.column(9,width=80)
    tablegestion.column(10,width=80)
    tablegestion.column(11,width=80)

    conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
    conteneu_rep = "SELECT * FROM faculte_un"
    aff = conn.cursor()
    aff.execute(conteneu_rep)
    for result in aff:
        tablegestion.insert('',END,values=result)
    conn.commit()
    conn.close()
    nouveaufen.mainloop()


def donnfac2():
        nouveaufen = tkinter.Tk()
        nouveaufen.title('Faculte-1')
        nouveaufen.geometry('1200x670')
        lbEffectiftotal = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs Total : 230")
        lbEffectifPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs paye : 12",text_color='#180')
        lbEffectifnonPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs non paye : 20",text_color='#100')
        tablegestion = ttk.Treeview(master=nouveaufen,columns=(1,2,3,4,5,6,7,8,9,10,11),height=24,show="headings")

        #initialisation du conteneu page gestion etudiant
        lbEffectiftotal.place(x=830,y=5)
        lbEffectifPaye.place(x=10,y=600)
        lbEffectifnonPaye.place(x=10,y=620)

        tablegestion.place(x=2,y=100)
        tablegestion.heading(1,text="#")
        tablegestion.heading(2,text='Nom')
        tablegestion.heading(3,text='Prenom')
        tablegestion.heading(4,text='Matricule')
        tablegestion.heading(5,text='Campus')
        tablegestion.heading(6,text='Departement')
        tablegestion.heading(7,text='Faculte/Instiut')
        tablegestion.heading(8,text='Annee')
        tablegestion.heading(9,text='Tra-1')
        tablegestion.heading(10,text='Tra-2')
        tablegestion.heading(11,text='Tra-3')

        tablegestion.column(1,width=10)
        tablegestion.column(2,width=180)
        tablegestion.column(3,width=110)
        tablegestion.column(4,width=100)
        tablegestion.column(5,width=100)
        tablegestion.column(6,width=180)
        tablegestion.column(7,width=210)
        tablegestion.column(8,width=60)
        tablegestion.column(9,width=80)
        tablegestion.column(10,width=80)
        tablegestion.column(11,width=80)

        conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
        conteneu_rep = "SELECT * FROM faculte_deux"
        aff = conn.cursor()
        aff.execute(conteneu_rep)
        for result in aff:
            tablegestion.insert('',END,values=result)
        conn.commit()
        conn.close()
        nouveaufen.mainloop()

def donnfac3():
        nouveaufen = tkinter.Tk()
        nouveaufen.title('Faculte-1')
        nouveaufen.geometry('1200x670')
        lbEffectiftotal = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs Total : 230")
        lbEffectifPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs paye : 12",text_color='#180')
        lbEffectifnonPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs non paye : 20",text_color='#100')
        tablegestion = ttk.Treeview(master=nouveaufen,columns=(1,2,3,4,5,6,7,8,9,10,11),height=24,show="headings")

        #initialisation du conteneu page gestion etudiant
        lbEffectiftotal.place(x=830,y=5)
        lbEffectifPaye.place(x=10,y=600)
        lbEffectifnonPaye.place(x=10,y=620)

        tablegestion.place(x=2,y=100)
        tablegestion.heading(1,text="#")
        tablegestion.heading(2,text='Nom')
        tablegestion.heading(3,text='Prenom')
        tablegestion.heading(4,text='Matricule')
        tablegestion.heading(5,text='Campus')
        tablegestion.heading(6,text='Departement')
        tablegestion.heading(7,text='Faculte/Instiut')
        tablegestion.heading(8,text='Annee')
        tablegestion.heading(9,text='Tra-1')
        tablegestion.heading(10,text='Tra-2')
        tablegestion.heading(11,text='Tra-3')

        tablegestion.column(1,width=10)
        tablegestion.column(2,width=180)
        tablegestion.column(3,width=110)
        tablegestion.column(4,width=100)
        tablegestion.column(5,width=100)
        tablegestion.column(6,width=180)
        tablegestion.column(7,width=210)
        tablegestion.column(8,width=60)
        tablegestion.column(9,width=80)
        tablegestion.column(10,width=80)
        tablegestion.column(11,width=80)

        conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
        conteneu_rep = "SELECT * FROM faculte_trois"
        aff = conn.cursor()
        aff.execute(conteneu_rep)
        for result in aff:
            tablegestion.insert('',END,values=result)
        conn.commit()
        conn.close()
        nouveaufen.mainloop()

def donninstitut1():
        nouveaufen = tkinter.Tk()
        nouveaufen.title('Faculte-1')
        nouveaufen.geometry('1200x670')
        lbEffectiftotal = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs Total : 230")
        lbEffectifPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs paye : 12",text_color='#180')
        lbEffectifnonPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs non paye : 20",text_color='#100')
        tablegestion = ttk.Treeview(master=nouveaufen,columns=(1,2,3,4,5,6,7,8,9,10,11),height=24,show="headings")

        #initialisation du conteneu page gestion etudiant
        lbEffectiftotal.place(x=830,y=5)
        lbEffectifPaye.place(x=10,y=600)
        lbEffectifnonPaye.place(x=10,y=620)

        tablegestion.place(x=2,y=100)
        tablegestion.heading(1,text="#")
        tablegestion.heading(2,text='Nom')
        tablegestion.heading(3,text='Prenom')
        tablegestion.heading(4,text='Matricule')
        tablegestion.heading(5,text='Campus')
        tablegestion.heading(6,text='Departement')
        tablegestion.heading(7,text='Faculte/Instiut')
        tablegestion.heading(8,text='Annee')
        tablegestion.heading(9,text='Tra-1')
        tablegestion.heading(10,text='Tra-2')
        tablegestion.heading(11,text='Tra-3')

        tablegestion.column(1,width=10)
        tablegestion.column(2,width=180)
        tablegestion.column(3,width=110)
        tablegestion.column(4,width=100)
        tablegestion.column(5,width=100)
        tablegestion.column(6,width=180)
        tablegestion.column(7,width=210)
        tablegestion.column(8,width=60)
        tablegestion.column(9,width=80)
        tablegestion.column(10,width=80)
        tablegestion.column(11,width=80)

        conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
        conteneu_rep = "SELECT * FROM institut_un"
        aff = conn.cursor()
        aff.execute(conteneu_rep)
        for result in aff:
            tablegestion.insert('',END,values=result)
        conn.commit()
        conn.close()
        nouveaufen.mainloop()

def donninstitut2():
    nouveaufen = tkinter.Tk()
    nouveaufen.title('Faculte-1')
    nouveaufen.geometry('1200x670')
    lbEffectiftotal = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs Total : 230")
    lbEffectifPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs paye : 12",text_color='#180')
    lbEffectifnonPaye = customtkinter.CTkLabel(master=nouveaufen,text="Effectifs non paye : 20",text_color='#100')
    tablegestion = ttk.Treeview(master=nouveaufen,columns=(1,2,3,4,5,6,7,8,9,10,11),height=24,show="headings")

    #initialisation du conteneu page gestion etudiant
    lbEffectiftotal.place(x=830,y=5)
    lbEffectifPaye.place(x=10,y=600)
    lbEffectifnonPaye.place(x=10,y=620)

    tablegestion.place(x=2,y=100)
    tablegestion.heading(1,text="#")
    tablegestion.heading(2,text='Nom')
    tablegestion.heading(3,text='Prenom')
    tablegestion.heading(4,text='Matricule')
    tablegestion.heading(5,text='Campus')
    tablegestion.heading(6,text='Departement')
    tablegestion.heading(7,text='Faculte/Instiut')
    tablegestion.heading(8,text='Annee')
    tablegestion.heading(9,text='Tra-1')
    tablegestion.heading(10,text='Tra-2')
    tablegestion.heading(11,text='Tra-3')

    tablegestion.column(1,width=10)
    tablegestion.column(2,width=180)
    tablegestion.column(3,width=110)
    tablegestion.column(4,width=100)
    tablegestion.column(5,width=100)
    tablegestion.column(6,width=180)
    tablegestion.column(7,width=210)
    tablegestion.column(8,width=60)
    tablegestion.column(9,width=80)
    tablegestion.column(10,width=80)
    tablegestion.column(11,width=80)

    conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
    conteneu_rep = "SELECT * FROM institut_deux"
    aff = conn.cursor()
    aff.execute(conteneu_rep)
    for result in aff:
        tablegestion.insert('',END,values=result)
    conn.commit()
    conn.close()
    nouveaufen.mainloop()


def vali():
    l = tkinter.Tk()
    l.title("Validation")

    def check():
        idd = int(id_entry.get())
        newvali = "Oui"
        conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
        ch = conn.cursor()
        re = "UPDATE faculte_un SET tra1 ='Oui' WHERE id="
        ch.execute(re,ch)
        conn.commit()
        conn.close()

    id_entry = customtkinter.CTkEntry(master=l,placeholder_text="Entre un id")
    btnid = customtkinter.CTkButton(master=l,text='Valider',command=check)

    id_entry.pack(padx=10,pady=10)
    btnid.pack(padx=10,pady=10)
    l.mainloop()


    
#creation des icons pour notre application pour les liens de navigation sur notre application

home_icon = Image.open("icon/home.png")
gestion_icon = Image.open("icon/gest.png")
faculte_icon = Image.open("icon/fac.png")
institut_icon = Image.open("icon/inst.png")
statistique_icon = Image.open("icon/stat.png")
dec_icon = Image.open("icon/dec.png")
retour_icon = Image.open("icon/retour.png")

#icon pour les instiut et faculte
fac1_icon = Image.open("icon/fac1.png")
fac2_icon = Image.open("icon/fac2.png")
fac3_icon = Image.open("icon/fac3.png")

inst1_icon = Image.open("icon/inst1.png")
inst2_icon = Image.open("icon/inst2.png")

#cration des frame qui va me permetre dec communique avec autre page c a d des multiple tables ici en bas
home_page = Frame(app)
gestionEtudinat_page = Frame(app)
faculte_page = Frame(app)
institut_page = Frame(app)
statistique_page  = Frame(app)
#deconnexion ni bouton niyo nagize kbx

#initiliastaion des differente pages.....

home_page.grid(row=0,column=0,sticky="nsew")
gestionEtudinat_page.grid(row=0,column=0,sticky="nsew")
faculte_page.grid(row=0,column=0,sticky="nsew")
institut_page.grid(row=0,column=0,sticky="nsew")
statistique_page.grid(row=0,column=0,sticky="nsew")

#fin de cration des frame pour mes page sur le logiciel......

"""donneer de la page home et ses composant"""


#zone des frame pour les contenues des pages
nav_framehome = tkinter.Frame(master=home_page,width=200,height=650,bg=couleur.white_color)
contenet_framehome = tkinter.Frame(master=home_page,width=1000,height=650,bg=couleur.white_bac)
contenet_framegestionEtudiant = tkinter.Frame(master=gestionEtudinat_page,width=1000,height=650,bg=couleur.white_color) 


#zone des wigets et autre ..
nom_logiciel = customtkinter.CTkLabel(master=nav_framehome,text="Minesoft",text_color=couleur.orange_color,font=("sans-serif",25))
home_bouton = customtkinter.CTkButton(master=nav_framehome,text="  Home",image=CTkImage(light_image=home_icon,dark_image=home_icon),
                                      font=("sans-serif",20),cursor="hand2",fg_color=couleur.orange_color,border_width=0,border_spacing=10,width=180,anchor="center",command=lambda:home_page.tkraise())

gestionEtudiant_bouton = customtkinter.CTkButton(master=nav_framehome,text="Gestion Etudiant",cursor="hand2",text_color=couleur.black_color,
                                                 width=180,font=("sans-serif",15),border_spacing=10,image=CTkImage(light_image=gestion_icon,dark_image=gestion_icon),fg_color=couleur.white_color,hover_color=couleur.orange_color,command=lambda:gestionEtudinat_page.tkraise())

faculte_bouton = customtkinter.CTkButton(master=nav_framehome,text="  Faculte  plus",cursor="hand2",text_color=couleur.black_color,
                                                 width=180,font=("sans-serif",18),border_spacing=10,image=CTkImage(light_image=faculte_icon,dark_image=faculte_icon),fg_color=couleur.white_color,hover_color=couleur.orange_color,anchor="center",
                                                 command=lambda:faculte_page.tkraise())

institut_bouton = customtkinter.CTkButton(master=nav_framehome,text="  Institut  plus ",cursor="hand2",width=180,anchor="center",
                                          text_color=couleur.black_color,
                                          border_spacing=10,image=CTkImage(light_image=institut_icon,dark_image=institut_icon),font=("sans-serif",18),
                                          hover_color=couleur.orange_color,fg_color=couleur.white_color,
                                          command=lambda:institut_page.tkraise())

statistique_bouton = customtkinter.CTkButton(master=nav_framehome,text="   Statistique ",fg_color=couleur.white_color,width=180,
                                             border_spacing=10,anchor="center",      
                                             image=CTkImage(light_image=statistique_icon,dark_image=statistique_icon),hover_color=couleur.orange_color,
                                             text_color=couleur.black_color,font=('sans-serif',18),command=lambda:statistique_page.tkraise())
deconnexion_bouton = customtkinter.CTkButton(master=nav_framehome,text="Deconnexion",text_color=couleur.white_color,border_spacing=10,
                                             font=("sans-serif",18),image=CTkImage(light_image=dec_icon,dark_image=dec_icon ),
                                             width=180,hover_color="red",cursor='hand2',command=quitter)
                                                                                                            
#initialisaton des wigets
nom_logiciel.place(x=40,y=20)
home_bouton.place(x=10,y=100)
gestionEtudiant_bouton.place(x=10,y=170)
faculte_bouton.place(x=10,y=230)
institut_bouton.place(x=10,y=300)
statistique_bouton.place(x=10,y=370)
deconnexion_bouton.place(x=10,y=600)

#"""intialiasation des frames..."""
nav_framehome.grid(row=0,column=0,sticky="nsew")
contenet_framehome.grid(row=0,column=1,sticky="nsew")
contenet_framegestionEtudiant.grid(row=0,column=1,sticky="nsew")

"""fin de l'intialisation  des donnes de la page home"""





"""donnneer de la page gestion des etutiant """
#zone frame
nav_framegestEt = Frame(master=gestionEtudinat_page,width=200,height=650,bg=couleur.white_color)


#zone des wideget et autres.....

nom_logiciel1 = customtkinter.CTkLabel(master=nav_framegestEt,text="Minesoft",text_color=couleur.orange_color,font=("sans-serif",25))
home_bouton1 = customtkinter.CTkButton(master=nav_framegestEt,text="  Home",image=CTkImage(light_image=home_icon,dark_image=home_icon),
                                      font=("sans-serif",20),cursor="hand2",fg_color=couleur.white_color,border_width=0,border_spacing=10,width=180,anchor="center",command=lambda:home_page.tkraise(),text_color=couleur.black_color,hover_color=couleur.orange_color)

gestionEtudiant_bouton1 = customtkinter.CTkButton(master=nav_framegestEt,text="Gestion Etudiant",cursor="hand2",text_color=couleur.white_color,
                                                 width=180,font=("sans-serif",15),border_spacing=10,image=CTkImage(light_image=gestion_icon,dark_image=gestion_icon),fg_color=couleur.orange_color,command=lambda:gestionEtudinat_page.tkraise())

faculte_bouton1 = customtkinter.CTkButton(master=nav_framegestEt,text="  Faculte  plus",cursor="hand2",text_color=couleur.black_color,
                                                 width=180,font=("sans-serif",18),border_spacing=10,image=CTkImage(light_image=faculte_icon,dark_image=faculte_icon),fg_color=couleur.white_color,hover_color=couleur.orange_color,anchor="center",
                                                 command=lambda:faculte_page.tkraise())

institut_bouton1 = customtkinter.CTkButton(master=nav_framegestEt,text="  Institut  plus ",cursor="hand2",width=180,anchor="center",text_color=couleur.black_color,
                                          border_spacing=10,image=CTkImage(light_image=institut_icon,dark_image=institut_icon),font=("sans-serif",18),
                                          hover_color=couleur.orange_color,fg_color=couleur.white_color,command=lambda:institut_page.tkraise())

statistique_bouton1 = customtkinter.CTkButton(master=nav_framegestEt,text="   Statistique ",fg_color=couleur.white_color,width=180,anchor="center",
                                             border_spacing=10,
                                             image=CTkImage(light_image=statistique_icon,dark_image=statistique_icon),hover_color=couleur.orange_color,
                                             text_color=couleur.black_color,font=('sans-serif',18),command=lambda:statistique_page.tkraise())

deconnexion_bouton1 = customtkinter.CTkButton(master=nav_framegestEt,text="Deconnexion",text_color=couleur.white_color,border_spacing=10,
                                             font=("sans-serif",18),image=CTkImage(light_image=dec_icon,dark_image=dec_icon ),
                                             width=180,hover_color="red",cursor='hand2',command=quitter)
     



#initialisation des wideget.....
nom_logiciel1.place(x=40,y=20)
home_bouton1.place(x=10,y=100)
gestionEtudiant_bouton1.place(x=10,y=170)
faculte_bouton1.place(x=10,y=230)
institut_bouton1.place(x=10,y=300)
statistique_bouton1.place(x=10,y=370)
deconnexion_bouton1.place(x=10,y=600)

#initialisation de la frame gestion etudiant
nav_framegestEt.grid(row=0,column=0,sticky="nsew")

"""fin de l'initialisation des donnes a la page gestion etutiant page"""



"""donnneer de la page faculte """
#zone frame
nav_framefac = Frame(master=faculte_page,width=200,height=650,bg=couleur.white_color)


#zone des wideget et autres.....

nom_logiciel2 = customtkinter.CTkLabel(master=nav_framefac,text="Minesoft",text_color=couleur.orange_color,font=("sans-serif",25))
home_bouton2 = customtkinter.CTkButton(master=nav_framefac,text="  Home",image=CTkImage(light_image=home_icon,dark_image=home_icon),
                                      font=("sans-serif",20),cursor="hand2",fg_color=couleur.white_color,border_width=0,border_spacing=10,width=180,anchor="center",command=lambda:home_page.tkraise(),text_color=couleur.black_color,hover_color=couleur.orange_color)

gestionEtudiant_bouton2 = customtkinter.CTkButton(master=nav_framefac,text="Gestion Etudiant",cursor="hand2",
                                                text_color=couleur.black_color,
                                                width=180,font=("sans-serif",15),border_spacing=10,image=CTkImage(light_image=gestion_icon,dark_image=gestion_icon),fg_color=couleur.white_color,command=lambda:gestionEtudinat_page.tkraise(),
                                                hover_color=couleur.orange_color)

faculte_bouton2 = customtkinter.CTkButton(master=nav_framefac,text="  Faculte  plus",cursor="hand2",text_color=couleur.white_color,
                                                 width=180,font=("sans-serif",18),border_spacing=10,image=CTkImage(light_image=faculte_icon,dark_image=faculte_icon),fg_color=couleur.orange_color,anchor="center",
                                                 command=lambda:faculte_page.tkraise())

institut_bouton2 = customtkinter.CTkButton(master=nav_framefac,text="  Institut  plus ",cursor="hand2",width=180,anchor="center",
                                        text_color=couleur.black_color,
                                        border_spacing=10,image=CTkImage(light_image=institut_icon,dark_image=institut_icon),font=("sans-serif",18),
                                        hover_color=couleur.orange_color,fg_color=couleur.white_color,
                                        command=lambda:institut_page.tkraise())

statistique_bouton2 = customtkinter.CTkButton(master=nav_framefac,text="   Statistique ",fg_color=couleur.white_color,width=180,
                                             border_spacing=10,anchor="center",
                                             image=CTkImage(light_image=statistique_icon,dark_image=statistique_icon),hover_color=couleur.orange_color,
                                             text_color=couleur.black_color,font=('sans-serif',18),
                                             command=lambda:statistique_page.tkraise())

deconnexion_bouton2 = customtkinter.CTkButton(master=nav_framefac,text="Deconnexion",text_color=couleur.white_color,border_spacing=10,
                                             font=("sans-serif",18),image=CTkImage(light_image=dec_icon,dark_image=dec_icon ),
                                             width=180,hover_color="red",cursor='hand2',command=quitter)
     



#initialisation des wideget.....
nom_logiciel2.place(x=40,y=20)
home_bouton2.place(x=10,y=100)
gestionEtudiant_bouton2.place(x=10,y=170)
faculte_bouton2.place(x=10,y=230)
institut_bouton2.place(x=10,y=300)
statistique_bouton2.place(x=10,y=370)
deconnexion_bouton2.place(x=10,y=600)

#initialisation de la frame gestion etudiant
nav_framefac.grid(row=0,column=0,sticky="nsew")

"""fin de l'initialisation des donnes a la page faculte page"""




"""donnneer de la page institut """
#zone frame
nav_frameinst = Frame(master=institut_page,width=200,height=650,bg=couleur.white_color)


#zone des wideget et autres.....

nom_logiciel3 = customtkinter.CTkLabel(master=nav_frameinst,text="Minesoft",text_color=couleur.orange_color,font=("sans-serif",25))
home_bouton3 = customtkinter.CTkButton(master=nav_frameinst,text="  Home",image=CTkImage(light_image=home_icon,dark_image=home_icon),
                                      font=("sans-serif",20),cursor="hand2",fg_color=couleur.white_color,border_width=0,border_spacing=10,width=180,anchor="center",command=lambda:home_page.tkraise(),text_color=couleur.black_color,hover_color=couleur.orange_color)

gestionEtudiant_bouton3 = customtkinter.CTkButton(master=nav_frameinst,text="Gestion Etudiant",cursor="hand2",
                                                text_color=couleur.black_color,
                                                 width=180,font=("sans-serif",15),border_spacing=10,image=CTkImage(light_image=gestion_icon,dark_image=gestion_icon),fg_color=couleur.white_color,command=lambda:gestionEtudinat_page.tkraise(),
                                                 hover_color=couleur.orange_color)

faculte_bouton3 = customtkinter.CTkButton(master=nav_frameinst,text="  Faculte  plus",cursor="hand2",text_color=couleur.black_color,
                                                 width=180,font=("sans-serif",18),border_spacing=10,image=CTkImage(light_image=faculte_icon,dark_image=faculte_icon),fg_color=couleur.white_color,hover_color=couleur.orange_color,anchor="center",
                                                 command=lambda:faculte_page.tkraise())

institut_bouton3 = customtkinter.CTkButton(master=nav_frameinst,text="  Institut  plus ",cursor="hand2",width=180,anchor="center",
                                        text_color=couleur.white_color,
                                        border_spacing=10,image=CTkImage(light_image=institut_icon,dark_image=institut_icon),font=("sans-serif",18),
                                        fg_color=couleur.orange_color,command=lambda:institut_page.tkraise())

statistique_bouton3 = customtkinter.CTkButton(master=nav_frameinst,text="   Statistique ",fg_color=couleur.white_color,width=180,
                                             border_spacing=10,anchor="center",
                                             image=CTkImage(light_image=statistique_icon,dark_image=statistique_icon),hover_color=couleur.orange_color,
                                             text_color=couleur.black_color,font=('sans-serif',18),
                                             command=lambda:statistique_page.tkraise())

deconnexion_bouton3 = customtkinter.CTkButton(master=nav_frameinst,text="Deconnexion",text_color=couleur.white_color,border_spacing=10,
                                             font=("sans-serif",18),image=CTkImage(light_image=dec_icon,dark_image=dec_icon ),
                                             width=180,hover_color="red",cursor='hand2',command=quitter)
     



#initialisation des wideget.....
nom_logiciel3.place(x=40,y=20)
home_bouton3.place(x=10,y=100)
gestionEtudiant_bouton3.place(x=10,y=170)
faculte_bouton3.place(x=10,y=230)
institut_bouton3.place(x=10,y=300)
statistique_bouton3.place(x=10,y=370)
deconnexion_bouton3.place(x=10,y=600)

#initialisation de la frame gestion etudiant
nav_frameinst.grid(row=0,column=0,sticky="nsew")

"""fin de l'initialisation des donnes a la page isntitut page"""


"""donnneer de la page statistique """
#zone frame
nav_framestat = Frame(master=statistique_page,width=200,height=650,bg=couleur.white_color)


#zone des wideget et autres.....

nom_logiciel4 = customtkinter.CTkLabel(master=nav_framestat,text="Minesoft",text_color=couleur.orange_color,font=("sans-serif",25))
home_bouton4 = customtkinter.CTkButton(master=nav_framestat,text="  Home",image=CTkImage(light_image=home_icon,dark_image=home_icon),
                                      font=("sans-serif",20),cursor="hand2",fg_color=couleur.white_color,border_width=0,border_spacing=10,width=180,anchor="center",command=lambda:home_page.tkraise(),text_color=couleur.black_color,hover_color=couleur.orange_color)

gestionEtudiant_bouton4 = customtkinter.CTkButton(master=nav_framestat,text="Gestion Etudiant",cursor="hand2",
                                                  text_color=couleur.black_color,
                                                 width=180,font=("sans-serif",15),border_spacing=10,image=CTkImage(light_image=gestion_icon,dark_image=gestion_icon),fg_color=couleur.white_color,command=lambda:gestionEtudinat_page.tkraise())

faculte_bouton4 = customtkinter.CTkButton(master=nav_framestat,text="  Faculte  plus",cursor="hand2",text_color=couleur.black_color,
                                                 width=180,font=("sans-serif",18),border_spacing=10,image=CTkImage(light_image=faculte_icon,dark_image=faculte_icon),fg_color=couleur.white_color,hover_color=couleur.orange_color,anchor="center",
                                                 command=lambda:faculte_page.tkraise())

institut_bouton4 = customtkinter.CTkButton(master=nav_framestat,text="  Institut  plus ",cursor="hand2",width=180,
                                        anchor="center",text_color=couleur.black_color,
                                        border_spacing=10,image=CTkImage(light_image=institut_icon,dark_image=institut_icon),font=("sans-serif",18),
                                          hover_color=couleur.orange_color,fg_color=couleur.white_color,command=lambda:institut_page.tkraise())

statistique_bouton4 = customtkinter.CTkButton(master=nav_framestat,text="   Statistique ",fg_color=couleur.orange_color,width=180,
                                             border_spacing=10,anchor="center",
                                             image=CTkImage(light_image=statistique_icon,dark_image=statistique_icon),hover_color=couleur.orange_color,
                                             text_color=couleur.white_color,font=('sans-serif',18),
                                             command=lambda:statistique_page.tkraise())
                                             

deconnexion_bouton4 = customtkinter.CTkButton(master=nav_framestat,text="Deconnexion",text_color=couleur.white_color,border_spacing=10,
                                             font=("sans-serif",18),image=CTkImage(light_image=dec_icon,dark_image=dec_icon ),
                                             width=180,hover_color="red",cursor='hand2',command=quitter)
     



#initialisation des wideget.....
nom_logiciel4.place(x=40,y=20)
home_bouton4.place(x=10,y=100)
gestionEtudiant_bouton4.place(x=10,y=170)
faculte_bouton4.place(x=10,y=230)
institut_bouton4.place(x=10,y=300)
statistique_bouton4.place(x=10,y=370)
deconnexion_bouton4.place(x=10,y=600)

#initialisation de la frame gestion etudiant
nav_framestat.grid(row=0,column=0,sticky="nsew")

"""fin de l'initialisation de la page statique page"""



#creation du contenu pour la page home
label_home = customtkinter.CTkLabel(master=contenet_framehome,text="Bienvenue sur Minesoft logiciel de gestion des Minervals scolaire",
                                    text_color=couleur.black_color,font=("sans-serif",25))

fac1_home = customtkinter.CTkButton(master=contenet_framehome,text="Faculte 1",text_color=couleur.white_color,font=("sans-serif",40)
                                    ,image=CTkImage(light_image=fac1_icon,dark_image=fac1_icon),border_spacing=50,anchor="center",
                                    cursor="hand2",height=200,fg_color="#809A50",command=faculte_un)

fac2_home = customtkinter.CTkButton(master=contenet_framehome,text="Faculte 2",text_color=couleur.white_color,font=("sans-serif",40)
                                    ,image=CTkImage(light_image=fac2_icon,dark_image=fac2_icon),border_spacing=50,anchor="center",
                                    cursor="hand2",height=200,fg_color=couleur.orange_color,command=faculte_deux)

fac3_home = customtkinter.CTkButton(master=contenet_framehome,text="Faculte 3",text_color=couleur.white_color,font=("sans-serif",40)
                                    ,image=CTkImage(light_image=fac3_icon,dark_image=fac3_icon),border_spacing=50,anchor="center",
                                    cursor="hand2",height=200,fg_color="#120",command=faculte_trois)



institut1_home = customtkinter.CTkButton(master=contenet_framehome,text="Institut 1",text_color=couleur.white_color,font=("sans-serif",40)
                                    ,image=CTkImage(light_image=inst1_icon,dark_image=inst1_icon),border_spacing=50,anchor="center",
                                    cursor="hand2",height=200,width=480,fg_color="#300",command=institut_un)

institut2_home = customtkinter.CTkButton(master=contenet_framehome,text="Institut 2",text_color=couleur.white_color,font=("sans-serif",40)
                                    ,image=CTkImage(light_image=inst2_icon,dark_image=inst2_icon),border_spacing=50,anchor="center",
                                    cursor="hand2",height=200,width=480,command=institut_deux)

aide_home = customtkinter.CTkButton(master=contenet_framehome,text="Aide ?",text_color=couleur.white_color,border_spacing=20,
                                    fg_color="#060",command=aide)


#initilisation du contenue page home
label_home.place(x=100, y=10)
fac1_home.place(x=10,y=80)
fac2_home.place(x=346,y=80)
fac3_home.place(x=680,y=80)

institut1_home.place(x=10,y=300)
institut2_home.place(x=512,y=300)

aide_home.place(x=800,y=550)
"""fin du contenu sur la page home on cree autre contenues des page qui ne sont pas encore cree..."""


#creation du contenue de la page gestion etudiant

img = tkinter.PhotoImage(file="image/meet.png")
showimage = tkinter.Label(master=contenet_framegestionEtudiant,image=img)
showimage.pack(anchor='center')

title_lab = customtkinter.CTkLabel(master=contenet_framegestionEtudiant,fg_color='transparent',text_color='#000',text="Veiller choisir entre les differents facultes et instituts pour bien debuter avec Minesoft\n Minesoft offre plusieur solition dans notre communaute\n ainsi dans notre environnement de travail",font=('sans-serif',20))

donne_fac1 = customtkinter.CTkButton(master=contenet_framegestionEtudiant,text='Faculte-1',width=400,height=150,fg_color='pink',text_color='#000',command=donnfac1)
donne_fac2 = customtkinter.CTkButton(master=contenet_framegestionEtudiant,text='Faculte-2',width=400,height=150,fg_color='orange',command=donnfac2)
donne_fac3 = customtkinter.CTkButton(master=contenet_framegestionEtudiant,text='Faculte-3',width=889,height=150,fg_color=couleur.orange_color,command=donnfac3)
donne_institu1 = customtkinter.CTkButton(master=contenet_framegestionEtudiant,text='Institut-1',width=400,height=150,fg_color='white',text_color='#000',command=donninstitut1)
donne_institu2 = customtkinter.CTkButton(master=contenet_framegestionEtudiant,text='Institut-2',height=150,width=400,fg_color='green',command=donninstitut2)


title_lab.place(x=10,y=10,anchor='nw')
donne_fac1.place(x=10,y=100)
donne_fac2.place(x=500,y=100)
donne_fac3.place(x=10,y=300)
donne_institu1.place(x=10,y=480)
donne_institu2.place(x=500,y=480)
"""fin du conteneu page etudiant et son initialisation"""

#creation du contenu pour l apage faculte
mod = customtkinter.CTkButton(master=faculte_page,text="Valider Etudiant",command=vali)
lbEffectiftotal = customtkinter.CTkLabel(master=faculte_page,text="Effectifs Total : 230")
lbEffectifPaye = customtkinter.CTkLabel(master=faculte_page,text="Effectifs paye : 12",text_color='#180')
lbEffectifnonPaye = customtkinter.CTkLabel(master=faculte_page,text="Effectifs non paye : 20",text_color='#100')
tablegestion = ttk.Treeview(master=faculte_page,columns=(1,2,3,4,5,6,7,8,9,10,11),height=24,show="headings")

#initialisation du conteneu page gestion etudiant
lbEffectiftotal.place(x=830,y=5)
lbEffectifPaye.place(x=10,y=600)
lbEffectifnonPaye.place(x=10,y=620)
mod.place(x=200,y=5)

tablegestion.place(x=210,y=50)
tablegestion.heading(1,text="#")
tablegestion.heading(2,text='Nom')
tablegestion.heading(3,text='Prenom')
tablegestion.heading(4,text='Matricule')
tablegestion.heading(5,text='Campus')
tablegestion.heading(6,text='Departement')
tablegestion.heading(7,text='Faculte/Instiut')
tablegestion.heading(8,text='Annee')
tablegestion.heading(9,text='Tra-1')
tablegestion.heading(10,text='Tra-2')
tablegestion.heading(11,text='Tra-3')

tablegestion.column(1,width=10)
tablegestion.column(2,width=180)
tablegestion.column(3,width=110)
tablegestion.column(4,width=100)
tablegestion.column(5,width=100)
tablegestion.column(6,width=180)
tablegestion.column(7,width=210)
tablegestion.column(8,width=60)
tablegestion.column(9,width=80)
tablegestion.column(10,width=80)
tablegestion.column(11,width=80)

conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
conteneu_rep = "SELECT * FROM faculte_un"
aff = conn.cursor()
aff.execute(conteneu_rep)
for result in aff:
    tablegestion.insert('',END,values=result)
conn.commit()
conn.close()

#creation du conteneu page institut
lbEffectiftotal = customtkinter.CTkLabel(master=institut_page,text="Effectifs Total : 230")
lbEffectifPaye = customtkinter.CTkLabel(master=institut_page,text="Effectifs paye : 12",text_color='#180')
lbEffectifnonPaye = customtkinter.CTkLabel(master=institut_page,text="Effectifs non paye : 20",text_color='#100')
tablegestion = ttk.Treeview(master=institut_page,columns=(1,2,3,4,5,6,7,8,9,10,11),height=24,show="headings")

#initialisation du conteneu page gestion etudiant
lbEffectiftotal.place(x=830,y=5)
lbEffectifPaye.place(x=10,y=600)
lbEffectifnonPaye.place(x=10,y=620)

tablegestion.place(x=210,y=50)
tablegestion.heading(1,text="#")
tablegestion.heading(2,text='Nom')
tablegestion.heading(3,text='Prenom')
tablegestion.heading(4,text='Matricule')
tablegestion.heading(5,text='Campus')
tablegestion.heading(6,text='Departement')
tablegestion.heading(7,text='Faculte/Instiut')
tablegestion.heading(8,text='Annee')
tablegestion.heading(9,text='Tra-1')
tablegestion.heading(10,text='Tra-2')
tablegestion.heading(11,text='Tra-3')

tablegestion.column(1,width=10)
tablegestion.column(2,width=180)
tablegestion.column(3,width=110)
tablegestion.column(4,width=100)
tablegestion.column(5,width=100)
tablegestion.column(6,width=180)
tablegestion.column(7,width=210)
tablegestion.column(8,width=60)
tablegestion.column(9,width=80)
tablegestion.column(10,width=80)
tablegestion.column(11,width=80)

conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
conteneu_rep = "SELECT * FROM institut_un"
aff = conn.cursor()
aff.execute(conteneu_rep)
for result in aff:
    tablegestion.insert('',END,values=result)
conn.commit()
conn.close()



"""raiser to home page after i call a home page"""
home_page.tkraise()

#initialisation de la fenetre pour la faire fonctionner sur notre application
if __name__ == '__main__':
	app.mainloop()