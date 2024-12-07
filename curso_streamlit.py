import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title = 'spotify songs'
)

df = pd.read_csv('01 Spotify.csv')

df.set_index("Track", inplace=True)

artists = df['Artist'].value_counts().index
option = st.selectbox('Artista',artists )

df_filter = df[df['Artist'] == option ]
st.bar_chart(df_filter["Stream"])