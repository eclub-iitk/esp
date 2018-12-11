#By Ashok Kumar Chaudhary

""" This Code is fow viewing the data"""

import pandas as pd

import numpy as np

from numpy import matrix

import xlwt

import matplotlib.pyplot as plt

i=1501
nof=1550 #no of files

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

while(i<=nof):
    #reading from each raw data
    mydata=pd.read_excel('d%d.xls'%i)
    mydata1=mydata.iloc[:,:2]

    #mydata1=mydata1.rolling(20).mean() #moving average

    mydata1.as_matrix()  #converting the dataframe to Matrix

    #breaking the matrix into column vectors {IMU}
    col1=matrix(mydata1).transpose()[0].getA()[0]
    col2=matrix(mydata1).transpose()[1].getA()[0]

    print (i)
    i=i+1

    plt.plot(col1)
    plt.plot(col2)

    plt.show()
