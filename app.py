import streamlit as st
import pandas as pd
import joblib

#Import des models et Encoders
encoders = joblib.load("encoders.pkl")
model = joblib.load("logistic_regression.pkl")

st.title("Scoring de Credit ")
st.write("Saisir les informations du client pour predire le risk")


age = st.number_input("Age" , min_value=18,max_value=80, value=30)
sex = st.selectbox("Sex", ["male","female"])
job = st.number_input("Categorie Professionnelle (0-3)",min_value=0,max_value=3, value=1)
housing = st.selectbox("Logement",['own', 'free', 'rent'])
saving_accounts = st.selectbox("Compte d'epargne",['little', 'quite rich', 'rich','moderate'])
checking_accounts = st.selectbox("Compte courant",['little', 'moderate','rich'])
credit_amount = st.number_input("Montant du credit", min_value=0)
Duration = st.number_input("Duree (Mois)", min_value=1 , value=12)
Purpose = st.selectbox("Objectif du Crédit",['radio/TV', 'education', 'furniture/equipment', 'car', 'business',
       'domestic appliances', 'repairs', 'vacation/others'])

input_dataframe = pd.DataFrame({
    "Age": [age],

    "Sex": [encoders["Sex"].transform([sex])[0]],

    "Job": [job],

    "Housing": [encoders["Housing"].transform([housing])[0]],

    "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],

    "Checking account": [encoders["Checking account"].transform([checking_accounts])[0]],

    "Credit amount": [credit_amount],

    "Duration": [Duration],

    "Purpose": [encoders["Purpose"].transform([Purpose])[0]]
})

if st.button("Prédire le risque"):

    prediction = model.predict(input_dataframe)[0]

    if prediction == 1:
        st.success("Le risque du crédit est bon")
    else:
        st.error("Attention, le risque est élevé")