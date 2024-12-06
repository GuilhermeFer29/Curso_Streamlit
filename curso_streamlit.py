import streamlit as st
import pandas as pd

df = pd.read_csv('artists.csv')
st.write(df[df["Streams"] > '10000000000'])