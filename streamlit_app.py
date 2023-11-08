import streamlit as st
import pandas as pd
import numpy as np 
import pickle
from sklearn.linear_model import logisticRegression
from sklearn.model_selection import train_test_split

st.header('Bem vindo ao portal!')
st.subheader('''
             A página está dividida assim:
                1. PowerBI
                2. Relatórios
             ''')

options = st.selectbox('Selecione',['Power BI', 'Relatórios'])
