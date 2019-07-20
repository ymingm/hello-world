# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:57:44 2019

@author: Administrator
"""
import os
os.chdir(r'C:\Users\Administrator\Desktop\李宏毅机器学习\作业\7.20')

#Q1

import numpy as np

matrixA = []
for i in open("matrixA.txt"):
    row = [int(x) for x in i.split(",")]
    matrixA.append(row)

matrixB = []
for j in open("matrixB.txt"):
    row = [int(x) for x in j.split(",")]
    matrixB.append(row)

matrixA = np.array(matrixA)
matrixB = np.array(matrixB)

ans = matrixA.dot(matrixB)
ans.sort(axis=1)

np.savetxt(r"C:\Users\Administrator\Desktop\李宏毅机器学习\作业\7.20\Q1_ans.txt", ans, fmt="%d", delimiter="\r\n")

#Q2
from PIL import Image

lena = Image.open("lena.png")
lena_modified = Image.open("lena_modified.png")

w, h = lena.size
for j in range(h):
    for i in range(w):
        if lena.getpixel((i, j)) == lena_modified.getpixel((i, j)):
            lena_modified.putpixel((i, j), 255)

lena_modified.save("ans_two.png")
lena_modified.show()


