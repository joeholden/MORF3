import os

test_dir = r"E:\MORF disease\Images\3341 RE\single".replace("\\", os.sep)

for root, dirs, files in os.walk(test_dir):
    for file in files:
        if file[0] == str(0):
            zeros_removed_filename = file.lstrip("0")
            os.rename(os.path.join(root, file), os.path.join(root, zeros_removed_filename))
