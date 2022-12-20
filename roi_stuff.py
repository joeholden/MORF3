from roifile2 import ImagejRoi
import matplotlib.pyplot as plt

roi = ImagejRoi.fromfile("0160-0137.roi")
for i in roi.multi_coordinates:
    print(i)
cords = list(roi.multi_coordinates)
cords = [i for i in cords if i != 4.0]  # Strips out the 4.0 which is used as a divider. Bug waiting to happen

sub_roi_data = []  # (sub_roi ident., x, y)
for i in range(0, len(cords) - 2, 3):
    sub_roi_data.append((cords[i], cords[i + 1], cords[i + 2]))

roi.plot()  # this is modified from the original roifile PyPy download
plt.scatter([i[1] for i in sub_roi_data], [i[2] for i in sub_roi_data], color='green')

plt.show()
