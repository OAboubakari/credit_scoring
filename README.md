# 💳 Credit Scoring App

Application de prédiction du risque de crédit utilisant le Machine Learning et développée avec Streamlit.

---

# 📌 Description

Cette application permet de prédire si un client présente un bon ou un mauvais risque de crédit à partir de plusieurs informations financières et personnelles.

Le modèle utilise un algorithme de Machine Learning entraîné sur des données de crédit afin d'aider à la prise de décision financière.

---

# 🚀 Fonctionnalités

* Interface interactive avec Streamlit
* Encodage automatique des variables catégorielles
* Chargement des modèles sauvegardés avec Joblib
* Prédiction en temps réel du risque de crédit
* Interface simple et intuitive

---

# 🛠️ Technologies utilisées

* Python
* Streamlit
* Pandas
* Scikit-Learn
* Joblib

---

# 📂 Structure du projet

```bash
Credit_Scoring/
│
├── app.py
├── logistic_regression.pkl
├── encoders.pkl
├── requirements.txt
├── README.md
└── data/
```

---

# ⚙️ Installation

## 1. Cloner le projet

```bash
git clone https://github.com/votre-username/credit-scoring-app.git
```

## 2. Accéder au dossier

```bash
cd credit-scoring-app
```

## 3. Créer un environnement virtuel

```bash
python -m venv venv
```

## 4. Activer l’environnement

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# 📦 Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# ▶️ Lancer l’application

```bash
streamlit run app.py
```

---

# 🧠 Variables utilisées

* Age
* Sexe
* Profession
* Type de logement
* Compte épargne
* Compte courant
* Montant du crédit
* Durée du crédit
* Objectif du crédit

---

# 📊 Modèle Machine Learning

Le projet utilise :

* Régression Logistique (Logistic Regression)

Le modèle a été entraîné avec :

* Encodage des variables catégorielles
* Nettoyage des données
* Séparation train/test
* Évaluation des performances

---

# 📈 Métriques d’évaluation

Les métriques utilisées :

* Accuracy
* Recall
* F1 Score
* ROC AUC

---

# 🔐 Sauvegarde du modèle

Les objets sauvegardés :

* `logistic_regression.pkl`
* `encoders.pkl`

Utilisation de :

```python
joblib.dump()
joblib.load()
```

---

# 📷 Aperçu de l’application

L’application permet à l’utilisateur :

1. de saisir les informations client,
2. de lancer une prédiction,
3. d’obtenir instantanément le niveau de risque du crédit.

---

# Auteur

Projet développé par Ouedraogo Aboubakari


