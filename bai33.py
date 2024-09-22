# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:29:29 2024

@author: Student
"""
import math
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập n: "))
    
if math.sqrt(n) == int(math.sqrt(n)):
    print("là số chính phương")
else:
    print("không là số chính phương")
        