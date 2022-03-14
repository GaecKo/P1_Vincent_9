#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Cette fonction représente une solution atteignable, elle n'est volontairement pas optimisée (en terme de temps, d'espace, etc)
#Pour que l'exercice soit accessible, étant donné que cette fonction servira de point de repaire pour comparer les temps #d'exécutions avec les réponses des étudiants.
def extreme_list(n):
    liste = []
    f_liste = []
    for i in range (n+1):
        liste.append(i)
    for a in range (n+1):
        if len(liste) != 0:
            f_liste.append(liste[0])
            del liste[0]
            if len(liste) != 0:
                f_liste.append(max(liste))
                liste.remove(max(liste))
                
    return f_liste
    
    
    
