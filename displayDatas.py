# coding:utf-8

import json

import tkinter


def valider():

    for datas in json.load(open("datas/datas.json")):
        if champId.get() == datas["id"] and datas["mdp"] == champMdp.get():
            fenetreFormulaire.destroy()
            fenetreFiche = tkinter.Tk()
            fenetreFiche.title(datas["id"])
            labelFiche = tkinter.Label(
                text="Prénom : {}\nNom de famille : {}\nAge : {}\nMot de passe : {}\nNuméro de téléphone : {}\nEmail : {}".format(
                    datas["name"],
                    datas["surname"],
                    datas["age"],
                    datas["mdp"],
                    datas["phone"],
                    datas["email"],
                )
            )
            labelFiche.pack()
            fenetreFiche.mainloop()
        else:
            pass


fenetreFormulaire = tkinter.Tk()
fenetreFormulaire.title("")
labelId = tkinter.Label(fenetreFormulaire, text="Identifiant : ")
labelMdp = tkinter.Label(fenetreFormulaire, text="Mot de passe : ")
champId = tkinter.Entry(fenetreFormulaire)
champMdp = tkinter.Entry(fenetreFormulaire, show="*")
boutonValider = tkinter.Button(fenetreFormulaire, text="Valider", command=valider)
labelId.grid(row=0, column=0)
labelMdp.grid(row=1, column=0)
champId.grid(row=0, column=1)
champMdp.grid(row=1, column=1)
boutonValider.grid(row=0, column=3, rowspan=2)
fenetreFormulaire.mainloop()
