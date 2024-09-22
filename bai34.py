# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:26:40 2024

@author: Student
"""

n = int(input("Nhập n: "))

while n <= 0:
    n = int(input("Nhập n: "))
    
if n<2:
    print("khong phai là so nguyen to")
else:
    for i in range(2, n+1):
        if n%i == 0:
            print("khong phai là so nguyen to")
            break
        else:
            print(" là so nguyen to")
            break