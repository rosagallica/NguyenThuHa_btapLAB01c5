# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:34:34 2024

@author: ADMIN
"""

n = int(input("Nhập n: "))

tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print(tong)