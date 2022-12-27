import pandas as pd
import os
import math
import scipy.io

# Keep flip DV unchecked
ANIMAL_NUMBER = "3237"
SIDE = "right"
MATLAB_PATH = r"C:\Users\joema\Desktop\RETISTRUCT_Working\3237 LE\right.mat".replace("\\", os.sep)
SAVE_DIR = ""


def excel_from_matlab(path, animal, side):
    data = scipy.io.loadmat(MATLAB_PATH)
    data = data['Dss'][0][0][0]
    df = pd.DataFrame(data, columns=['Latitude (Radius Radians)', 'Longitude (Theta Radians)'])
    df.index += 1  # index starts at 1 now and is the direct correspondance to cell number

    df['Longitude (Theta Positive Radians)'] = [i + 2 * math.pi if i < 0 else i for i in df['Longitude (Theta Radians)']]
    df['Longitude (Theta Positive Degrees)'] = [round((i * 360) / (2 * math.pi), 1) for i in df['Longitude (Theta ' \
                                                                                                'Positive Radians)']]

    if SIDE.lower() == 'right':
        df['Theta Degrees in Left Eye Space'] = list(map(lambda x: 180 - x, df['Longitude (Theta Positive Degrees)']))
        df['Theta Degrees in Left Eye Space'] = [i - 360 if i > 360 else i for i in df['Theta Degrees in Left Eye Space']]
        df['Theta Degrees in Left Eye Space'] = [i + 360 if i < 0 else i for i in
                                                 df['Theta Degrees in Left Eye Space']]
    elif SIDE.lower() == 'left':
        df['Theta Degrees in Left Eye Space'] = df['Longitude (Theta Positive Degrees)']
    else:
        print('Spelling Error')

    def region(angle):
        if 0 < angle < 90:
            return 'DT'
        elif 90 < angle < 180:
            return 'DN'
        elif 180 < angle < 270:
            return 'VN'
        elif 270 < angle < 360:
            return 'VT'
        elif angle == 0 or angle == 360:
            return 'T'
        elif angle == 90:
            return 'D'
        elif angle == 180:
            return 'N'
        elif angle == 270:
            return 'V'
        else:
            return 'ERROR'

    df['Region'] = list(map(region, df['Theta Degrees in Left Eye Space']))

    df.to_excel(f'{ANIMAL_NUMBER}_{SIDE}_RETISTRUCT.xlsx')


excel_from_matlab(MATLAB_PATH, ANIMAL_NUMBER, SIDE)