import streamlit as st
from utils.parser import parse_icd_file
from utils.generator import generate_derived_parameters

st.set_page_config(page_title="ICD Derived Generator")

st.title(" ICD Derived Parameter Generator")
st.markdown("Uploadez votre fichier ICD au format `.csv`")

uploaded_file = st.file_uploader(" Sélectionnez un fichier ICD (.csv)", type=["csv"])

if uploaded_file:
    # Lire le contenu du fichier via votre fonction parser
    rows = parse_icd_file(uploaded_file)

    # Générer les lignes dérivées
    derived_lines = generate_derived_parameters(rows)

    if derived_lines:
        derived_text = "".join(derived_lines)
        st.success("Paramètres dérivés générés avec succès.")
        st.download_button(
            label=" Télécharger le fichier dérivé généré",
            data=derived_text,
            file_name="derived_parameters.txt",
            mime="text/plain"
        )
    else:
        st.warning("Aucun paramètre dérivé n'a été généré.")
