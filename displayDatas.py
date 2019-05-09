#! usr/bin/env python3
# coding:utf-8

import json

import tkinter


def valider():

    for datas in json.load(open("datas/datas.json")):
        
        if champId.get() == datas["id"] and datas["mdp"] == champMdp.get():
            
            fiche = ("Prénom : " + datas["name"] + "\n" 
                     + "Nom de famille : " + datas["surname"] + "\n" 
                     + "Age : " + str(datas["age"]) + "\n"
                     + "Mot de passe : " + datas["mdp"] + "\n"
                     + "Numéro de téléphone : " + datas["phone"] + "\n"
                     + "Email : " + datas["email"])
            
            fenetreFormulaire.destroy()
            
            fenetreFiche = tkinter.Tk()
            fenetreFiche.title(datas["id"])
            
            labelFiche = tkinter.Label(text=fiche)
            labelFiche.pack()
            fenetreFiche.mainloop()

# Créer la fenetre du formulaire
fenetreFormulaire = tkinter.Tk()
fenetreFormulaire.title("")

# Creer une frame
frame = tkinter.Frame(fenetreFormulaire, bg="#cef1d3")

# Personnaliser la fenetre
fenetreFormulaire.geometry("720x480")
fenetreFormulaire.config(background="#cef1d3")

labelId = tkinter.Label(frame, text="Identifiant : ", bg="#cef1d3")
champId = tkinter.Entry(frame, bg="#cef1d3")

labelMdp = tkinter.Label(frame, text="Mot de passe : ", bg="#cef1d3")
champMdp = tkinter.Entry(frame, show="*", bg="#cef1d3")

boutonValider = tkinter.Button(fenetreFormulaire, text="Valider", highlightbackground="#a8cbfa", height=5, command=valider)

# Afficher les elements
labelId.grid(column=0, row=0, pady=10)
champId.grid(column=1, row=0, pady=10)
labelMdp.grid(column=0, row=1, pady=10)
champMdp.grid(column=1, row=1, pady=10)

frame.pack(expand="YES")
boutonValider.pack(fill=tkinter.X)

fenetreFormulaire.mainloop()