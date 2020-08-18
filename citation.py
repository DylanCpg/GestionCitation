from random import randrange
import webScraping as webScraping
import os
import csv
import requests
from bs4 import BeautifulSoup

quotes = []

characters = []




def get_random_item_in(my_list):

        random =randrange(len(quotes))
        random =randrange(len(quotes))
          
        item = my_list[random]
        print(item+characters[random])
    
        return "\nUne autre citation ?"

def add_citation(quotes,characters):
        user_citation=input("Ajoutez votre citation")
        if(len(user_citation)!=0):
                quotes.append(user_citation)
        user_characters=input("Ajoutez le nom de l'auteur")
        if(len(user_characters)!=0):
                characters.append(user_characters)
        
        return "\najout réussi"

def suppr_citation(quotes,characters):
        user_authCitation=input("Donner l'auteur de la citation à supprimer")
        for i in range(len(characters)):
                if characters[i]==user_authCitation:
                        del(characters[i])
                        del(quotes[i])
                        return "suppression ok"
                elif i==len(characters)-1 and characters[i]!=user_authCitation:
                        print("l'auteur n'existe pas")

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


user_answer = input('Tapez entrée pour découvrir une autre citation, sur A pour ajouter une citation, sur S pour supprimer ou B pour quitter le programme.\n')
webScrap()




while (user_answer != 'b' and user_answer != 'B') or user_answer=='A' or user_answer=='S' :
        if user_answer=='A':
            add_citation(quotes,characters)
        elif user_answer=='S':
                 suppr_citation(quotes,characters)
        else:   
                print(get_random_item_in(quotes))
               
        user_answer=input('Tapez entrée pour découvrir une autre citation, sur A pour ajouter une citation, sur S pour supprimer ou B pour quitter le programme.\n')
    
   

    
    
