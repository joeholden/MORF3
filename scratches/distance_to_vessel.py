import cv2
from contour_functions import centroid
import pandas as pd
import keyboard

ROI_PATH = 'big60.roi'
IMG_PATH = 'big_60.png'
RESOLUTION = 6.4455


# ////////////////////////////////////////////////////
def vessel_distance(roi_path, image_path, resolution):
    """
    Loads in an image with the astrocyte and vessels
    Displays the image and a circle around the centroid of the ROI provided.
    Slider allows you to alter the radius of the circle.
    Press q when the circle touches a vessel (min radius)
    Press escape to terminate for some reason.
    """

    def dummy(var):
        pass

    xc, yc = centroid(roi_path)
    image = cv2.imread(image_path)
    cv2.namedWindow('Astrocyte Centroid')
    cv2.createTrackbar('Radius', 'Astrocyte Centroid', 250, 1000, dummy)  # 50 is the initialization value for the bar

    end = False
    previous_slider_position = 0
    pressed_q = False
    end_radius_px = None

    while not end:
        current_slider = cv2.getTrackbarPos("Radius", "Astrocyte Centroid")
        if current_slider != previous_slider_position:
            rgb = image.copy()

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        slider_val = cv2.getTrackbarPos("Radius", "Astrocyte Centroid")
        cv2.circle(rgb, (xc, yc), slider_val, (255, 0, 255), thickness=3)

        cv2.imshow('Astrocyte Centroid', rgb)

        # Create Key Bindings to Output Radius Value
        if k == 113:  # key 'q'
            print(f'Radius px: {slider_val}\nRadius um: {round(slider_val / resolution, 1)}')
            pressed_q = True
            end_radius_px = slider_val

        if pressed_q:
            end = True

    print(end_radius_px)
    print(resolution)
    return end_radius_px, round((end_radius_px / resolution), 1), image_path


df = pd.DataFrame(columns=['Image', 'Radius (um)'])
rad_px, rad_um, img_path = vessel_distance(roi_path=ROI_PATH, image_path=IMG_PATH, resolution=RESOLUTION)
new_df = pd.DataFrame([[img_path, rad_um]], columns=['Image', 'Radius (um)'])
# df2 = df.append([new_df], ignore_index=True)
df = pd.concat([df, new_df], axis=0, ignore_index=True)
print(df)


df.to_excel('Distances to Vessels.xlsx')




