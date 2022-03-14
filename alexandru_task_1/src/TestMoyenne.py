#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

import CorrectionMoyenne as correct
import student_code as student

import random   
import string  
import secrets

def random_list():
    lis = []
    longueur = 10 # define the length of the string
    k = random.randint(5, 10)
    for i in range(k):
        resultat = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(longueur))  
        lis.append(str(resultat))
    return lis

class TestMoyenne(unittest.TestCase):
    
    def test_instance(self):
        args = []
        for i in range(10):
            args.append(random_list())
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {}\ncomme argument alors que la réponse attendue est {}. \nL'instance de votre réponse ({}) n'équivaut pas à l'instance de la réponse attendue (Int).")
        for n in args:
            try:
                student_ans = student.moyenne(n)
                if isinstance(student_ans, str):
                    reponse = "String"
                elif isinstance(student_ans, float):
                    reponse = "Float"
                else:
                    reponse = ""
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.moyenne(n)
            self.assertIsInstance(student_ans, type(1),
                             rep.format(type(student_ans), n, type(correct_ans), reponse))
            
    def test0_None(self):
        args = []
        for i in range(10):
            args.append(random_list())
        rep = _("Votre fonction a retourné None pour {} comme argument.\nCela implique probablement qu'il manque un return dans votre code.")
        for n in args:
            try:
                student_ans = student.moyenne(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            self.assertIsNotNone(student_ans, rep.format(n))

    def test1_moy(self):
        args = []
        for i in range(10):
            args.append(random_list())
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {}\ncomme argument alors que la réponse attendue est {}.\n{}")
        for n in args:
            try:
                student_ans = student.moyenne(n)
                if isinstance(student_ans, str):
                    reponse = "N'oubliez pas que votre réponse doit être un nombre entier (pas de type float non plus) !"
                elif isinstance(student_ans, float):
                    reponse = "N'oubliez pas que vous devez faire une division entière !"
                else:
                    reponse = ''
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.moyenne(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans, reponse))

    def test1_no_numbers(self):
        args = [[' ', 'c', 'tù`ze-_'], [] , ['', '', '', '']]
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {}\ncomme argument alors que la réponse attendue est {} puisque aucun nombre n'est présent dans la liste.")
        for n in args:
            try:
                student_ans = student.moyenne(n)
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.moyenne(n)
            self.assertTrue(isinstance(student_ans, bool), f"Vous avez renvoyé {student_ans} à la place de {correct_ans} avec comme argument {n}, votre réponse n'est pas un booléen! \nVotre fonction aurait dû retourner False.")
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans))

    def test2_moy(self):
        args = []
        for i in range(10):
            args.append(random_list())
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {}\ncomme argument alors que la réponse attendue est {}.\n{}")
        for n in args:
            try:
                student_ans = student.moyenne(n)
                if isinstance(student_ans, str):
                    reponse = "N'oubliez pas que votre réponse doit être un nombre entier (pas de type float non plus) !"
                elif isinstance(student_ans, float):
                    reponse = "N'oubliez pas que vous devez faire une division entière !"
                else:
                    reponse = ''
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, n))
            correct_ans = correct.moyenne(n)
            self.assertEqual(student_ans, correct_ans,
                             rep.format(student_ans, n, correct_ans, reponse))

if __name__ == '__main__':
    unittest.main()