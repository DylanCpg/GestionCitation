from random import randrange

quotes = [
    "Exige beaucoup de toi-même et attends peu des autres. Ainsi beaucoup d'ennuis te seront épargnés.", 
    "Dans la vie on ne fait pas ce que l'on veut mais on est responsable de ce que l'on est.",
    "La vie est un mystère qu'il faut vivre, et non un problème à résoudre.",
    "On passe une moitié de sa vie à attendre ceux qu'on aimera et l'autre moitié à quitter ceux qu'on aime.",
    "La vie, c'est comme une bicyclette, il faut avancer pour ne pas perdre l'équilibre.",
    "Pour critiquer les gens il faut les connaître, et pour les connaître, il faut les aimer.",
    "Un seul être vous manque et tout est dépeuplé.",
    "Dans la vengeance et en amour, la femme est plus barbare que l'homme.",
    "L'homme veut être le premier amour de la femme, alors que la femme veut être le dernier amour de l'homme.",
    "Il ne faut avoir aucun regret pour le passé, aucun remords pour le présent, et une confiance inébranlable pour l'avenir.",
    "L'honnêteté, la sincérité, la simplicité, l'humilité, la générosité, l'absence de vanité, la capacité à servir les autres - qualités à la portée de toutes les âmes- sont les véritables fondations de notre vie spirituelle.",
    "Un sourire coûte moins cher que l'électricité, mais donne autant de lumière."
]

characters = [
    "Confusius", 
    "Sartre",
    "Gandhi",
    "Victor Hugo",
    "Albert Einshtein",
    "Coluche",
    "Lamartine",
    "Nietzsche",
    "Oscar Wilde",
    "Jean Jaurès",
    "Nelson Mandela",
    "Abbé Pierre"
]




def get_random_item_in(my_list):

        random =randrange(len(quotes))
        random =randrange(len(quotes))
          
        item = my_list[random] 
        print(item+" "+characters[random])
    
        return "\nUne autre citation ?"

def add_citation(quotes,characters):
        user_citation=input("Ajoutez votre citation")
        if(len(user_citation)!=0):
                quotes.append(user_citation)
        user_characters=input("Ajoutez le nom de l'auteur")
        if(len(user_characters)!=0):
                characters.append(user_characters)
        print(quotes)
        return "\najout réussi"
        
user_answer = input('Tapez entrée pour découvrir une autre citation, sur A pour ajouter une citation ou B pour quitter le programme.')

while user_answer != 'b' and user_answer != 'B' or user_answer=='A' :
        if user_answer=='A':
            add_citation(quotes,characters)
        if(len(quotes)>12):
                user_answer=input('Tapez entrée pour découvrir une autre citation, sur A pour ajouter une citation ou B pour quitter le programme.')
        print(get_random_item_in(quotes))
        if(len(quotes)==12):
                user_answer = input('Tapez entrée pour découvrir une autre citation, sur A pour ajouter une citation ou B pour quitter le programme.')
   

    
   

    
    
