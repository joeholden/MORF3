import cv2
import pandas as pd
import os
import glob
import datetime
import keyboard
import re

"""
This program allows you to start from your last location each time.
If you have analyzed some images so far, the program reads in your previous data sheet and looks at each image filename
to see if it has been processed already. Only new images are processed. A new excel sheet is added each time so you
don't have to worry about overwriting any existing data by accident. 

Load image as PNG

Left Mouse: Add point
Q: Add point and end colletion of points
W: Add point and continue adding
E: Undo last addition and continue adding
F: Undo last selection and end collection of points
ESC: Skip if the motif is absent

If you add one and realize that it was the last one, just hit e and then re add it and hit q

"""
# Only Modify the HOME Directory
HOME = "C:/Users/Acer/Desktop/practice motif program/9999 LE/"

IMGS_DIR = os.path.join(HOME, 'v5 neuronal png')
EXCEL_DIR = os.path.join(HOME, 'excel')
IMG_SAVE_DIR = os.path.join(HOME, "IMG_SPOT_OVERLAY")


def motif_count(image_path):
    """
    Loads an image and displays it using OpenCV. Program awaits mouse clicks to lock in coordinates for the width
    of a blood vessel. Left click to lock in the first coordinate and right click to lock in the second. At this point,
    a line should be completed. Now the program is awaiting a keyboard event to determine how to proceed. If 'W' is
    pressed, the user is allowed to add another vessel. Unlimited number of vessels can be added. If 'Q' is pressed,
    the function ends and returns an array of diameters of the vessels and the image path.
    """
    image = cv2.imread(image_path)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    width = int(image.shape[1] * .80)
    height = int(image.shape[0] * .80)
    cv2.resizeWindow("image", width, height)

    x1, y1, mouse_x, mouse_y = None, None, None, None
    all_points = []  # these points are true image coordinates- it is independent of scaling factor to display the image

    q_pressed = False
    w_pressed = False
    e_pressed = False
    f_pressed = False

    def on_mouse(event, x, y, flags, param):
        nonlocal x1, y1, mouse_x, mouse_y, all_points
        if event == cv2.EVENT_MOUSEMOVE:
            mouse_x, mouse_y = x, y
        if event == cv2.EVENT_LBUTTONDOWN:
            x1, y1, = x, y

    cv2.setMouseCallback('image', on_mouse)  # when an event occurs it runs on_mouse

    while True:
        # Load in a copy of the original image so the line you draw doesn't leave traces
        image_c = image.copy()

        if x1 is not None:  # did the user click
            if (x1, y1) not in all_points:
                all_points.append((x1, y1))

        # Re draw points each time the image refreshes
        for p in all_points:
            cv2.circle(image_c, (p[0], p[1]), 7, (0, 255, 255), -1)

        cv2.imshow('image', image_c)

        # sub loop waiting for capture of key press (action selection)
        if x1 is not None:
            while not q_pressed or not w_pressed or not e_pressed or not f_pressed:
                k = cv2.waitKey(20) & 0xFF
                if k == 27:
                    break
                if k == 113:
                    q_pressed = True
                    break
                if k == 119:
                    w_pressed = True
                    break
                if k == 101:
                    e_pressed = True
                    break
                if k == 102:
                    f_pressed = True
                    break

        if q_pressed:  # q, add point and end
            break
        if w_pressed:  # w, add point and add more
            x1, y1, mouse_x, mouse_y = None, None, None, None
            w_pressed = False
        if e_pressed:  # e (erase last point and continue)
            x1, y1, mouse_x, mouse_y = None, None, None, None
            e_pressed = False
            all_points.pop()
        if f_pressed:  # e (erase last point and end)
            f_pressed = False
            all_points.pop()
            print('That last point was removed even though the image still had the circle')
            break

        k = cv2.waitKey(20) & 0xFF

        if k == 27:
            break
        elif k == ord('a'):
            print(mouse_x, mouse_y)

    for p in all_points:
        cv2.circle(image_c, (p[0], p[1]), 7, (0, 255, 255), -1)
    cv2.imwrite(os.path.join(IMG_SAVE_DIR, os.path.basename(image_path)), image_c)

    return image_path, all_points


def choice_to_continue():
    while True:
        a = keyboard.read_key()

        if a == '1':
            return 1
        if a == '0':
            return 0


# If execution of the program was stopped at some point, we want to be able to
# process the rest of the files without repeats
try:
    list_of_files = glob.glob(os.path.join(EXCEL_DIR, 'motif count/*'))  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    df = pd.read_excel(latest_file, index_col='Unnamed: 0')
except ValueError:
    df = pd.DataFrame()

for root, dirs, files in os.walk(IMGS_DIR):
    for file in files:
        image_path = os.path.join(root, file).split("/")[-1]
        id = re.search(pattern=r"/(\d+) (\w+)", string=root)
        identifier = id[1] + "_" + id[2] + "_" + image_path.strip(".png")

        if identifier in df.columns:
            print(identifier)
            continue
        else:
            image_path, coordinates = motif_count(image_path=os.path.join(root, file))
            coordinates = pd.Series(coordinates)
            image_path = image_path.split('/')[-1].strip('.png')
            id = re.search(pattern=r"/(\d+) (\w+)", string=root)
            identifier = id[1] + "_" + id[2] + "_" + image_path
            new_df = pd.DataFrame(coordinates, columns=[identifier])
            df = pd.concat([df, new_df], axis=1)
            print('Run Another? yes: 1, n: 0?\n')
            key = choice_to_continue()
            if key == 0:
                break

df.to_excel(os.path.join(EXCEL_DIR, f'motif count/{datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")}.xlsx'))

print(df.T)
print(df.shape)
