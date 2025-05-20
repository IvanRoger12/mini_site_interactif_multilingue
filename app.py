
import streamlit as st
import json
import random

# Charger les histoires depuis un fichier JSON
with open("histoires_enfants.json", "r", encoding="utf-8") as f:
    histoires = json.load(f)

st.set_page_config(page_title="Histoires pour enfants", layout="centered")
st.title("📖 Histoires Magiques pour Enfants")

# Choix du mode : liste ou aléatoire
mode = st.radio("Choisis ton mode de lecture :", ["📚 Liste des histoires", "🎲 Histoire aléatoire"])

# Choisir une histoire
if mode == "📚 Liste des histoires":
    titres = [h["titre"] for h in histoires]
    choix = st.selectbox("Choisis une histoire :", titres)
    histoire = next(h for h in histoires if h["titre"] == choix)
else:
    histoire = random.choice(histoires)
    st.success(f"Histoire aléatoire sélectionnée : {histoire['titre']}")

# Affichage de l'histoire
st.header(histoire["titre"])
st.write(histoire["intro"])

col1, col2 = st.columns(2)
if col1.button(histoire["choix"][0]):
    st.success(histoire["resultats"][0])
if col2.button(histoire["choix"][1]):
    st.info(histoire["resultats"][1])
