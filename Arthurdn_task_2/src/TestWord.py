#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import random

import CorrWord as correct
import WordString as student

def create_word_in_with_difference():
    """
    pre: /
    post: Une liste avec en index 0 un mot aléatoire et en index 2 une chaine de caractère dans lequel se trouve le mot avec une différence.
    -> Fonction qui créée aléatoirement un mot qui se trouvent dans le string avec une différence / erreur.
    """
    letter = "abCdeFghIjkLmnopQrsTuvWxyZ1234567890"
    mot = ""
    string = ""
    taille_mot = 0
    for i in range(random.randint(3, 20)):  # création du mot
        mot += letter[random.randint(0, 35)] 
        taille_mot += 1
    for i in range(random.randint(0, 10)): # création du string 
        string += letter[random.randint(0, 35)]
    
    random_index = random.randint(1, taille_mot) 
    changed_word = mot[0:random_index] + letter[random.randint(0, 35)] + mot[random_index+1:] # création du mot modifié pour l'ajouter au string
    string += changed_word
    for i in range(random.randint(0, 10)):
        string += letter[random.randint(0, 35)]
    return [mot, string]

def create_word_in():
    """
    pre: /
    post: Une liste avec en index 0 un mot aléatoire et en index 2 une chaine de caractère dans lequel se trouve le mot.
    -> Fonction qui créée aléatoirement un mot qui se trouvent dans le string
    """
    letter = "abCdeFghIjkLmnopQrsTuvWxyZ1234567890"
    mot = ""
    string = ""
    for i in range(random.randint(3, 20)):  # création du mot
        mot += letter[random.randint(0, 35)] 
    for i in range(random.randint(0, 10)): # création du string 
        string += letter[random.randint(0, 35)]
    string += mot
    for i in range(random.randint(0, 10)):
        string += letter[random.randint(0, 35)]
    return [mot, string]

class TestWordString(unittest.TestCase):
    def test_0_None(self):
        """
        Test vérifiant que la fonction de l'étudiant renvoit bien quelque chose et ce sans erreurs.
        """
        args = [["salUt", "salutc'estmoi"], ["ouh", "misterouhouh"]]
        rep = ("Votre fonction a retourné None pour {} comme argument. Avez-vous bien mis un/des return dans votre code?")
        for n in args:
            try:
                student_ans = student.word_in_string(n[0], n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, '"'+ n[0] + '"', '"'+ n[1] + '"'))
            self.assertIsNotNone(student_ans, rep.format(n))
    
    def test_1_word_in_string(self):
        """
        Test vérifiant les cas où le mot est simplement dans le string, sans différence. Il y est aussi utilisé create_word_in() qui génère des tests.
        """
        args = [["test", "testsHouldbeok"], ["çamarche", "estcequeçamArche"], ["HELLO", "nohello"], ["salUT", "aaasalUT"]]
        for i in range(20):
            tests = create_word_in()
            args.append(tests)
        rep = ("Votre fonction a retourné {} au lieu de {} avec comme arguments: {} et {}.")
        for n in args:
            try:
                student_ans = student.word_in_string(n[0], n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, '"'+ n[0] + '"', '"'+ n[1] + '"'))
            correct_ans = correct.word_in_string(n[0], n[1])
            print(correct_ans)
            self.assertEqual(student_ans, correct_ans, rep.format(student_ans, correct_ans, '"'+ n[0] + '"', '"'+ n[1] + '"'))
        
    def test_2_word_in_string_with_differnce(self):
        """
        Test vérifiant les cas où le mot est dans le string, avec cependant une différence. Le programme devrait cependant quand même 
        indiquer que le mot est dans le string et donner l'index de l'erreur.
        """
        args = [["test", "tSstshouldbeok"], ["çaMarche", "estcequeçaXarche"], ["pourQUOI", "pourKuoi"], ["SAUT", "aaasSWUT"], ["sAlUt", "SalXtc'estmoi"], ["oUh", "misteroxhouh"]]
        for i in range(20):
            tests = create_word_in_with_difference()
            args.append(tests)
        rep = ("Votre fonction a retourné {} au lieu de {} avec comme arguments: {} et {}. Votre fonction accepte-t-elle bien une différence?")
        for n in args:
            try:
                student_ans = student.word_in_string(n[0], n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, '"'+ n[0] + '"', '"'+ n[1] + '"'))
            correct_ans = correct.word_in_string(n[0], n[1])
            self.assertEqual(student_ans, correct_ans, rep.format(student_ans, correct_ans, '"'+ n[0] + '"', '"'+ n[1] + '"'))

    def test_2_word_not_in_string(self):
        """
        Test vérifiant les cas où le mot n'est tout simplement pas dans le string. 
        """
        args = [["TEST", "tisstshouldnotbeok"], ["çamARCHE", "estcequeçaaaarche"], ["pourqoi", "pourmmoiquoi"], ["saut", "aaasalwt"], ["salut", "salutc'estmoi"], ["ouh", "misterhou"]]
        rep = ("Votre fonction a retourné {} au lieu de {} avec comme arguments: {} et {}. Votre fonction vérifie bien l'égalité entre le mot et le string?")
        for n in args:
            try:
                student_ans = student.word_in_string(n[0], n[1])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {} et {}".format(type(e), e, '"'+ n[0] + '"', '"'+ n[1] + '"'))
            correct_ans = correct.word_in_string(n[0], n[1])
            self.assertEqual(student_ans, correct_ans, rep.format(student_ans, correct_ans, '"'+ n[0] + '"', '"'+ n[1] + '"'))
        
if __name__ == "__main__":
    unittest.main()