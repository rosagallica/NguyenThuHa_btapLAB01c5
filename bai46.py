# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 2*x + 7*1 + 9*1 = 979 => x = (979 - (7+9))/2 = 488.5 (490)
# 2*1 + 7*y + 9*1 = 979 => y = (979 - (2+9))/2 = 138.5 (140)
# 2*1 + 7*1 + 9*z = 979 => z = (979 - (7+2))/2 = 108 (109)

bo_nghiem = []
for x in range(1, 490):
    for y in range(1, 140):
        for z in range(1, 109):
            if 2*x + 7*y + 9*z == 979:
                bo_nghiem += [(x, y, z)]
if bo_nghiem:
    print(f' {bo_nghiem}')    

