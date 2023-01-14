from collections import defaultdict
import os
import pandas as pd
import cv2

image_dir = "test_ident"
output_dir = "test_ident"
identity = "3233 LE"
image_identity = defaultdict(str)

for root, dirs, files in os.walk(image_dir):
    for file in files:
        image = cv2.imread(os.path.join(root, file))
        cv2.imshow('Image', image)

        while True:
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            if k == ord("q"):
                print('Pressed Q')
                image_identity[file.split(".")[0]] = "Full Enveloping"
                break
            if k == ord("w"):
                print('Pressed W')
                image_identity[file.split(".")[0]] = "Partial Enveloping"
                break
            if k == ord("a"):  # key 'q'
                print('Pressed A')
                image_identity[file.split(".")[0]] = "Mural"
                break
            if k == ord("s"):  # key 'q'
                print('Pressed S')
                image_identity[file.split(".")[0]] = "Foot Associated"
                break

df = pd.DataFrame(image_identity.items(), columns=['Cell', 'Class'])
df.to_excel(f"{output_dir}/{identity}_classes.xlsx")