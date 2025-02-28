import tkinter
import customtkinter
from tkinter import *
from customtkinter import *
import mysql.connector
import couleur
from tkinter import messagebox
import os
from os import *


#cration des fenentre registre account
fenRegistre = tkinter.Tk()
fenRegistre.title("Cree un compte sur notre plateforme")
fenRegistre.resizable(False,False)
fenRegistre.geometry("900x600")

#defintion des fonction pour valider notre formulaire

def validerform():
	nom = str(nom_input.get())
	prenom = str(prenom_input.get())
	adresse = str(adresse_input.get())
	fonction = str(combox_input.get())
	mdp = str(pass_input.get())
	if nom == "" or prenom == "" or adresse == "" or fonction == "" or mdp == "":
		messagebox.showinfo("Attetion","Cases vides....!")
	else:
		conn = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
		ajou = conn.cursor()
		rep = "INSERT INTO user(nom,prenom,adresse,fonction,mdp) VALUES(%s,%s,%s,%s,%s)"
		ajou.execute(rep,(nom,prenom,adresse,fonction,mdp))
		if ajou:
			nom_input.delete(0,END)
			prenom_input.delete(0,END)
			adresse_input.delete(0,END)
			pass_input.delete(0,END)
			os.popen("python3 main.py")
			fenRegistre.quit()
        
		conn.commit()
		conn.close()
	

#creation d un title sur notre forum
regitre_title = customtkinter.CTkLabel(master=fenRegistre,text="S'inscrire sur Minesoft",text_color=couleur.orange_color,font=("sans-serif",30))

nom_label = customtkinter.CTkLabel(master=fenRegistre,text="Votre Nom :",text_color=couleur.black_color)
prenom_label = customtkinter.CTkLabel(master=fenRegistre,text='Votre Prenom :',text_color=couleur.black_color)
adresse_label = customtkinter.CTkLabel(master=fenRegistre,text='Votre Adresse :',text_color=couleur.black_color)
fonction_label = customtkinter.CTkLabel(master=fenRegistre,text="Fonction :",text_color=couleur.black_color)
pass_label = customtkinter.CTkLabel(master=fenRegistre,text="Mot de pass :",text_color=couleur.black_color)
#creation des labels entre sur le forum

nom_input = customtkinter.CTkEntry(master=fenRegistre,placeholder_text="Votre Nom ici........?*"
                                   ,width=450,height=40,fg_color=couleur.white_color,text_color=couleur.black_color)

prenom_input = customtkinter.CTkEntry(master=fenRegistre,placeholder_text="votre Prenom..."
                                      ,width=450,height=40,fg_color=couleur.white_color,text_color=couleur.black_color)

adresse_input = customtkinter.CTkEntry(master=fenRegistre,placeholder_text="votre adresse..."
                                       ,width=450,height=40,fg_color=couleur.white_color,text_color=couleur.black_color)

option_defaut = customtkinter.StringVar(value = 'Aucune')

combox_input = customtkinter.CTkComboBox(master=fenRegistre,values=['Aucune','Directeur Academique','Directrice Academique','Economat','Doyen','Planton']
	                        ,width=450,height=40,fg_color=couleur.white_color,text_color=couleur.black_color,variable=option_defaut)

pass_input = customtkinter.CTkEntry(master=fenRegistre,placeholder_text="Mot de pass....*",fg_color=couleur.white_color
                                    ,width=450,height=40,text_color=couleur.black_color,show="*")

#cration d'un boutonn de validation du formulaire

valide_buttom = customtkinter.CTkButton(master=fenRegistre,text="Valider",text_color=couleur.white_color
                                        ,fg_color=couleur.orange_color,cursor="hand2",command=validerform)

#activation des labels et des bouton plus input
regitre_title.pack(pady=20,padx=20)
nom_label.place(x=260,y=70)
prenom_label.place(x=260,y=150)
adresse_label.place(x=260,y=220)
fonction_label.place(x=260,y=300)
pass_label.place(x=260,y=380)




# activation des entre de saisie
nom_input.place(x=250,y=100)
prenom_input.place(x=250,y=180)
adresse_input.place(x=250,y=250)
combox_input.place(x=250,y=330)
pass_input.place(x=250,y=410)

#validation du bouttom
valide_buttom.place(x=400,y=480)
#validation de la fenetre registre avec la fonction mainloop
fenRegistre.config(bg=couleur.white_color)
fenRegistre.mainloop()