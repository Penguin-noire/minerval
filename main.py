#coding:utf-8
#importation des modules 
import tkinter
import customtkinter
from tkinter import *
from customtkinter import *
import mysql.connector
import couleur
from tkinter import messagebox
import os
from os import *


#creation de  la fenetre d'auverture du logiciel

fen = tkinter.Tk()
fen.title('Application de gestion de Paiement de Minerval')
fen.geometry('800x500')
fen.resizable(False,False)
#cration des fonctions

def valider(): 
    #LES variable globalapp.Run();
    #global username
    #global mot_pass 
    
    #reception des input avec get
    confirmation = messagebox.askquestion("Vous etes sur De!",'vouloir se connecter')
    if confirmation == "yes":
        username = input_username.get()
        mot_pass = input_pass.get()
    
        #suppresion des donnees input apres la validation du formulaire
        input_username.delete(0,END)
        input_pass.delete(0,END)
        
        #on va test si les variables que ne sont pas vide
        
        if username == "" or mot_pass == "":
            
            messagebox.showwarning("Alerte !!",'Veiller completer les case vides')
            
        else:
            #on va se connecte a la base des donnees puis login     
            conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
            ch = conn.cursor()
            ch.execute("SELECT * FROM user")
            res = ch.fetchall()
            for resultat in res:
                if username == resultat[3] or mot_pass == resultat[5]:
                    os.popen("python3 my_application.py")
                    fen.quit()
                else:
                    messagebox.showwarning("Error","Adresse ou pass incorrect")

            conn.commit()
            conn.close()
    elif confirmation == 'no':
        pass



def creeCompte():
    os.popen("python3 registre.py")
    fen.quit()



#cration des label pour text
login_label_text = customtkinter.CTkLabel(master=fen,text="Se Connecter",font=('sans-serif',40),text_color=couleur.orange_color)
lable_username = customtkinter.CTkLabel(master=fen,text="Adresse Mail :",text_color=couleur.black_color)
label_pass = customtkinter.CTkLabel(master=fen,text='Mot de pass :',text_color=couleur.black_color)

#creation des des entre et des input pour se connecter
input_username = customtkinter.CTkEntry(master=fen,width=400,height=40,placeholder_text="Adresse Mail *",fg_color=couleur.white_color,
                                        text_color=couleur.black_color)

input_pass = customtkinter.CTkEntry(master=fen,width=400,height=40,placeholder_text="Mot de pass *",fg_color=couleur.white_color,
                                    text_color=couleur.black_color)


#creation des boutons pour valider le formulaire
btn_connexion = customtkinter.CTkButton(master=fen,text="Connexion",width=400,height=40,text_color=couleur.white_color,
                                        fg_color=couleur.orange_color,cursor='hand2',font=('sans-serif',15),
                                        command=valider)

btn_createAccount = customtkinter.CTkButton(master=fen,text="Cree un compte! si vous n'avez pas",command=creeCompte)
                                            









#activation des labels
login_label_text.pack(pady=15)
lable_username.place(x=205,y=90)
label_pass.place(x=205,y=180)

#activation des entres
input_username.place(x=200,y=120)
input_pass.place(x=200,y=210)

#activation des bouton pour valider le formulaire
btn_connexion.place(x=200,y=300)
btn_createAccount.place(x=300,y=370)



#actiovation de la fenetre avec mainloop
fen.config(bg=couleur.white_color)
fen.mainloop()
