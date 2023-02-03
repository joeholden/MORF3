import cv2

name = "Asset 3.png"
home_dir = "C:/Users/joema/Desktop/1x/"
path = home_dir + name

im = cv2.imread(path)

for i in range(im.shape[1]):
    for j in range(im.shape[0]):
        px = im[j, i]
        new_px = [px[2], px[1], px[2]]
        im[j, i] = new_px

# cv2.imshow('image', im)
# cv2.waitKey()
# cv2.destroyAllWindows()
cv2.imwrite(home_dir + 'magenta_' + name, im)
