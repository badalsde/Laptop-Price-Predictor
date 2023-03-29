import streamlit as st
import pickle
import numpy as np

#import the model
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('Laptop Price Predictor')
#brand
company = st.selectbox('Brand', df['Company'].unique())

#type of laptop
type = st.selectbox('Type', df['TypeName'].unique())

#Ram
ram = st.selectbox('Ram(in GB)', [2, 4, 6, 8, 12, 16, 32, 64])

#Weight
weight = st.number_input('Weight of Laptop')

#Touch Screen
touchscreen = st.selectbox('Touch Screen', ['No', 'Yes'])

#IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

#screen size
screen_size = st.number_input('Screen Size')

#Resolution
resolution = st.selectbox('Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1440', '2304x1440'])

#CPU
cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())

#HDD
hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

#SSD
ssd = st.selectbox('SSD(in GB)', [0, 128, 256, 512, 1024])

#GPU Brand
gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())

#OS
os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os], dtype=object)

    query = query.reshape(1, 12)
    st.title(np.round(np.exp(pipe.predict(query)), 2))

