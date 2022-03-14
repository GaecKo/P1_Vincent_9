#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrCaseControl as correct
import CaseControl as student

def random_list_creator(): # créé une liste de taille entre 0 et 50, avec des éléments aléatoires entre 0 et 200
    return [random.randint(0, 200) for i in range(random.randint(0, 50))] 

class TestCaseControl(unittest.TestCase):

    def test_empty_list(self):
        correct_ans = correct.case_control([])
        student_ans = student.case_control([])
        self.assertEqual(correct_ans,student_ans,"Votre fonction ne retourne pas correctement une liste vide")

    def test_high_weight_luggage(self):
        args = [[17, 18, 19], [25, 35, 21], [19, 27, 17]] # faire des arguments avec quelques tests simples
        rep = ("Votre fonction a retourné {} au lieu de {} avec comme arguments: {}. Il semble que votre code ait du mal avec des valises de plus de 16kg.")
        for liste in args: # lancement des tests pour chaque liste
            try: # essaye d'avoir la réponse de l'étudiant, au cas où il y aurait une erreur
                student_ans = student.case_control(liste) # réponse étudiante
            except Exception as e: # en cas d'erreur
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, liste )) # affiche l'erreur 
            correct_ans = correct.case_control(liste) # réponse correcte
            self.assertEqual(student_ans, correct_ans, rep.format(student_ans, correct_ans, liste)) # comparaison entre la bonne réponse et celle de l'étudiant
    
    def test_high_total_weight_luggage(self):
        args = [[8,8,8],[8,7,6,8],[10],[8,8]]
        rep = ("Votre fonction a retourné {} au lieu de {} avec comme arguments: {}. On dirait bien que votre fonction a du mal avec le poids total des valises.")
        for liste in args: # lancement des tests pour chaque liste
            try: # essaye d'avoir la réponse de l'étudiant, au cas où il y aurait une erreur
                student_ans = student.case_control(liste) # réponse étudiante
            except Exception as e: # en cas d'erreur
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, liste )) # affiche l'erreur 
            correct_ans = correct.case_control(liste) # réponse correcte
            self.assertEqual(student_ans, correct_ans, rep.format(student_ans, correct_ans, liste)) # comparaison entre la bonne réponse et celle de l'étudiant
    
    def test_random_list(self):
        args = [[1, 2, 3], [4, 8, 10], [19, 7, 8]] # faire des arguments avec quelques tests simples
        for _ in range(20):
            args.append(random_list_creator()) # ajout de 20 listes aléatoires dans notre liste d'arguments
        rep = ("Votre fonction a retourné {} au lieu de {} avec comme arguments: {}.") # message si fausse réponse
        for liste in args: # lancement des tests pour chaque liste
            try: # essaye d'avoir la réponse de l'étudiant, au cas où il y aurait une erreur
                student_ans = student.case_control(liste) # réponse étudiante
            except Exception as e: # en cas d'erreur
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, liste )) # affiche l'erreur 
            correct_ans = correct.case_control(liste) # réponse correcte
            self.assertEqual(student_ans, correct_ans, rep.format(student_ans, correct_ans, liste)) # comparaison entre la bonne réponse et celle de l'étudiant

if __name__ == '__main__':
    unittest.main()
