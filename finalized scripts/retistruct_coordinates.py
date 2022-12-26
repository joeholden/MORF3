import pandas as pd
import os
import math
import scipy.io

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
        df['Theta Degrees in Left Eye Space'] = list(map(lambda x: x + 180, df['Longitude (Theta Positive Degrees)']))
        df['Theta Degrees in Left Eye Space'] = [i - 360 if i > 360 else i for i in df['Theta Degrees in Left Eye Space']]
    elif SIDE.lower() == 'left':
        df['Theta Degrees in Left Eye Space'] = df['Longitude (Theta Positive Degrees)']
    else:
        print('Spelling Error')

    df.to_excel(f'{ANIMAL_NUMBER}_{SIDE}_RETISTRUCT.xlsx')


excel_from_matlab(MATLAB_PATH, ANIMAL_NUMBER, SIDE)