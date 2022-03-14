#!/usr/bin/python3
# -*- coding: utf-8 -*-


def moyenne(li):
    """
    @pre: 'li' est une liste contenant des nombres entiers, réels,
    des mots, voire des caractères spéciaux, chaque élément de 
    la liste étant transformé en une chaine de caractères

    @post : retourne la moyenne de chaque nombre de la liste 'li' 
    en fonction du nombre d'éléments se trouvant dans celle-ci, 
    retourne False si la liste ne contient pas de nombres
    
    Attention: la moyenne doit être un nombre entier !
    """
    l = []
    calc = 0
    for i in range(len(li)):
        char = ''
        for j in range(len(li[i])):
            if li[i][j] in '0123456789':
                char+=li[i][j]
        if char != '':
            l.append(int(char))
    if l == []:
        return False
    for k in range(len(l)):
        calc+=l[k] 
    return calc//len(li)