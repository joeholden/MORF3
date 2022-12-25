import os

home_dir = "C:/Users/joema/Desktop/home/"
list_animals = [
    '3257 LE',
    '3257 RE',
    '3041 LE'
]

for animal in list_animals:
    animal_home = os.path.join(home_dir, animal)

    excel_sheets = os.path.join(animal_home, "Excel Sheets")
    png_vessels = os.path.join(animal_home, "Vessel and V5 PNGs")
    rois = os.path.join(animal_home, "ROIs")

    complex_centroids = os.path.join(excel_sheets, "Complex Centroids")
    vessel_distance = os.path.join(excel_sheets, "Distance to Vessel")
    vessel_diameter = os.path.join(excel_sheets, "Vessel Diameters")
    vessel_counts = os.path.join(excel_sheets, "Vessel Counts")

    hull = os.path.join(rois, "Complex Hull")
    full = os.path.join(rois, "Full Complex")

    dirs = [animal_home, excel_sheets, png_vessels, rois, complex_centroids, vessel_distance, vessel_diameter,
            vessel_counts, hull, full]
    for directory in dirs:
        os.mkdir(directory)

