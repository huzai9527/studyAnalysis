#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:06:08 2020

@author: xuehuzhou
"""



import pandas as pd
import numpy as np
import sys

#allStudentFile = "无锡分校-东南-第十二期.xlsx"
studentName = "无锡分校总名单.xlsx"
allStudentFile = sys.argv[1] +".xlsx"
allStudentFileDf = pd.read_excel(allStudentFile)
studentNameDf = pd.read_excel(studentName)
print(sys.argv[1]+"大学习，无锡分校各班级参与情况如下：")

allClass = allStudentFileDf["姓名"].str.replace(r"[0-9]*","")
allClass = allClass.str.replace("-","")
allClass = allClass.str.replace(" ","")
allClass = allClass.str.replace("+","")
allClass = set(allClass.dropna())

className = list(studentNameDf.columns)
moreInfo = pd.DataFrame(index=className,columns=['总人数','参与人数','参与率','未参加人员'])
allCount = []
attendCount = []
percentCount = []
for i in range(0,len(className)):
    nowClassName = str(className[i])
    nowClass = set(studentNameDf[nowClassName].dropna())
    a1 = len(nowClass)
    allCount.append(a1)
    a2 = len(nowClass.intersection(allClass))
    attendCount.append(a2)
    a3 = a2/a1
    percentCount.append(a3)
    print('%s共%d名同学，其中%d名同学参与学习，参与率为：%.2f'%(nowClassName,a1,a2,a3))
moreInfo['总人数'] = allCount
moreInfo['参与人数'] = attendCount
moreInfo['参与率'] = percentCount
moreInfo.to_excel(sys.argv[1]+"大学习，无锡分校各班级参与情况.xlsx")
print("EXCELL文件保存成功")




