import customtkinter
import tkinter
from tkinter import ttk


lbEffectiftotal = customtkinter.CTkLabel(master=contenet_framegestionEtudiant,text="Effectifs Total : 230")
lbEffectifPaye = customtkinter.CTkLabel(master=contenet_framegestionEtudiant,text="Effectifs paye : 12",text_color='#180')
lbEffectifnonPaye = customtkinter.CTkLabel(master=contenet_framegestionEtudiant,text="Effectifs non paye : 20",text_color='#100')
searchentry = customtkinter.CTkEntry(master=contenet_framegestionEtudiant,placeholder_text="Chercher un Etudiant ici..!",width=400,height=40)
btnsearch = customtkinter.CTkButton(master=contenet_framegestionEtudiant,text="Chercher",width=40,height=40,cursor="hand2", command=chercher)
tablegestion = ttk.Treeview(master=contenet_framegestionEtudiant,columns=(1,2,3,4,5,6,7,8,9),height=24,show="headings")

#initialisation du conteneu page gestion etudiant
lbEffectiftotal.place(x=830,y=5)
lbEffectifPaye.place(x=10,y=600)
lbEffectifnonPaye.place(x=10,y=620)
searchentry.place(x=250,y=50)
btnsearch.place(x=660,y=50)

tablegestion.place(x=2,y=100)
tablegestion.heading(1,text='Nom')
tablegestion.heading(2,text='Prenom')
tablegestion.heading(3,text='Campus')
tablegestion.heading(4,text='Matricule')
tablegestion.heading(5,text='Faculte/Instiut')
tablegestion.heading(6,text='Annee')
tablegestion.heading(7,text='Tra-1')
tablegestion.heading(8,text='Tra-2')
tablegestion.heading(9,text='Tra-3')

tablegestion.column(1,width=180)
tablegestion.column(2,width=140)
tablegestion.column(3,width=110)
tablegestion.column(4,width=100)
tablegestion.column(5,width=160)
tablegestion.column(6,width=60)
tablegestion.column(7,width=80)
tablegestion.column(8,width=80)
tablegestion.column(9,width=80)



