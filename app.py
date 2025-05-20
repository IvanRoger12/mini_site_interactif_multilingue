# MINI SITE INTERACTIF V2 – STRUCTURE DE BASE
# ⚙️ Contenu : multilingue, calcul mental, histoire, pub, sécurité, base utilisateur (structure à compléter)

import streamlit as st
import random
import time
from datetime import datetime

# --- Authentification simple (mot de passe client) ---
PASSWORD = "accesvip"
if st.sidebar.text_input("Mot de passe", type="password") != PASSWORD:
    st.warning("🔐 Accès réservé. Veuillez entrer le mot de passe.")
    st.stop()

# --- Multilingue ---
langue = st.sidebar.selectbox("🌐 Langue", ["Français", "English", "Español", "中文", "Italiano"])
traductions = {
    "welcome": ("Bienvenue !", "Welcome!", "¡Bienvenido!", "欢迎！", "Benvenuto!"),
    "math_game": ("Calcul mental", "Mental math", "Cálculo mental", "心算", "Calcolo mentale"),
    "story_game": ("Aventure interactive", "Interactive adventure", "Aventura interactiva", "互动冒险", "Avventura interattiva"),
    "ads": ("Découvrez nos partenaires IA", "Discover our AI partners", "Descubre nuestros socios IA", "探索我们的AI合作伙伴", "Scopri i nostri partner IA")
}
def t(key):
    idx = {"Français": 0, "English": 1, "Español": 2, "中文": 3, "Italiano": 4}
    return traductions[key][idx[langue]]

# --- Interface principale ---
st.set_page_config(page_title="Site IA V2", layout="wide")
st.title("🎮 " + t("welcome"))

# Menu de navigation
menu = st.sidebar.radio("Menu", [t("math_game"), t("story_game"), "💡 À propos"])

# --- Jeux mathématiques ---
if menu == t("math_game"):
    st.header("🧠 " + t("math_game"))
    score = 0
    for i in range(5):
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-", "*"])
        correct = eval(f"{a}{op}{b}")
        ans = st.number_input(f"{a} {op} {b} = ?", key=f"q{i}")
        if st.button(f"Valider {i+1}", key=f"b{i}"):
            if ans == correct:
                st.success("✔️ Correct")
                score += 1
            else:
                st.error(f"❌ Faux. Réponse : {correct}")
    st.info(f"Score final : {score}/5")

# --- Histoire interactive simplifiée ---
elif menu == t("story_game"):
    st.header("📖 " + t("story_game"))
    st.markdown("Vous êtes dans une forêt magique. Deux chemins : gauche 🌲 ou droite 🔥 ?")
    if st.button("Aller à gauche"):
        st.success("Vous trouvez un coffre magique !")
    if st.button("Aller à droite"):
        st.error("Un dragon apparaît... mais vous vous échappez de justesse.")

# --- Publicité et info ---
else:
    st.header("🔗 " + t("ads"))
    st.markdown("👉 Visitez [notre site partenaire](https://example.com) pour plus de contenu.")
    st.markdown("© 2025 | Propulsé par Streamlit")
