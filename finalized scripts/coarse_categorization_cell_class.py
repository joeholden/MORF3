from collections import defaultdict
import os
import pandas as pd
import cv2

"""
Q: Full Enveloping
W: Partial Enveloping
A: Mural
S: Foot-Associated
M: Re-Do

Tap key twice for each image to advance. If you made a mistake, press 'M' and you can re-do it
"""

image_dir = "test_ident"
output_dir = "test_ident"
identity = "3233 LE"
image_identity = defaultdict(str)

end_run = False
for root, dirs, files in os.walk(image_dir):
    for file in files:
        def begin_loop():
            global end_run
            redo = False
            image = cv2.imread(os.path.join(root, file))
            cv2.imshow('Image', image)

            while True:
                k = cv2.waitKey(1) & 0xFF
                if k == 27:
                    end_run = True
                    break
                if k == ord("q"):
                    print('Q: Full Enveloping')
                    image_identity[int(file.split(".")[0])] = "Full Enveloping"
                    break
                if k == ord("w"):
                    print('W: Partial Enveloping')
                    image_identity[int(file.split(".")[0])] = "Partial Enveloping"
                    break
                if k == ord("a"):  # key 'q'
                    print('A: Mural')
                    image_identity[int(file.split(".")[0])] = "Mural"
                    break
                if k == ord("s"):  # key 'q'
                    print('S: Foot Associated')
                    image_identity[int(file.split(".")[0])] = "Foot Associated"
                    break
            while True:
                k = cv2.waitKey(1) & 0xFF
                if k == 27:
                    end_run = True
                    break
                if k == ord("q"):
                    break
                if k == ord("w"):
                    break
                if k == ord("a"):  # key 'q'
                    break
                if k == ord("s"):  # key 'q'
                    break
                if k == ord("m"):  # mistake made
                    redo = True
                    image_identity[int(file.split(".")[0])] = "Back"
                    print(image_identity[int(file.split(".")[0])])
                    break
            cv2.destroyAllWindows()
            print("Redo:" + str(redo))
            return redo

        if not end_run:
            r = begin_loop()
            if r:
                begin_loop()


df = pd.DataFrame(image_identity.items(), columns=['Cell', 'Class'])
df = df.sort_values("Cell")
df.to_excel(f"{output_dir}/{identity}_classes.xlsx")
