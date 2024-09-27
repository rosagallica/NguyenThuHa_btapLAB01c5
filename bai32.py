# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:02:51 2024

@author: ADMIN
"""

qd = float(input("Nhập quãng đường :"))
if qd == 1:
    tien = 15
elif 1 < qd <= 5:
    tien = 15 + (qd-1)*13.5
elif qd >= 6:
    tien = 15 + (4*13.5) + (qd-5)*11
elif qd > 120:
    tien = (15 + (4*13.5) + ((qd-5)*11))*0.9
print (tien)