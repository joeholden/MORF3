import cv2
from roifile2 import ImagejRoi
import matplotlib.pyplot as plt
import numpy as np
from tools import get_roi_pixels
from scipy.spatial import ConvexHull
from scipy.spatial.distance import euclidean
from shapely.geometry import Polygon


def get_axes_length(roi, show=False):
    """Returns the length of the major axis and minor axis of bounding rectangle (rotated as needed)
    This can be at times larger than FeretX and FeretY

    :param roi - an ImageJ ROI from polygon
    :param show - True if you want the plot displayed and False if you don't"""

    def distance(p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        delta_x = x2 - x1
        delta_y = y2 - y1

        d = pow(pow(delta_x, 2) + pow(delta_y, 2), 0.5)
        return d

    roi = ImagejRoi.fromfile(roi)
    coordinates = roi.integer_coordinates

    x_coordinates = [i[0] for i in coordinates]
    y_coordinates = [i[1] for i in coordinates]
    fig, ax = plt.subplots()
    plt.fill(x_coordinates, y_coordinates, color="grey")

    rectangle = cv2.minAreaRect(coordinates)  # (center(x, y), (width, height), angle of rotation)
    box = cv2.boxPoints(rectangle)
    box = np.int0(box)
    box = np.vstack([box, box[0]])
    axis_1 = (distance(box[0], box[1]) + distance(box[2], box[3])) / 2
    axis_2 = (distance(box[1], box[2]) + distance(box[3], box[0])) / 2

    ax1_is_major = False
    if axis_1 > axis_2:
        ax1_is_major = True

    colors = {
        "ax1": 'green' if ax1_is_major else 'red',
        "ax2": 'red' if ax1_is_major else 'green'
    }

    plt.plot([box[0][0], box[1][0]], [box[0][1], box[1][1]], color=colors["ax1"],
             label=f"major:{round(axis_1, 1)}" if ax1_is_major else f"minor:{round(axis_1, 1)}")
    plt.plot([box[2][0], box[3][0]], [box[2][1], box[3][1]], color=colors["ax1"])
    plt.plot([box[1][0], box[2][0]], [box[1][1], box[2][1]], color=colors["ax2"],
             label=f"minor:{round(axis_2, 1)}" if ax1_is_major else f"major:{round(axis_2, 1)}")
    plt.plot([box[3][0], box[0][0]], [box[3][1], box[0][1]], color=colors["ax2"])

    # plt.plot([i[0] for i in box], [i[1] for i in box], color='#702963', lw=3, label='major')

    plt.scatter(x_coordinates, y_coordinates, color='black')
    plt.title("ROI Contour and Bounding Rectangle", fontsize=16)
    ax.invert_yaxis()
    plt.legend()
    if show:
        plt.show()

    return round(max(axis_1, axis_2), 1), round(min(axis_1, axis_2), 1)


def contour_area(roi, resolution=None):
    """Returns the number of pixels within ROI and the area
    in terms of microns if a resolution is provided"""
    inside_px = get_roi_pixels(roi)
    pixel_area = len(inside_px)
    area = None
    if resolution is not None:
        area = pixel_area / resolution
    return pixel_area, area


def perimeter_convex_hull(roi):
    """returns the perimeter of the ROI"""
    roi = ImagejRoi.fromfile(roi)
    coordinates = roi.integer_coordinates

    hull = ConvexHull(coordinates)

    vertices = hull.vertices.tolist() + [hull.vertices[0]]
    perimeter = np.sum([euclidean(x, y) for x, y in zip(coordinates[vertices], coordinates[vertices][1:])])
    return round(perimeter, 1)


def centroid(roi_path, image_path=None, show=False):
    """returns the centroid of the given roi (xc, yc).
    If an image_path is provided and show=True, the value is printed and shown on the image"""
    roi = ImagejRoi.fromfile(roi_path)
    coordinates = roi.integer_coordinates

    outline = Polygon(coordinates)
    xc = int(outline.centroid.x) + roi.left
    yc = int(outline.centroid.y) + roi.top

    if show:
        print(xc, yc)
        image = cv2.imread(image_path)
        cv2.circle(image, (xc, yc), 3, (255, 255, 255), thickness=3)
        cv2.imshow('i', image)
        cv2.waitKey()
        cv2.destroyAllWindows()

    return xc, yc



