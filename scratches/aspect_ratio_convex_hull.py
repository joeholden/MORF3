import matplotlib.pyplot as plt
from roifile2 import ImagejRoi
import matplotlib.pyplot as plt
import numpy as np

roi = ImagejRoi.fromfile("polygon.roi")
coordinates = roi.integer_coordinates
x_data = [i[0] for i in coordinates]
y_data = [i[1] for i in coordinates]
xy = np.array([x_data, y_data])

eigvals, eigvecs = np.linalg.eig(np.cov(xy))

fig, (ax1, ax2) = plt.subplots(nrows=2)
x, y = xy
center = xy.mean(axis=-1)

for ax in [ax1, ax2]:
    ax.plot(x, y, 'ro')
    ax.axis('equal')
    ax.invert_yaxis()


for val, vec in zip(eigvals, eigvecs.T):
    # val *= 2
    print(np.vstack((center + val * vec, center, center - val * vec)).T)
    x, y = np.vstack((center + val * vec, center, center - val * vec)).T
    ax2.plot(x, y, 'b-', lw=3)
    ax2.scatter(x, y,)
    plt.xlim(-150, 400)
    plt.ylim(-30, 400)
    ax.invert_yaxis()

print(eigvals)
print(eigvecs.T)

plt.show()

print(eigvals)
print(eigvecs.T)
