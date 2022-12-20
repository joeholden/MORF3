import math
from roifile import ImagejRoi

roi = ImagejRoi.fromfile("polygonz.roi")
v = list(roi.integer_coordinates)


def find_major_minor_axes(vertices):
    # Calculate the centroid of the polygon
    centroid_x = sum(x for x, y in vertices) / len(vertices)
    centroid_y = sum(y for x, y in vertices) / len(vertices)
    centroid = (centroid_x, centroid_y)

    # Calculate the angle of each vertex relative to the centroid
    angles = []
    for x, y in vertices:
        dx = x - centroid_x
        dy = y - centroid_y
        angle = math.atan2(dy, dx)
        angles.append(angle)

    # Sort the vertices by their angle relative to the centroid
    vertices_with_angles = list(zip(vertices, angles))
    vertices_with_angles.sort(key=lambda x: x[1])

    # Find the distances from the centroid to each vertex
    distances = []
    for x, y in vertices:
        dx = x - centroid_x
        dy = y - centroid_y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        distances.append(distance)

    # Find the minimum and maximum distances from the centroid
    minor_axis = min(distances)
    major_axis = max(distances)

    return (major_axis, minor_axis)

print(find_major_minor_axes(v))