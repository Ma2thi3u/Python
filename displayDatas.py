#coding:utf-8

import json

import tkinter

def valider():
    
    for datas in json.load(open("datas/datas.json")):
        if champ1.get() == datas["id"] and datas["mdp"] == champ2.get():
            fenetre.destroy()
            fenetreFiche = tkinter.Tk()
            fenetreFiche.title(datas["id"])
            labelFiche = tkinter.Label(text="Prénom : {}\nNom de famille : {}\nAge : {}\nMot de passe : {}\nNuméro de téléphone : {}\nEmail : {}".format(datas["name"], datas["surname"], datas["age"], datas["mdp"], datas["phone"], datas["email"]))
            labelFiche.pack()
            fenetreFiche.mainloop()
        else:
            pass    


fenetre = tkinter.Tk()
fenetre.title("")
label1 = tkinter.Label(fenetre, text="Identifiant : ")
label2 = tkinter.Label(fenetre, text="Mot de passe : ")
champ1 = tkinter.Entry(fenetre)
champ2 = tkinter.Entry(fenetre)
bouton = tkinter.Button(fenetre, text="Valider", command=valider)
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
champ1.grid(row=0, column=1)
champ2.grid(row=1, column=1)
bouton.grid(row=0, column=3, rowspan=2)
fenetre.mainloop()