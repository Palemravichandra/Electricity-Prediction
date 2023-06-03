import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

df = pd.read_csv("data.csv")
forest = open('power.pkl','rb')
model = pickle.load(forest)
st.title(':orange[ELECTRICITY GENERATION PREDICTOR]')
view = ['STANDARD PARAMETERS','PREDICTION PARAMETERS']
select = st.selectbox('Select Parameters',view)
if select == 'STANDARD PARAMETERS':
    col1,col2=st.columns(2)
    with col1:
        st.subheader(':violet[TEMPERATURE]')
        Temp = st.selectbox('Select Temperature',df['Temp'].unique())
        #st.text(" ")
        st.subheader(':violet[VACUUM]')
        Vacuum = st.selectbox('Select Vacuum',df['Vacuum'].unique())
        #st.text(" ")
        st.subheader(':violet[PRESSURE]')
        Pressure = st.selectbox('Select Pressure',df['Pressure'].unique())
        st.subheader(':violet[HUMIDITY]')
        Humidity = st.selectbox('Select Humidity',df['Humidity'].unique())
    with col2:
        st.subheader(':violet[TEMPERATURE DIFFERENCE]')
        TempDiff = st.selectbox('Select Temperature Difference',df['TempDiff'].unique())
        #st.text(" ")
        st.subheader(':violet[PRESSURE DIFFERENCE]')
        PressureDiff = st.selectbox('Select Pressure Difference',df['PressureDiff'].unique())
        st.subheader(':violet[POWER PER FUEL]')
        PowerPerFuel = st.selectbox('Select Power Per Fuel',df['PowerPerFuel'].unique())
        st.text(" ")
        st.text(" ")
        submit=st.button('SUBMIT')
        if submit:
            y = np.array([[Temp, Vacuum, Pressure, Humidity, TempDiff,PressureDiff,PowerPerFuel]])
            new = model.predict(y)
            st.write("##:green[ELECTRICAL POWER OUTPUT IS]",round(new[0]))
else:
    col1, col2,col3= st.columns(3)
    with col1:
        st.subheader(':violet[TEMPERATURE]')
        Temp = st.text_input('Enter Temperature')
        if Temp:
            Temp=int(Temp)
        #st.text(" ")
        st.subheader(':violet[VACUUM]')
        Vacuum = st.text_input('Enter Vacuum')
        if Vacuum:
            Vacuum=int(Vacuum)
        #st.text(" ")
        st.subheader(':violet[PRESSURE]')
        Pressure = st.text_input('Enter Pressure')
        if Pressure:
            Pressure=int(Pressure)
    with col2:
        st.subheader(':violet[HUMIDITY]')
        Humidity = st.text_input('Enter Humidity')
        if Humidity:
            Humidity=int(Humidity)
        st.subheader(':violet[TEMPERATURE DIFFERENCE]')
        TempDiff = st.text_input('Enter Temperature Difference')
        if TempDiff:
            TempDiff=int(TempDiff)
        st.text(" ")
        st.subheader(':violet[PRESSURE DIFFERENCE]')
        PressureDiff = st.text_input('Enter Pressure Difference')
        if PressureDiff:
            PressureDiff=int(PressureDiff)
    with col3:
        st.subheader(':violet[POWER PER FUEL]')
        PowerPerFuel = st.text_input('Enter Power Per Fuel')
        if PowerPerFuel:
            PowerPerFuel=int(PowerPerFuel)
        st.text(" ")
        st.text(" ")
        submit = st.button('SUBMIT')
        if submit:
            y = np.array([[Temp, Vacuum, Pressure, Humidity, TempDiff, PressureDiff, PowerPerFuel]])
            new = model.predict(y)
            st.write("##:green[ELECTRICAL POWER OUTPUT IS]", round(new[0]))

st.write( f'<h5 style="color:rgb(0, 153, 153,0.35);">App Created by RAVI CHANDRA PALEM </h5>', unsafe_allow_html=True )
