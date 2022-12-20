from roifile2 import ImagejRoi
import matplotlib.pyplot as plt
import math
import pandas as pd
import scipy
import numpy as np

roi = ImagejRoi.fromfile("polygon.roi")
coordinates = roi.integer_coordinates

# array = [(0, 0), (0, 1), (1, 0), (1, 1)]
m = scipy.spatial.distance_matrix(coordinates, coordinates, p=2, threshold=1000000)

# Gets non-zero max and min distances between coordinates
min_val = np.min(m[np.nonzero(m)])
max_val = np.max(m[np.nonzero(m)])

# Gets a list of distance matrix indices that are max and min (row, col)
max_xy = np.where(m == max_val)
min_xy = np.where(m == min_val)
distance_array_coordinates_max = list(zip(max_xy[0], max_xy[1]))
distance_array_coordinates_min = list(zip(min_xy[0], min_xy[1]))

output_max, seen_max = [], set()
for item in distance_array_coordinates_max:
    t1 = tuple(item)
    if t1 not in seen_max and tuple(reversed(item)) not in seen_max:
        seen_max.add(t1)
        output_max.append(item)

output_min, seen_min = [], set()
for item in distance_array_coordinates_min:
    t1 = tuple(item)
    if t1 not in seen_min and tuple(reversed(item)) not in seen_min:
        seen_min.add(t1)
        output_min.append(item)


print(output_max, output_min)

headers = []
for i in coordinates:
    headers.append(tuple(i))


df = pd.DataFrame(m, columns=headers, index=headers)

# df.to_excel('array.xlsx')
# print('\n')
# print(roi.integer_coordinates)

plt.plot([i[0] for i in coordinates], [i[1] for i in coordinates], color='green')  # plots ROI outline
plt.scatter([i[0] for i in coordinates], [i[1] for i in coordinates], color='green')  # plots ROI points
plt.scatter([367, 8, 201, 165], [279, 141, 7, 0], color='purple')  # plots max and min axis points
plt.plot([367, 8], [279, 141], color='red')
plt.gca().invert_yaxis()
plt.show()