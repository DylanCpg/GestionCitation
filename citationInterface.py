from tkinter import *
from PIL import ImageTk,Image
from random import randrange
import webScraping as webScraping
import os
import csv
import requests
from bs4 import BeautifulSoup

quotes = []

characters = []

cpt=0
compteurSupression=0
compteurAjout=0

def get_random_item_in(my_list):

        global cpt
        global citation 
        random =randrange(len(quotes))
        random =randrange(len(quotes))
        
        item = my_list[random]
   
        
        if cpt>0:
                 citation.config(text=item+"\n"+characters[random])
                 longueur=citation.cget("text")
                 if len(longueur)>190:
                        saut=""
                        text=""
                        for i in range(len(longueur)):
                               
                                saut=saut+longueur[i]
                                if (longueur[i]=="." or  longueur[i]==":")and longueur[i+1]!="." and longueur[i+2]!="." :
                                        text=text+"\n"+saut
                                        saut=""
                                if longueur[i]=="." and longueur[i+1]==".":
                                       pass
                                citation.config(text=text+"\n"+characters[random])        
        if cpt==0:
                citation=Label(window, text=item+"\n"+characters[random], font=("Helvetica",10),bg='black',fg='white',justify="center")
                citation.place(relx = 0.5,  
                   rely = 0.4,
                   anchor = 'center')   
                cpt=cpt+1
        


def add_citation():
        global compteurAjout
        if compteurAjout==0:
                entry=Entry(justify='center')
                entry.place(relx =0.4,rely = 0.6)

                entryAuth=Entry(justify='center')
                entryAuth.place(relx =0.52,rely = 0.6)
                
                ajoutOk=Label(window, text="", font=("Helvetica",10),bg='black',fg='white')
                ajoutOk.place(relx =0.45,rely = 0.2)
        
                buttonValider2=Button(window,text='Valider ajout',font=("Helvetica",10),bg='grey',fg='white',height=0,command=lambda: ajout(entry,entryAuth,ajoutOk))
                buttonValider2.place(relx =0.44,rely = 0.68)

                buttonAnnuler2=Button(window,text='Annuler',font=("Helvetica",10),bg='grey',fg='white',height=0,command=lambda: annulerAjout(buttonValider2,buttonAnnuler2,entry,entryAuth,ajoutOk))
                buttonAnnuler2.place(relx =0.52,rely = 0.68)
                compteurAjout=1
                
def ajout(entry,entryAuth,ajoutOk):
        for i in range(len(quotes)):
                if entry.get()==quotes[i]:
                        existe="true"
                else:
                        existe="false"

        if existe=="false":  
                if(len(entry.get())!=0 and len(entryAuth.get())!=0 ):
                        quotes.append(entry.get())
                        characters.append(entryAuth.get())
                        ajoutOk.config(text="ajout fait")
                        ajoutOk.place(relx =0.49,rely = 0.63)
        if existe=="true" or (len(entry.get())==0 and len(entryAuth.get())==0 ):
                ajoutOk.config(text="échec de l'ajout")
                ajoutOk.place(relx =0.48,rely = 0.63)
                
def annulerAjout(buttonValider2,buttonAnnuler2,entry,entryAuth,ajoutOk):
        global compteurAjout
        buttonValider2.destroy()
        buttonAnnuler2.destroy()
        entry.destroy()
        entryAuth.destroy()
        ajoutOk.destroy()
        compteurAjout=0
        
def suppr_citation():
        global compteurSupression
     
        if compteurSupression==0:
                e=Entry(justify='center')
                e.pack(pady=50)
                
                supressionOk=Label(window, text="", font=("Helvetica",10),bg='black',fg='white')
                supressionOk.place(relx =0.45,rely = 0.2)
        
                buttonValider=Button(window,text='Valider suppression',font=("Helvetica",10),bg='grey',fg='white',height=0,command=lambda: supression(e,supressionOk))
                buttonValider.place(relx =0.43,rely = 0.25)

                buttonAnnuler=Button(window,text='Annuler',font=("Helvetica",10),bg='grey',fg='white',height=0,command=lambda: annuler(buttonValider,buttonAnnuler,e,supressionOk))
                buttonAnnuler.place(relx =0.53,rely = 0.25)
                compteurSupression=1
                
def supression(e,supressionOk):
        global characters
        for i in range(len(characters)):
                if characters[i]==e.get():
                        print(quotes[i])
                        del(characters[i])
                        del(quotes[i])
                        supressionOk.config(text="suppression ok")
                        supressionOk.place(relx =0.45,rely = 0.2)
                        print("suppression ok")
                        break 
                elif i==len(characters)-1 and characters[i]!=e.get():
                        supressionOk.config(text="l'auteur n'existe pas ou plus")
                        supressionOk.place(relx =0.42,rely = 0.2)
                        print("l'auteur n'existe pas")
                        

def annuler(buttonValider,buttonAnnuler,e,supressionOk):
          global compteurSupression
          buttonValider.destroy()
          e.destroy()
          buttonAnnuler.destroy()
          supressionOk.destroy()
          compteurSupression=0

        
def webScrap():
    requete = requests.get("https://dicocitations.lemonde.fr/citations-mot-liste.php")
    page = requete.content
    soup = BeautifulSoup(page,"html.parser")

    a = soup.find_all("a", {"class": "lienmot"})
    strong =soup.find_all("strong")
    global quotes
    global characters
   
    liste_citations = [elt.string.strip() for elt in a]
    liste_auteurs=[elt.string.strip() for elt in strong]
    del liste_citations[0]
    del liste_auteurs[0]
    
    del liste_citations[len(liste_citations)-1]
    del liste_citations[len(liste_citations)-1]
    quotes.extend(liste_citations)
    characters.extend(liste_auteurs)   


window=Tk()

webScrap()

window.title("Gestionaire de citations")
window.geometry("1600x900")
window.minsize(480,360)
window.config(background='black')


title=Label(window, text="Bienvenue sur notre application de citation", font=("Helvetica",30),bg='black',fg='white')
title.pack()

button=Button(window,text='Citation',font=("Helvetica",20),bg='grey',fg='white',justify="left",command=lambda: get_random_item_in(quotes))
button.place(relx = 0.45,rely = 0.5)

buttonSuppr=Button(window,text='Suppression',font=("Helvetica",20),bg='grey',fg='white',justify="center",command=suppr_citation)
buttonSuppr.place(relx = 0.25,rely = 0.5)

buttonAdd=Button(window,text='Ajout',font=("Helvetica",20),bg='grey',fg='white',justify="center",command=add_citation)
buttonAdd.place(relx = 0.6,rely = 0.5)

window.mainloop()







   

    
    
