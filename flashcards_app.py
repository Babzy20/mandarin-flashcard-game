import streamlit as st
import pandas as pd
import random

# Vocabulary list
data = {
    "Graphie": ["爸爸", "妈妈", "爷爷", "奶奶", "哥哥", "弟弟", "姐姐", "妹妹", "家", "有", "没", "几个 ……?", "几口人?", "兄弟姐妹", "爱", "孩子", "父母"],
    "Pinyin": ["bàba", "māma", "yéye", "nǎinai", "gēge", "dìdi", "jiějie", "mèimei", "jiā", "yǒu", "méi", "jǐ gè …… ?", "jǐ kǒu rén?", "Xiōngdì-jiěmèi", "ài", "háizi", "fùmǔ"],
    "Signification": ["papa", "maman", "grand-père paternel", "grand-mère maternelle", "grand frère", "petit frère", "grande soeur", "petite soeur", "famille, maison", "avoir", "ne pas … (négation avec le verbe avoir)", "combien de ? (quantité d’individus, choses) 1 à 9", "combien de personnes dans ta famille? (quantité membres de la famille)", "frères et soeurs", "aimer = sentiment amoureux", "enfant", "parents"]
}
df = pd.DataFrame(data)

# App title
st.title("📚 Apprendre le Mandarin : Flashcards & Jeu d'association")

# Mode selection
mode = st.radio("Choisissez un mode :", ["Flashcards", "Jeu d'association"])

# Flashcard Mode
if mode == "Flashcards":
    if 'index' not in st.session_state:
        st.session_state.index = 0
    if 'show_translation' not in st.session_state:
        st.session_state.show_translation = False

    current_word = df.iloc[st.session_state.index]

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

    st.markdown(f"""
        <div class="flashcard">
            <p>{current_word['Graphie']}</p>
            <p class="pinyin">{current_word['Pinyin']}</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Afficher la traduction"):
        st.session_state.show_translation = True

    if st.session_state.show_translation:
        st.markdown(f"""
            <div class="flashcard">
                <p>{current_word['Signification']}</p>
            </div>
        """, unsafe_allow_html=True)

    if st.button("Mot suivant"):
        st.session_state.index += 1
        st.session_state.show_translation = False
        if st.session_state.index >= len(df):
            st.session_state.index = 0

# Matching Game Mode
else:
    st.subheader("🎯 Associez les mots chinois à leur signification")

    if 'shuffled_graphie' not in st.session_state or 'shuffled_signification' not in st.session_state:
        st.session_state.shuffled_graphie = random.sample(list(df["Graphie"]), len(df))
        st.session_state.shuffled_signification = random.sample(list(df["Signification"]), len(df))
        st.session_state.correct_pairs = df.set_index("Graphie")["Signification"].to_dict()

    col1, col2 = st.columns(2)

    with col1:
        graphie_choice = st.radio("Choisissez un mot chinois :", st.session_state.shuffled_graphie, key="graphie")

    with col2:
        signification_choice = st.radio("Choisissez une signification :", st.session_state.shuffled_signification, key="signification")

    if st.button("Vérifier la correspondance"):
        correct = st.session_state.correct_pairs.get(graphie_choice) == signification_choice
        if correct:
            st.success("✅ Bonne réponse !")
        else:
            st.error(f"❌ Mauvaise réponse. La bonne signification de '{graphie_choice}' est : {st.session_state.correct_pairs[graphie_choice]}")

    if st.button("🔄 Rejouer"):
        st.session_state.shuffled_graphie = random.sample(list(df["Graphie"]), len(df))
        st.session_state.shuffled_signification = random.sample(list(df["Signification"]), len(df))
