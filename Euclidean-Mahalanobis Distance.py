from PIL import Image
import numpy as np
import math
import time
import os
import yaml

start_time = time.time()
img = []
width = 0
height = 0
path = os.path.dirname(os.path.realpath(__file__)) + "/"

f = open(path + "config.yaml", "r")
config = yaml.load(f)
f.close()


def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def create_ethalon(x1, y1, x2, y2):
    ethalon = []
    mean = []
    for h in range(y1, y2):
        for w in range(x1, x2):
            ethalon.append(pixels[width * h + w])

    for j in range(12):
        sum = 0
        for i in range(len(ethalon)):
            sum += ethalon[i][j]
        mean.append((int)(sum / (len(ethalon))))
    print(mean, "\n\n\n\n\n")
    return mean


def euclidean_mahalanobis(x, y):
    xMy = [k - j for k, j in zip(x, y)]
    x = np.transpose(x)
    cov_matrix = np.cov(x, bias=False)
    se = np.linalg.inv(np.sum([cov_matrix, np.eye(1)], axis=0))
    em_distance = np.sqrt(np.dot(np.dot(xMy, se[0][0]), np.transpose(xMy)))
    return em_distance


with Image.open(path + "1.png") as im:
    width, height = im.size

pixels = [[0 for _ in range(12)] for _ in range(width * height)]

for i in range(4):
    image = Image.open(path + str((i + 1)) + ".png")
    img.append([list(elem) for elem in image.getdata()])

for h in range(height):
    for w in range(width):
        for i in range(4):
            pixels[width * h + w][i * 3] = img[i][width * h + w][0]
            pixels[width * h + w][i * 3 + 1] = img[i][width * h + w][1]
            pixels[width * h + w][i * 3 + 2] = img[i][width * h + w][2]

length = len(pixels)

classified_image = Image.new("RGB", (width, height))


def ethalon_dist_calc(ethalon, x, y, i):
    ethalon_distance = euclidean_mahalanobis(pixels[i], ethalon)
    return ethalon_distance if ethalon_distance > 0 else 0.01


def classifying_thread(start, finish):
    ethalons = []
    for e in range(len(config)):
        ethalon = []
        for c in config[e]["ethalons"]:
            ethalon.append(create_ethalon(c[0], c[1], c[2], c[3]))
        ethalons.append(ethalon)
    for i in range(int(start), int(finish)):
        em_distance = []
        pixel_x = i % width + 1
        pixel_y = i // width + 1
        for ethalon in ethalons:
            min_em = []
            for e in ethalon:
                min_em.append(ethalon_dist_calc(e, pixel_x, pixel_y, i))
            em_distance.append(min_em)
        classification = em_distance.index(min(em_distance))
        classified_image.putpixel(
            (pixel_x - 1, pixel_y - 1), tuple(config[classification]["rgb"])
        )
        if i % 5000 == 0:
            classified_image.save(path + "classified.jpg")


classifying_thread(0, length)
classified_image.save(path + "classified.jpg")

print("Execution time: ", round((time.time() - start_time), 2))