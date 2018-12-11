#By Suraj Hanchinal
""" This Code is fow viewing the data"""

import pandas as pd

import numpy as np

from numpy import matrix

import xlwt

import matplotlib.pyplot as plt

i=1
nof=1 #no of files

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

while(i<=nof):
    #reading from each raw data
    mydata=pd.read_excel('d%d.xls'%i)
    mydata1=mydata.iloc[:,:2]
    mydata1 = mydata1.values
    #print(mydata1)
    col1 = mydata1[:,0]
    col2 = mydata1[:,1]
    print (i)
    i=i+1

    plt.plot(col1)
    plt.plot(col2)

    plt.show()
