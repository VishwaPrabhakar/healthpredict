#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:33:18 2019

@author: vishwaprabhakarsingh
"""
import numpy as np
import pandas as pd
df =pd.read_csv('/Users/vishwaprabhakarsingh/Desktop/weekend_dsp_noon/Health_model_predictive_/newdata.csv')
print(df.head())

x=df[['Height','Weight','Bmi']]
y=df[['Marks']]
from sklearn.linear_model import LinearRegression
lr=LinearRegression()

lr.fit(x,y)
#d={
#        'Height':128,
#        'Weight':88,
#        'Bmi':1.103440,}
#tmpdf=pd.DataFrame(data=d)

#tmp=[128,88,1.103440]
#tmp=np.array(tmp)
#tmp=tmp.reshape(-3,3)
#print(lr.predict(tmp))

import sys
import tkinter
from tkinter import messagebox 
from tkinter import *
window=Tk()
window.title("Health Predictor")
window.geometry("440x330")
L1=Label(window,text="Health Checking Software",font=('Arial',20))
L1.grid(column=0,row=0)
L1=Label(window,text="Enter your name::")
L1.grid(column=0,row=1)
e1=Entry(window,width=10)
e1.grid(column=1,row=1)

L2=Label(window,text="Enter your Height::")
L2.grid(column=0,row=2)
e2=Entry(window,width=10)
e2.grid(column=1,row=2)

L3=Label(window,text="Enter your Weight::")
L3.grid(column=0,row=3)
e3=Entry(window,width=10)
e3.grid(column=1,row=3)


def calcbmi():
    h=int(e2.get())
    w=int(e3.get())
    bmi=w/(h*h)
    tmp=[h,w,bmi]
    tmp=np.array(tmp)
    tmp=tmp.reshape(-3,3)
    prediction_mark=lr.predict(tmp)
    
    show="your health is "+str(bmi)
    print(show)
    ##
    if ( prediction_mark < 1):
        show="severely underweight your bmi is"+str(bmi)+"and mark is "+str(prediction_mark)
        messagebox.showinfo("your Health REsult",show)

    elif ( bmi >= 1 or bmi < 2):
        show="underweight your bmi is"+str(bmi)+"and mark is "+str(prediction_mark)
        messagebox.showinfo("your Health REsult",show)
        
    
    elif ( bmi >= 2 or bmi < 3):
        show="Healthy, your bmi is"+str(bmi)+"and mark is "+str(prediction_mark)
        messagebox.showinfo("your Health REsult",show)
    
    elif ( bmi >= 3 or bmi < 4):
        show="overweight, your bmi is"+str(bmi)+"and mark is "+str(prediction_mark)
        messagebox.showinfo("your Health REsult",show)
        
    
    elif ( bmi >=4):
        show="severely overweight, your bmi is"+str(bmi)+"and mark is "+str(prediction_mark)
        messagebox.showinfo("your Health REsult",show)
    else:
        messagebox.showinfo("Alert","Unkown error: contact vishwa")

B1=Button(window,text="Calculate",command=calcbmi)
B1.grid(column=0,row=5)

#B2=Button(window,text="Exit Software",command=window.destroy)
#B2.grid(column=1,row=5)
window.config(bg='blue')
window.mainloop()


