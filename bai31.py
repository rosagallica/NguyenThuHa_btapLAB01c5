# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:18:56 2024

@author: ADMIN
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print ("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("3 số không tạo thành tam giác")
    
        