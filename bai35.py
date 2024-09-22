# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:23:37 2024

@author: Student
"""

n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập n: "))
tong = 0
for i in range(1, n+1):
    tong += i
print(tong)