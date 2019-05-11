#! usr/bin/env python3
# coding:utf-8

import json

import tkinter


def valider():

    for datas in json.load(open("datas/datas.json")):
        
        if champId.get() == datas["id"] and datas["mdp"] == champMdp.get():
            
            fichePrenom = "Prénom : " + datas["name"]
            ficheNom = "Nom de famille : " + datas["surname"]
            ficheAge = "Age : " + str(datas["age"])
            ficheMdp = "Mot de passe : " + datas["mdp"]
            fichePhone = "Numéro de téléphone : " + datas["phone"]
            ficheEmail = "Email : " + datas["email"]
            
            fenetreFormulaire.destroy()
            
            fenetreFiche = tkinter.Tk()
            fenetreFiche.title(datas["id"])
            
            frameFiche = tkinter.Frame(fenetreFiche, bg="#cef1d3")
            
            fenetreFiche.geometry("720x480")
            fenetreFiche.config(background="#cef1d3")
            
            labelFichePrenom = tkinter.Label(frameFiche, text=fichePrenom, bd=1, relief="solid", bg="#F2A6A6", width=30)
            labelFicheNom = tkinter.Label(frameFiche, text=ficheNom, bd=1, relief="solid", bg="#D1A6F2", width=30)
            labelFicheAge = tkinter.Label(frameFiche, text=ficheAge, bd=1, relief="solid", bg="#A6C6F2", width=30)
            labelFicheMdp = tkinter.Label(frameFiche, text=ficheMdp, bd=1, relief="solid", bg="#F2F1A6", width=30)
            labelFichePhone = tkinter.Label(frameFiche, text=fichePhone, bd=1, relief="solid", bg="#F2CC85", width=30)
            labelFicheEmail = tkinter.Label(frameFiche, text=ficheEmail, bd=1, relief="solid", bg="#97DCA1", width=30)
            
            labelFichePrenom.grid(column=0, row=0, pady=10, padx=10, ipady=10, ipadx=10)
            labelFicheNom.grid(column=1, row=0, pady=10, padx=10, ipady=10, ipadx=10)
            labelFicheAge.grid(column=0, row=1, pady=10, padx=10, ipady=10, ipadx=10)
            labelFicheMdp.grid(column=1, row=1, pady=10, padx=10, ipady=10, ipadx=10)
            labelFichePhone.grid(column=0, row=2, pady=10, padx=10, ipady=10, ipadx=10)
            labelFicheEmail.grid(column=1, row=2, pady=10, padx=10, ipady=10, ipadx=10)
            
            frameFiche.pack(expand="YES")
            
            fenetreFiche.mainloop()

# Create the tkinter window
fenetreFormulaire = tkinter.Tk()
fenetreFormulaire.title("")

# Create a frame
frame = tkinter.Frame(fenetreFormulaire, bg="#cef1d3")

# Customize the window
fenetreFormulaire.geometry("720x480")
fenetreFormulaire.config(background="#cef1d3")

# Create the elements of the window (label, entry and button)
labelId = tkinter.Label(frame, text="Identifiant : ", bg="#cef1d3")
champId = tkinter.Entry(frame, bg="#cef1d3")

labelMdp = tkinter.Label(frame, text="Mot de passe : ", bg="#cef1d3")
champMdp = tkinter.Entry(frame, show="*", bg="#cef1d3")

boutonValider = tkinter.Button(fenetreFormulaire, text="Valider", highlightbackground="#a8cbfa", height=5, command=valider)

# Display the elements of the window (label, entry and button)
labelId.grid(column=0, row=0, pady=10)
champId.grid(column=1, row=0, pady=10)
labelMdp.grid(column=0, row=1, pady=10)
champMdp.grid(column=1, row=1, pady=10)

frame.pack(expand="YES")
boutonValider.pack(fill=tkinter.X)

# Display the window
fenetreFormulaire.mainloop()