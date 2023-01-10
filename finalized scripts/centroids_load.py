import pandas as pd
import re


def read_complex_outline_centroids(path):
    """Returns (cell number, x coordinate of centroid, y coordinate of centroid)"""
    df = pd.read_csv(path)
    filenames = list(df['Label'])

    def get_cell_number_regex(centroid_output_label):
        """Returns the nubmer of the cell whose ROI string was input"""
        pattern = r'full_outline_(\d+).nd2.roi:full_outline'
        number = re.search(pattern=pattern, string=centroid_output_label).group(1)
        return number

    filenames = map(get_cell_number_regex, filenames)
    x = df['X']
    y = df['Y']

    centroid_information = list(zip(filenames, x, y))
    return centroid_information
