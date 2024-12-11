import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
data = pd.read_csv('numDocs.tsv', sep='\t')

# Conversion du timestamp
data['TIMESTAMP'] = pd.to_datetime(data['TIMESTAMP'], unit='s')

# Configuration du graphique
plt.figure(figsize=(16, 9))
plt.plot(data['TIMESTAMP'], data['SOLR1'], label='SOLR1', color='blue')
plt.plot(data['TIMESTAMP'], data['SOLR2'], label='SOLR2', color='orange')

# Personnalisation du graphique
plt.title('Évolution du nombre de documents SOLR1 et SOLR2', fontsize=14)
plt.xlabel('Temps', fontsize=12)
plt.ylabel('Nombre de documents', fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.5)
plt.legend()

# Affichage et sauvegarde
plt.tight_layout()
plt.show()
