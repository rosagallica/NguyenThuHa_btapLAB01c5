# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:16:49 2024

@author: Student
"""

n = int(input("Nhập n: "))
while n <= 0 or n % 2 != 0:
    n = int(input("Nhập n: "))
tong = 0
for i in range(2, n+1, 2):
    tong += i
print(tong)