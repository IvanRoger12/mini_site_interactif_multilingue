import streamlit as st
import json
import random
import time

st.set_page_config(page_title="Jeux Magiques", layout="wide")

# Musique de fond magique
st.markdown("""
<audio controls autoplay loop style="width: 100%;">
  <source src="https://www.bensound.com/bensound-music/bensound-slowmotion.mp3" type="audio/mp3">
  Votre navigateur ne supporte pas l’audio.
</audio>
""", unsafe_allow_html=True)

# Langues disponibles
langue = st.sidebar.selectbox("🌐 Langue / Language", ["Français", "English", "Español", "中文", "Italiano"])
lang_index = ["Français", "English", "Español", "中文", "Italiano"].index(langue)

# Dictionnaire de traduction
T = lambda d: d[lang_index]
trads = {
    "title": ("Jeux & Histoires Magiques", "Magic Games & Stories", "Juegos y Cuentos Mágicos", "魔法游戏和故事", "Giochi e Storie Magiche"),
    "welcome": ("Bienvenue !", "Welcome!", "¡Bienvenido!", "欢迎！", "Benvenuto!"),
    "math_game": ("Calcul Mental", "Mental Math", "Cálculo Mental", "心算游戏", "Calcolo Mentale"),
    "story_game": ("Histoires Magiques", "Magic Stories", "Cuentos Mágicos", "魔法故事", "Storie Magiche"),
    "mode": ("Choisis un mode :", "Choose a mode:", "Elige un modo:", "选择模式：", "Scegli una modalità:"),
    "choose_story": ("Choisis une histoire :", "Choose a story:", "Elige una historia:", "选择一个故事：", "Scegli una storia:"),
    "random_story": ("Histoire aléatoire", "Random Story", "Historia aleatoria", "随机故事", "Storia casuale"),
    "start": ("Commencer", "Start", "Comenzar", "开始", "Inizia"),
    "ads": ("🎁 Découvrez notre univers magique sur [notre boutique](https://example.com)",
            "🎁 Discover our magical world at [our shop](https://example.com)",
            "🎁 Descubre nuestro mundo mágico en [nuestra tienda](https://example.com)",
            "🎁 在[我们的商店](https://example.com)探索我们的魔法世界",
            "🎁 Scopri il nostro mondo magico su [il nostro shop](https://example.com)")
}

# Prénom de l'enfant
name = st.sidebar.text_input("🎈 Entre ton prénom :", placeholder="Prénom")
if name:
    st.sidebar.success(f"Bienvenue {name} !")

# Titre
st.title("🎮 " + T(trads["title"]))
st.markdown("### " + T(trads["welcome"]))

# Choix du mode
mode = st.radio(T(trads["mode"]), [T(trads["math_game"]), T(trads["story_game"])])

# Machine à écrire
def typewriter(text, delay=0.02):
    container = st.empty()
    txt = ""
    for c in text:
        txt += c
        container.markdown(f"### {txt}")
        time.sleep(delay)

# Mode Calcul Mental
if mode == T(trads["math_game"]):
    score = 0
    for i in range(5):
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-", "*"])
        correct = eval(f"{a}{op}{b}")
        rep = st.number_input(f"{a} {op} {b} = ?", key=f"q{i}")
        if st.button(f"{T(trads['start'])} {i+1}", key=f"b{i}"):
            if rep == correct:
                st.success("✅ Correct !")
                score += 1
            else:
                st.error(f"❌ Mauvaise réponse. C'était {correct}")
    st.info(f"🏁 Score : {score}/5")

# Mode Histoire Magique
else:
    with open("histoires_enfants.json", "r", encoding="utf-8") as f:
        histoires = json.load(f)

    choix_mode = st.radio("🎬", [T(trads["choose_story"]), T(trads["random_story"])])
    if choix_mode == T(trads["choose_story"]):
        titres = [h["titre"] for h in histoires]
        selected = st.selectbox(T(trads["choose_story"]), titres)
        histoire = next(h for h in histoires if h["titre"] == selected)
    else:
        histoire = random.choice(histoires)
        st.success(f"{T(trads['random_story'])} : {histoire['titre']}")

    st.header("📖 " + histoire["titre"])
    if st.button(T(trads["start"])):
        typewriter(histoire["intro"], delay=0.02)

    col1, col2 = st.columns(2)
    if col1.button(histoire["choix"][0]):
        st.success(histoire["resultats"][0])
    if col2.button(histoire["choix"][1]):
        st.info(histoire["resultats"][1])

# Publicité
st.markdown("---")
st.markdown(T(trads["ads"]))
