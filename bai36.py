# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:20:17 2024

@author: Student
"""

n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập n: "))
tong = 0
for i in range(1, n+1):
    tong += i**2
print(tong)