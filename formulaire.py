import streamlit as st
import numpy as np
import pandas as pd
import re
import os

# Fonction de validation d'e-mail
def is_valid_email(email):
    """
    Vérifie si l'adresse e-mail est valide.
    
    :param email: Adresse e-mail à vérifier
    :return: True si l'adresse e-mail est valide, False sinon
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def formular():
    # Initialiser les variables dans st.session_state si elles n'existent pas
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    # Formulaire de suggestions
    st.header("Vos Suggestions")
    with st.form(key='suggestion_form'):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        suggestion = st.text_area("Suggestion")
        submit_button = st.form_submit_button(label='Envoyer')

    if submit_button:
        if is_valid_email(email):
            st.session_state.submitted = True
            st.session_state.name = name

            # Enregistrer la suggestion dans un fichier CSV
            new_data = pd.DataFrame([[name, email, suggestion]], columns=["Nom", "Email", "Suggestion"])

            if os.path.exists('suggestions.csv'):
                new_data.to_csv('suggestions.csv', mode='a', header=False, index=False)
            else:
                new_data.to_csv('suggestions.csv', index=False)
            
            st.write(f"Merci pour votre suggestion, {st.session_state.name} !")
        else:
            st.error("Veuillez entrer une adresse e-mail valide.")

