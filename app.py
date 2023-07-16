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
        Temp = st.selectbox('Select Temperature',df['Temp'].unique().sort())
        #st.text(" ")
        st.subheader(':violet[VACUUM]')
        Vacuum = st.selectbox('Select Vacuum',df['Vacuum'].unique())
        #st.text(" ")
        st.subheader(':violet[PRESSURE]')
        Pressure = st.selectbox('Select Pressure',df['Pressure'].unique())
    with col2:
        st.subheader(':violet[HUMIDITY]')
        Humidity = st.selectbox('Select Humidity',df['Humidity'].unique())
        st.subheader(':violet[Temp-Diff ]')
        TempDiff = st.selectbox('Select Temperature Difference',df['TempDiff'].unique())
        #st.text(" ")
        st.subheader(':violet[PRESSURE-DIFF]')
        PressureDiff = st.selectbox('Select Pressure Difference',df['PressureDiff'].unique())
        #st.text(" ")
    with col3:
        st.subheader(':violet[POWER-PER-FUEL]')
        PowerPerFuel = st.selectbox('Select Power Per Fuel',df['PowerPerFuel'].unique())
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

