#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:06:08 2020

@author: xuehuzhou
"""

import pandas as pd
import sys

#allStudentFile = "无锡分校-东南-第十二期.xlsx"
studentName = "本院总名单.xlsx"
allStudentFile = sys.argv[1] +".xlsx"

allStudentFileDf = pd.read_excel(allStudentFile)
studentNameDf = pd.read_excel(studentName)

print(sys.argv[1]+"大学习各班级参与情况如下：")

allClass = allStudentFileDf["姓名"].str.replace(r"[0-9]*","")
allClass = allClass.str.replace("-","")
allClass = allClass.str.replace(" ","")
allClass = allClass.str.replace("+","")
allClass = set(allClass.dropna())
className = list(studentNameDf.columns)
moreInfo = pd.DataFrame(index=className,columns=['总人数','参与人数','参与率','排名','是否合格','本期分数','累计分数','未参加人员'])
all_score = pd.read_excel("班级累计分数.xlsx",index_col=0)
allCount = []
attendCount = []
percentCount = []
impresent = []
ispass = []
now_score = []
percentCount1 = []
for i in range(0,len(className)):
    nowClassName = str(className[i])
    nowClass = set(studentNameDf[nowClassName].dropna())
    a1 = len(nowClass)
    allCount.append(a1)
    a2 = len(nowClass.intersection(allClass))
    attendCount.append(a2)
    a3 = a2/a1
    percentCount.append(round(a3,4))
    percentCount1.append(str(round(a3,2)*100)+"%")
    a4 = list(nowClass.difference(nowClass.intersection(allClass)))
    impresent.append(a4)
    a5 = 0 if a3<0.7 else 4 if a3>=0.7 and a3 <0.8 else 6 if a3 >=0.8 and a3<0.9 else 8 
    now_score.append(a5)
    ispass.append("是") if a5>0 else ispass.append("否")
    print('%s共%d名同学，其中%d名同学参与学习，参与率为：%.2f'%(nowClassName,a1,a2,a3))
moreInfo['总人数'] = allCount
moreInfo['参与人数'] = attendCount
moreInfo['参与率'] = percentCount
moreInfo['是否合格'] = ispass
moreInfo['本期分数'] = now_score
moreInfo['累计分数'] = (all_score + pd.DataFrame(now_score,columns=['累计分数'],index=className))['累计分数']
all_score['累计分数'] += now_score
moreInfo['未参加人员'] = impresent
moreInfo.sort_values("参与率",inplace=True,ascending=False)
moreInfo['排名'] = moreInfo['参与率'].rank(method='first',ascending=False)
moreInfo['参与率'] = moreInfo['参与率'].apply(lambda x: format(x, '.2%'))
moreInfo.to_excel("结果/"+sys.argv[1]+"大学习各班级参与情况.xlsx")
all_score.to_excel("班级累计分数.xlsx")
print("EXCELL文件保存成功")




