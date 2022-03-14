#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import random
import time

import CorrAbs as correct
import abs as student

#Liste d'argument généré aléatoirement pour tester la fonction de l'étudiant (des valeurs de bases sont ajoutées manuellements
#pour compléter la liste aléatoire)
liste_arg = random.sample(range(0, 25), 10)
liste_arg.append(0)
liste_arg.append(1)

#Liste d'indices pour aider l'étudiant, ils seront sélectionnés aléatoirements, un à la fois.
indices = ["Indice: Evitez les boucles inutiles.",
          "Indice: Evitez les boucles imbriquées.",
          "Indice: Votre fonction présente-t-elle de la redondance dans son code ?",
          "Indice: Votre fonction présente-t-elle de la redondance dans son exécution ?",
          "Indice: Evitez les fonctions built-in de python, elle peuvent prendre plus de temps que nécéssaire.",
          ]

class TestExtreme_list(unittest.TestCase):

    #Premier test vérifie si la fonction de l'étudiant retourne bien une liste, elle vérifie donc le type de la réponse.
    def test_0(self): 
        rep = ("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument. \nLa réponse attendue est une une liste contenant {}.")
        try:
            student_ans = student.extreme_list(5)
        except Exception as e:
            self.fail("Votre fonction provoque l'erreur {}: {} avec argument {}".format(type(e), e, n))
        correct_ans = correct.extreme_list(5)
        if type(student_ans) == list:
            the_type = True
        else: 
            the_type = False
        self.assertTrue(the_type, rep.format(student_ans, 5, correct_ans))

    #Teste la fonction de l'étudiant et compare les réponses attentudes avec des arguments généré aléatoirement (plus haut dans     #le code)
    def test_1(self):
        args = liste_arg
        rep = ("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument. \nLa bonne réponse est {}.")
        for n in args:
            try:
                student_ans = student.extreme_list(n)
            except Exception as e:
                self.fail("Votre fonction provoque l'erreur {}: {} avec argument {}".format(type(e), e, n))
            correct_ans = correct.extreme_list(n)
            self.assertEqual(student_ans, correct_ans, rep.format(student_ans, n, correct_ans))

    #Compare la moyenne du temps d'exécution de la fonction de l'étudiant avec le correctif. 
    #En effecutant 100 run de chaque algorithme à chaque fois avec l'argument 1000, on prend une moyenne des résultats et           #l'algorithme est considéré comme suffisement rapide si il est au moins 40 fois plus rapide que l'algorithme de référence       #sur les 100 runs
    def test_2(self):
        algo = False
        student_moyenne = 0
        correct_moyenne = 0
        ratio = 0
        for i in range (100):
            rep = ("Votre fonction n'est pas assez rapide, elle a prit en moyenne {} secondes avec l'argument 1000,\nFibonnaci attend un temps d'exécution inférieur ou égal à {}.\nVous prennez {} secondes de trop.\n{}")
            start_time_01 = time.time()
            student.extreme_list(1000)
            student_time = (time.time() - start_time_01)
            start_time_02 = time.time()
            correct.extreme_list(1000)
            correct_time = (time.time() - start_time_02)
            if correct_time >= student_time:
                ratio += 1
            student_moyenne += student_time
            correct_moyenne += correct_time
        if ratio >= 40:
            algo = True

        try:
            ratio = 100
#Le message d'erreur retourne les résultats du temps d'exécutions ainsi qu'un indice pour l'étudiant
        except Exception as e:
            self.fail("Votre fonction provoque l'erreur {}: {} avec argument {}".format(type(e), e, n))
        self.assertTrue(algo, rep.format('{:.8f}'.format((student_time/100)),'{:.8f}'.format((correct_time/100)) ,'{:.8f}'.format(((student_time/100)-(correct_time/100))),(indices[(random.randint(0, 5))])))
   
            


if __name__ == '__main__':
    unittest.main()
