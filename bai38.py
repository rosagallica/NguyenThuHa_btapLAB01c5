# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:04:10 2024

@author: Student
"""

n = int(input("Nhập n: "))
while n <= 0 or n % 2 == 0:
    n = int(input("Nhập n: "))
tích = 1
for i in range(1, n+1):
    tích *= i
print(tích)
    