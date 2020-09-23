#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 00:30:21 2020
@author: xuehuzhou
"""


import pandas as pd
import numpy as np
import sys

allStudentFile = "无锡分校-东南-第十二期.xlsx"
studentName = "students.xlsx"
#allStudentFile = sys.argv[1] +".xlsx"
#studentName = sys.argv[1]+".xlsx"
allStudentFileDf = pd.read_excel(allStudentFile)
studentNameDf = pd.read_excel(studentName)
print(sys.argv[1]+"大学习，网安参与情况如下：")
allClass = allStudentFileDf["姓名"].str.replace(r"[0-9]*","").replace("-","")
allClass = set(allClass.dropna())
classOne = set(studentNameDf["一班"].dropna())
a1 = len(classOne)
a2 = len(classOne.intersection(allClass))
a3 = a2/a1
print('网安一班共%d名同学，其中%d名同学参与学习，参与率为：%.2f'%(a1,a2,a3))
classTwo = set(studentNameDf["二班"].dropna())
b1 = len(classTwo)
b2 = len(classTwo.intersection(allClass))
b3 = b2/b1
print('网安二班共%d名同学，其中%d名同学参与学习，参与率为：%.2f'%(b1,b2,b3))

classThree = set(studentNameDf["三班"].dropna())
c1 = len(classThree)
c2 = len(classThree.intersection(allClass))
c3 = c2/c1
print('网安三班共%d名同学，其中%d名同学参与学习，参与率为：%.2f'%(c1,c2,c3))

classFour = set(studentNameDf["四班"].dropna())
d1 = len(classFour)
d2 = len(classFour.intersection(allClass))
d3 = d2/d1
print('网安四班共%d名同学，其中%d名同学参与学习，参与率为：%.2f'%(d1,d2,d3))

classFive = set(studentNameDf["五班"].dropna())
e1 = len(classFive)
e2 = len(classFive.intersection(allClass))
e3 = e2/e1
print('网安五班共%d名同学，其中%d名同学参与学习，参与率为：%.2f'%(e1,e2,e3))


