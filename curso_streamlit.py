import streamlit as st
import pandas as pd

# Configuração Pagina
st.set_page_config(
    layout='wide',
    page_title = 'spotify songs'
)

# Leitura dos dados em  CSV 
df = pd.read_csv('01 Spotify.csv')


# Chamar dados dos Albuns
df.set_index("Track", inplace=True)

#Select Box seleção de artista
artists = df['Artist'].value_counts().index
option = st.selectbox('Artista',artists )
df_filtered = df[df['Artist'] == option ]


#seleção de albuns

album = df_filtered['Album'].value_counts().index
artist  = st.selectbox('Album', album)
df_filtered2 = df[df['Album'] == artist]

#side bar ocultar/mostrar Dados

artist_data = st.checkbox("Dados Artista")
if artist_data:
    st.bar_chart(df_filtered2["Stream"])