import cv2
import matplotlib.pyplot as plt
import numpy


IN_SIZE_X = 1920
IN_SIZE_Y = 1080
N_BLACK_PIXELS = 3

OUT_SIZE_X = IN_SIZE_X * N_BLACK_PIXELS + 1
OUT_SIZE_Y = IN_SIZE_Y * N_BLACK_PIXELS + 1


result = numpy.full((OUT_SIZE_Y, OUT_SIZE_X, 3), 0)


img = cv2.imread("./../example.jpg")

# plt.imshow(img)
# plt.show()

# print(img.shape)

counter_x = 0
counter_y = 0


for y in range(OUT_SIZE_Y):
    if y == 0:
        continue

    if y % N_BLACK_PIXELS != 0:
        continue

    for x in range(OUT_SIZE_X):

        if x == 0:
            continue
        
        if x % N_BLACK_PIXELS == 0:
            for color in range(3):
                result[y][x][color] = img[counter_y][counter_x][color]
            counter_x += 1

    counter_x = 0
    counter_y += 1


cv2.imwrite("./../result.png", result)

