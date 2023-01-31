from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import umap
import hdbscan
import sklearn.cluster as cluster
import math
import numpy as np

RESOLUTION = 6.4455

sns.set(style="darkgrid", context='notebook', rc={'figure.figsize': (14, 10)})
data = pd.read_excel("Merged Data_31.xlsx")
print(data.shape)
# data = data.dropna()
# print(data.shape)
# data['CCOM Distance'] = np.sqrt((data['FO_XM'] - data['CVH_X'])**2 + (data['FO_YM'] - data['CVH_Y'])**2)  # Pixels
# data['CCOM Distance'] = round(data['CCOM Distance'] / RESOLUTION, 2)
# data.to_excel('Consolidated + Distance.xlsx')
data_numeric = data.select_dtypes(exclude=['object'])  # Drop any columns with non-quantitative variables

region = {'DT': 0, 'VT': 1, 'VN': 2, 'N': 3, 'V': 4, 'DN': 5}

reducer = umap.UMAP()  # 21, 16, 10 is interesting n_neighbors
# n_neighbors low prioritizes local structure, higher = glboal. Default is 15
#
cleaned_data = data[[
    "Latitude (Radius Radians)",
    "Theta Degrees in Left Eye Space",
    "FO_Area",
    "FO_Perim.",
    "FO_Major",
    "FO_Minor",
    "FO_Circ.",
    "FO_Feret",
    "FO_%Area",
    "FO_Round",
    "FO_Solidity",
    "CVH_Area",
    "CVH_Perim.",
    "CVH_Feret",
    "Radius (um)",
    "CCOM Distance",
    "Mean Vessel Diameter",
    "Min Vessel Diameter",
    "Max Vessel Diameter",
    "Number of Contacts"
]].values

scaled_data = StandardScaler().fit_transform(cleaned_data)
embedding = reducer.fit_transform(cleaned_data)

# KMeans Labels- Don't Use
# kmeans_labels = cluster.KMeans(n_clusters=3).fit_predict(cleaned_data)

# HDBSCAN Labels
clusterer = hdbscan.HDBSCAN(min_samples=3, min_cluster_size=10)
clusterer.fit(cleaned_data)
palette = sns.color_palette()
cluster_colors = [sns.desaturate(palette[col], sat)
                  if col >= 0 else (0.5, 0.5, 0.5) for col, sat in
                  zip(clusterer.labels_, clusterer.probabilities_)]

plt.scatter(
    embedding[:, 0],
    embedding[:, 1],
    c=cluster_colors,
)
# c=[sns.color_palette()[x] for x in data.Region.map(region)])
plt.gca().set_aspect('equal', 'datalim')
plt.title('UMAP projection of the Dataset', fontsize=24)
plt.xlabel('UMAP1', fontsize=18)
plt.ylabel('UMAP2', fontsize=18)
plt.legend()

plt.show()
