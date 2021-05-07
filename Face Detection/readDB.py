import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np, sys
from skimage import data, color, feature
import skimage.data
import cv2
import os

def load_images_from_folder(folder):
    images = []
    for imgFolder in os.listdir(folder):
        folderName = os.path.join(folder,imgFolder)
        for img in os.listdir(folderName):
            if not img.endswith('.bad'):
                images.append(cv2.imread(os.path.join(folderName,img)))
    return images

images = load_images_from_folder("CroppedYale")
plt.imshow(images[0])
plt.show()
print(images[0])
print(len(images))
