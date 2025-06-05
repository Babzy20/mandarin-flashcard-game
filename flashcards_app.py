import streamlit as st
import pandas as pd

# Custom CSS for flashcard styling
st.markdown("""
    <style>
    .flashcard {
        border: 2px solid #f0f0f0;
        border-radius: 10px;
        padding: 20px;
        margin: 20px;
        text-align: center;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .flashcard p {
        font-size: 24px;
        margin: 10px 0;
    }
    .flashcard p.pinyin {
        font-size: 18px;
        color: #888888;
    }
    </style>
""", unsafe_allow_html=True)

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

        st.markdown(f"""
            <div class="flashcard">
                <p>{current_word['mandarin']}</p>
                <p class="pinyin">{current_word['pinyin']}</p>
            </div>
        """, unsafe_allow_html=True)

        if st.button("Afficher la traduction"):
            st.session_state.show_translation = True

        if st.session_state.show_translation:
            st.markdown(f"""
                <div class="flashcard">
                    <p>{current_word['french']}</p>
                </div>
            """, unsafe_allow_html=True)

        if st.button("Mot suivant"):
            st.session_state.index += 1
            st.session_state.show_translation = False

            if st.session_state.index >= len(df):
                st.session_state.index = 0
    else:
        st.write("Le fichier CSV doit contenir les colonnes 'mandarin', 'pinyin' et 'french'.")
