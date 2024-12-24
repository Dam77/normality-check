import pandas as pd
import streamlit as st
from scipy.stats import shapiro, normaltest, anderson

# Vous allez décider du seuil de risque 'alpha' pour la normalité.

# Fonction de vérification de normalité
def check_normality(data, alpha):
    results = {}
    stat, p_value = shapiro(data)
    if p_value > alpha:
        results['Shapiro-Wilk'] = f"La distribution est normale (p-valeur = {p_value:.4f}, H0 non rejetée)"
    else:
        results['Shapiro-Wilk'] = f"La distribution n'est pas normale (p-valeur = {p_value:.4f}, H0 rejetée)"
    return results

# Application Streamlit
st.title("Vérification automatique de normalité")

# Explication de l'objectif
st.write("Cette application teste si une série de données suit une distribution normale.")

#  Choix du seuil de risque (0.05 par default). Seuil de confiance de 0.95 signifie un risque de 1-0.95=0.05
alpha = st.number_input("Entrez le seuil alpha (par exemple, 0.05) :", min_value=0.001, max_value=1.0, value=0.05)

# Importation de données
uploaded_file = st.file_uploader("Chargez un fichier CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :", df.head())

    # Sélection de la colonne
    column = st.selectbox("Sélectionnez une colonne numérique :", df.select_dtypes(include=['float', 'int']).columns)
    
    # Analyse de normalité
    if st.button("Vérifier la normalité"):
        st.write("""
Le **test de Shapiro-Wilk** vérifie si les données suivent une distribution normale. 
- **Hypothèse nulle (H0)** : Les données suivent une distribution normale.
- Une **p-valeur > alpha** signifie que H0 n'est pas rejetée (les données sont normales).
- Une **p-valeur <= alpha** signifie que H0 est rejetée (les données ne sont pas normales).
""")
        results = check_normality(df[column].dropna(), alpha)
        st.write(f"Résultats pour la colonne '{column}':", results)

    
st.write("Projet réalisé avec Python. Pour avoir le code source, [cliquez ici](https://github.com/dam77/normality-check).")
