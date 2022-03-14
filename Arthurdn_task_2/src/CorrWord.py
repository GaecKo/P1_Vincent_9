#!/usr/bin/python3
# -*- coding: utf-8 -*-
def word_in_string(word, string):
    for i in range(len(string) - len(word) + 1):
        if word[0].lower() == string[i].lower():
            goods = 0
            wrong = -1
            for j in range(len(word)):
                if word[j].lower() == string[i+j].lower():
                    goods += 1
                else:
                    wrong = i+j
            if goods >= len(word) - 1:
                return [i, wrong]
    return False