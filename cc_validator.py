#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:57:40 2022

@author: ashutosh
"""


cc_number=input()

cc_new=cc_number.replace(cc_number[-1],'')
rev_cc=cc_new[::-1]
print(cc_new)
print(rev_cc)

total=0
t_9=0

for i in range(len(rev_cc)):
    if i%2==0:
        twice=int(cc_number[i])*2
        if twice>9:
            t_9=twice-9
            
            total+=t_9
            
        elif twice<9:
            total+=twice
    elif i%2!=0:
        total+=int(cc_number[i])
            
print(total)
last_digit=int(cc_number[-1])
print(last_digit)
final=total+last_digit
print(final)

if final%10==0:
    print("Credit card nuber is valid")
else:
    print("Please enter valid credit card")
