import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

df = pd.read_csv("data.csv")
forest = open('power.pkl','rb')
model = pickle.load(forest)
st.title(':orange[POWER OUTPUT PREDICTION APP]')
#view = ['STANDARD PARAMETERS','PREDICTION PARAMETERS']
select = st.radio('Select Parameters:',['STANDARD PARAMETERS','PREDICTION PARAMETERS'],horizontal=True)
if select == 'STANDARD PARAMETERS':
    col1,col2,col3=st.columns(3)
    with col1:
        st.subheader(':violet[TEMP]')
        a=df['Temp'].unique()
        a.sort()
        Temp = st.selectbox('Select Temperature',a)
        #st.text(" ")
        st.subheader(':violet[VACUUM]')
        b=df['Vacuum'].unique()
        b.sort()
        Vacuum = st.selectbox('Select Vacuum',b)
        #st.text(" ")
        st.subheader(':violet[PRESSURE]')
        c=df['Pressure'].unique()
        c.sort()
        Pressure = st.selectbox('Select Pressure',c)
    with col2:
        st.subheader(':violet[HUMIDITY]')
        a=df['Humidity'].unique()
        a.sort()
        Humidity = st.selectbox('Select Humidity',a)
        st.subheader(':violet[Temp-Diff ]')
        b=df['TempDiff'].unique()
        b.sort()
        TempDiff = st.selectbox('Select Temperature Difference',b)
        #st.text(" ")
        st.subheader(':violet[PRESSURE-DIFF]')
        c=df['PressureDiff'].unique()
        c.sort()
        PressureDiff = st.selectbox('Select Pressure Difference',c)
        #st.text(" ")
    with col3:
        st.subheader(':violet[POWER-PER-FUEL]')
        a=df['PowerPerFuel'].unique()
        a.sort()
        PowerPerFuel = st.selectbox('Select Power Per Fuel',a)
        st.text(" ")
        st.text(" ")
    submit=st.button('SUBMIT')
    if submit:
        y = np.array([[Temp, Vacuum, Pressure, Humidity, TempDiff,PressureDiff,PowerPerFuel]])
        new = model.predict(y)
        st.write("### :green[ELECTRICAL POWER OUTPUT IS]",round(new[0],2),":green[KWH]")
else:
    col1, col2,col3 = st.columns(3)
    with col1:
        st.subheader(':violet[TEMP]')
        Temp = st.text_input('Enter Temperature')
        if Temp:
            Temp=float(Temp)
        #st.text(" ")
        st.subheader(':violet[VACUUM]')
        Vacuum = st.text_input('Enter Vacuum')
        if Vacuum:
            Vacuum=float(Vacuum)
        #st.text(" ")
        st.subheader(':violet[PRESSURE]')
        Pressure = st.text_input('Enter Pressure')
        if Pressure:
            Pressure=float(Pressure)
    with col2:
        st.subheader(':violet[HUMIDITY]')
        Humidity = st.text_input('Enter Humidity')
        if Humidity:
            Humidity=float(Humidity)

        st.subheader(':violet[TEMP-DIFF]')
        TempDiff = st.text_input('Enter Temperature Difference')
        if TempDiff:
            TempDiff=float(TempDiff)
        #st.text(" ")
        st.subheader(':violet[PRESSURE-DIFF]')
        PressureDiff = st.text_input('Enter Pressure Difference')
        if PressureDiff:
            PressureDiff=float(PressureDiff)
    with col3:
        st.subheader(':violet[POWER-PER-FUEL]')
        PowerPerFuel = st.text_input('Enter Power Per Fuel')
        if PowerPerFuel:
            PowerPerFuel=float(PowerPerFuel)
        st.text(" ")
        st.text(" ")
        st.text(' ')
    submit = st.button('SUBMIT')
    if submit:
        y = np.array([[Temp, Vacuum, Pressure, Humidity, TempDiff, PressureDiff, PowerPerFuel]])
        new = model.predict(y)
        st.write("### :green[ELECTRICAL POWER OUTPUT IS]", round(new[0],2),":green[KWH]")

st.write( f'<h5 style="color:rgb(0, 153, 153,0.35);">App Created by RAVI CHANDRA PALEM </h5>', unsafe_allow_html=True )

