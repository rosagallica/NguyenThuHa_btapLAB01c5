# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:37:20 2024

@author: ADMIN
"""

n = int(input("Nhập n: "))

while n <= 0:
    n = int(input("Nhập n: "))
    
uoc_so = []
for i in range(1, n+1):
    if n % i == 0:
        uoc_so.append(i)
print(uoc_so)