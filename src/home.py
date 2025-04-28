import streamlit as st
from Data.db_connections.mysql_connections import sql_connection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Governance VDL Reporting: 👋")

st.write("Observability and Data Catalog")

st.write("Observability")
df = pd.read_sql("SELECT * FROM events", con= sql_connection("monitoring"))
st.dataframe(df)

plt.figure(figsize=(10, 6))
sns.histplot(df, x='time_execution', hue='description', palette='Set2', kde=True, bins=20)

# Ajouter un titre et des labels
plt.title('Distribution des durées d\'exécution par description')
plt.xlabel('Durée d\'exécution')
plt.ylabel('Fréquence')


# Afficher l'histogramme dans Streamlit
st.pyplot(plt)

st.write("Data catalog")
df = pd.read_sql("SELECT * FROM data_catalog", con=sql_connection("treasury_catalogs"))
st.dataframe(df)