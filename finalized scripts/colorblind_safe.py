import cv2
import os
import math

home_dir = "C:/Users/Acer/Desktop/test/"


def mix(a, b, t):
    val = math.sqrt(((1 - t) * a**2) + (t * b**2))
    return val


for root, dirs, files in os.walk(home_dir):
    for file in files:
        im = cv2.imread(os.path.join(root, file))
        for i in range(im.shape[1]):
            for j in range(im.shape[0]):
                px = im[j, i]
                if tuple(px) == (255, 255, 255) or tuple(px) == (0, 0, 0):  # white / black
                    new_px = [px[0], px[1], px[2]]
                elif tuple(px)[0] != 0 and tuple(px)[1] == 0 and tuple(px)[2] == 0:  # blue
                    new_px = [px[0], px[0], 0]  # cyan
                elif tuple(px)[0] == 0 and tuple(px)[1] != 0 and tuple(px)[2] == 0:  # green
                    new_px = [0, px[1], px[1]]  # yellow
                elif tuple(px)[0] == 0 and tuple(px)[1] == 0 and tuple(px)[2] != 0:  # red
                    new_px = [px[2], 0, px[2]]  # magenta
                else:
                    # new_px = [px[0] + px[2], px[0] + px[1], px[1] + px[2]]
                    # new_px = [max(min(x, 255), 0) for x in new_px]
                    new_px = [mix(px[0], px[2], 0.5), mix(px[0], px[1], 0.5), mix(px[1], px[2], 0.5)]
                im[j, i] = new_px

        cv2.imwrite(os.path.join(root, f"recolored/{file}55.png"), im)
