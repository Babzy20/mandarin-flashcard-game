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

# Shuffle once per session
if 'shuffled_indices' not in st.session_state:
    st.session_state.shuffled_indices = random.sample(range(len(df)), len(df))
    st.session_state.current = 0
    st.session_state.reveal = False
    st.session_state.review_later = []

# Get current word
idx = st.session_state.shuffled_indices[st.session_state.current]
word = df.iloc[idx]

# Page layout
st.set_page_config(page_title="Mandarin Flashcards", layout="centered")
st.title("📖 Mandarin Flashcards")

# Flashcard display
st.markdown("""
    <style>
    .card {
        border: 2px solid #ddd;
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        background-color: #fff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 30px auto;
        width: 80%;
    }
    .card p {
        font-size: 32px;
        margin: 10px 0;
    }
    .card .pinyin {
        font-size: 20px;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="card">
        <p>{word['Graphie']}</p>
        <p class="pinyin">{word['Pinyin']}</p>
        {"<p><strong>" + word['Signification'] + "</strong></p>" if st.session_state.reveal else ""}
    </div>
""", unsafe_allow_html=True)

# Buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("🔁 Revoir plus tard"):
        st.session_state.review_later.append(idx)
        st.session_state.current += 1
        st.session_state.reveal = False
with col2:
    if st.button("👁️ Afficher la traduction"):
        st.session_state.reveal = True
with col3:
    if st.button("➡️ Suivant"):
        st.session_state.current += 1
        st.session_state.reveal = False
