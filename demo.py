#import pandas as pd# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
from sklearn.tree import DecisionTreeRegressor
st.write('machine learning')
st.write('HELLO')
import pandas as pd
df=pd.read_csv('YIELD1.csv')
st.line_chart(df['PH'])
x=df.iloc[:,[0,5]]
y=df.iloc[:,[1,2,3]]
model=DecisionTreeRegressor()
model.fit(x,y)
def user_input_features():
    AGE=(st.number_input('Enter age of tea area'))
    YIELD=st.number_input('Yield expected',min_value=0,max_value=5000)
    data={'AGE':[AGE],'YIELD':[YIELD]}
    features=pd.DataFrame(data)
    return features
df1=user_input_features()
df=pd.read_csv('YIELD1.csv')
st.line_chart(df['PH'])
x=df.iloc[:,[0,5]]
y=df.iloc[:,[1,2,3]]
model=DecisionTreeRegressor()
model.fit(x,y)
prediction=model.predict(df1)
st.write(prediction)

