# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:21:08 2024

@author: Student
"""
s = 0
ts = 0
ms = 0
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập n: "))
x = float(input("Nhập x: "))
for i in range(1, n+1):
    ts = x**i
    ms = ms + i
    s += ts/ms
print(round(s, 2))