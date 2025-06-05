
import streamlit as st
import pandas as pd

st.title("Apprendre le Mandarin avec des Flashcards")
st.write("Téléchargez un fichier CSV contenant des mots en Mandarin, Pinyin et Français.")

uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'mandarin' in df.columns and 'pinyin' in df.columns and 'french' in df.columns:
        if 'index' not in st.session_state:
            st.session_state.index = 0
        if 'show_translation' not in st.session_state:
            st.session_state.show_translation = False

        current_word = df.iloc[st.session_state.index]

        st.write(f"**Mandarin:** {current_word['mandarin']}")
        st.write(f"**Pinyin:** {current_word['pinyin']}")

        if st.button("Afficher la traduction"):
            st.session_state.show_translation = True

        if st.session_state.show_translation:
            st.write(f"**Français:** {current_word['french']}")

        if st.button("Mot suivant"):
            st.session_state.index += 1
            st.session_state.show_translation = False

            if st.session_state.index >= len(df):
                st.session_state.index = 0
    else:
        st.write("Le fichier CSV doit contenir les colonnes 'mandarin', 'pinyin' et 'french'.")
