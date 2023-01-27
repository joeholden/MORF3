from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import umap
import hdbscan
import sklearn.cluster as cluster

sns.set(style="darkgrid", context='notebook', rc={'figure.figsize': (14, 10)})
data = pd.read_excel("C:/Users/joema/Downloads/Merged Data.xlsx")
data = data.dropna()
data_numeric = data.select_dtypes(exclude=['object'])  # Drop any columns with non-quantitative variables

region = {'DT': 0, 'VT': 1, 'VN': 2, 'N': 3, 'V': 4, 'DN': 5}

reducer = umap.UMAP(n_neighbors=16, min_dist=0)  # 21, 16, 10 is interesting n_neighbors
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
]].values

scaled_data = StandardScaler().fit_transform(cleaned_data)
embedding = reducer.fit_transform(cleaned_data)

kmeans_labels = cluster.KMeans(n_clusters=4).fit_predict(cleaned_data)
hdbscan_labels = hdbscan.HDBSCAN(min_samples=2, min_cluster_size=50).fit_predict(cleaned_data)

plt.scatter(
    embedding[:, 0],
    embedding[:, 1],
    c=kmeans_labels,
    cmap='seismic')
# c=[sns.color_palette()[x] for x in data.Region.map(region)])
plt.gca().set_aspect('equal', 'datalim')
plt.title('UMAP projection of the Dataset', fontsize=24)

plt.show()
