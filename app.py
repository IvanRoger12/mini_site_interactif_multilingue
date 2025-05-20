
import streamlit as st
import random
from datetime import datetime

# --- Authentification simple ---
PASSWORD = "accesvip"

st.sidebar.title("🔐 Accès sécurisé")
user_password = st.sidebar.text_input("Mot de passe", type="password")
if user_password != PASSWORD:
    st.warning("🔒 Entrez le mot de passe pour accéder au contenu.")
    st.stop()

# --- Sélection de la langue ---
langue = st.sidebar.selectbox("🌐 Langue", ["Français", "English", "Español", "中文", "Italiano"])

# --- Dictionnaire de traduction ---
translations = {
    "title": ("Mini Site Interactif", "Interactive Mini Site", "Sitio Interactivo", "互动小游戏站点", "Mini Sito Interattivo"),
    "welcome": ("Bienvenue!", "Welcome!", "¡Bienvenido!", "欢迎！", "Benvenuto!"),
    "story_title": ("Histoire Interactive", "Interactive Story", "Historia Interactiva", "互动故事", "Storia Interattiva"),
    "start_game": ("Commencer le calcul mental", "Start Mental Math", "Comenzar cálculo mental", "开始心算", "Inizia il calcolo mentale"),
    "question": ("Question", "Question", "Pregunta", "问题", "Domanda"),
    "your_answer": ("Votre réponse:", "Your answer:", "Tu respuesta:", "你的答案：", "La tua risposta:"),
    "correct": ("Correct! +1 point", "Correct! +1 point", "¡Correcto! +1 punto", "正确！+1分", "Corretto! +1 punto"),
    "incorrect": ("Incorrect. La bonne réponse était", "Incorrect. Correct answer was", "Incorrecto. La respuesta era", "错误，正确答案是", "Errato. La risposta era"),
    "score": ("Score final", "Final Score", "Puntaje final", "最终得分", "Punteggio finale"),
    "story_intro": (
        "Vous entrez dans une forêt mystérieuse. Deux chemins s'offrent à vous.",
        "You enter a mysterious forest. Two paths lie ahead.",
        "Entras en un bosque misterioso. Dos caminos se abren ante ti.",
        "你走进了一片神秘的森林。前方有两条路。",
        "Entri in una foresta misteriosa. Davanti a te due sentieri."
    ),
    "left": ("Aller à gauche", "Go left", "Ir a la izquierda", "向左走", "Vai a sinistra"),
    "right": ("Aller à droite", "Go right", "Ir a la derecha", "向右走", "Vai a destra"),
    "left_result": (
        "Tu trouves un trésor magique sous un arbre. Fin de l'aventure.",
        "You find a magical treasure under a tree. End of story.",
        "Encuentras un tesoro mágico bajo un árbol. Fin de la historia.",
        "你在树下发现了一个神奇的宝藏。故事结束。",
        "Trovi un tesoro magico sotto un albero. Fine della storia."
    ),
    "right_result": (
        "Un loup apparaît, mais te laisse passer. Tu es libre. Fin.",
        "A wolf appears but lets you pass. You're free. The end.",
        "Un lobo aparece pero te deja pasar. Eres libre. Fin.",
        "一只狼出现了，但它让你通过。你自由了。结束。",
        "Appare un lupo ma ti lascia passare. Sei libero. Fine."
    ),
    "ads": ("📢 Partenaire : Découvrez nos formations IA sur [notre site](https://example.com)", 
            "📢 Partner: Discover our AI courses on [our site](https://example.com)",
            "📢 Socio: Descubre nuestros cursos de IA en [nuestro sitio](https://example.com)",
            "📢 合作伙伴：在[我们的网站](https://example.com)了解我们的AI课程",
            "📢 Partner: Scopri i nostri corsi di IA su [il nostro sito](https://example.com)")
}

# Fonction de traduction
def t(key):
    idx = {"Français": 0, "English": 1, "Español": 2, "中文": 3, "Italiano": 4}
    return translations[key][idx[langue]]

# Page titre
st.title(f"🎮 {t('title')}")
st.markdown(f"## {t('welcome')}")

# Calcul mental simple
if st.button(t("start_game")):
    score = 0
    for i in range(3):
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-", "*"])
        if op == "+": correct_ans = a + b
        elif op == "-": correct_ans = a - b
        else: correct_ans = a * b
        user = st.number_input(f"{t('question')} {i+1}: {a} {op} {b} =", key=f"q{i}")
        if st.button(f"✅ {t('your_answer')} {i+1}", key=f"btn{i}"):
            if user == correct_ans:
                score += 1
                st.success(t("correct"))
            else:
                st.error(f"{t('incorrect')}: {correct_ans}")
    st.success(f"🎉 {t('score')}: {score}/3")

# Histoire interactive
st.markdown(f"### 📖 {t('story_title')}")
st.markdown(t("story_intro"))
if st.button(t("left")):
    st.success(t("left_result"))
if st.button(t("right")):
    st.info(t("right_result"))

# Zone publicité
st.divider()
st.markdown(t("ads"))
