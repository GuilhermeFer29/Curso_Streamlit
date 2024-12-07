import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title = 'spotify songs'
)

df = pd.read_csv('01 Spotify.csv')

df.set_index("Track", inplace=True)

st.bar_chart(df[df["Stream"] > 1000000000]["Stream"])