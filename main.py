from contour_functions import get_axes_length, contour_area, perimeter_convex_hull

roi = "polygonz.roi"

major_axis, minor_axis = get_axes_length(roi, True)
contour_area_px, contour_area_um = contour_area(roi)
perimeter = perimeter_convex_hull(roi)

print(major_axis, minor_axis, contour_area_px, contour_area_um, perimeter)
