# Load the file to inspect its content
import pandas as pd

# File path
file_path = '/home/fra/UniNA-diagram/numDocs.tsv'

# Load the data
data = pd.read_csv(file_path, sep='\t')

# Display the first few rows to understand the structure
data.head()


import matplotlib.pyplot as plt
from datetime import datetime

# Convert TIMESTAMP to datetime for better visualization
data['TIMESTAMP'] = pd.to_datetime(data['TIMESTAMP'], unit='s')

# Plotting with multiple lines
#plt.figure(figsize=(12, 6))
plt.figure(figsize=(16, 9))
plt.plot(data['TIMESTAMP'], data['SOLR1'], label='SOLR1', color='blue')
plt.plot(data['TIMESTAMP'], data['SOLR2'], label='SOLR2', color='orange')
#plt.plot(data['TIMESTAMP'], data['SOLR3'], label='SOLR3', color='green')

# Adding titles and labels
plt.title('SOLR1 e SOLR2 nel tempo', fontsize=14)
plt.xlabel('Tempo', fontsize=12)
plt.ylabel('numDocs', fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.5)
plt.legend()

# Save the updated plot as an image
output_path_multi = '/home/fra/UniNA-diagram/numDocs.svg'
plt.savefig(output_path_multi)
plt.show()

output_path_multi
