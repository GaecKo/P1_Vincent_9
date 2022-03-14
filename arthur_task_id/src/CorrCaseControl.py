#!/usr/bin/python3
# -*- coding: utf-8 -*-
def case_control(l):
    """
    @pre : l est une liste comprenant des nombres
    @post : 
    """
    to_pay = 0
    if sum(l[:]) > (6 * len(l)) + 3: to_pay += sum(l[:]) - ((6 * len(l)) + 3)
    for i in l:
        if i > 16: to_pay += 100
        elif i > 8: to_pay += 5*(i-8)    
    return to_pay

