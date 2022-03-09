import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt


image = skimage.io.imread(fname='encrypted image_AES.png', as_gray=True)
fig, ax = plt.subplots()
# plt.imshow(image, cmap='gray')
# plt.show()
# img1 = cv2.imread('im1.png')
# img2 = cv2.imread('encrypted image_AES.png')
# img3 = cv2.imread('encrypted image_DES.png')
histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
plt.plot(bin_edges[0:-1], histogram)
# plt.hist(img2.ravel(),256,[0,256],alpha=0.5, label="Cipher Image AES")
# plt.hist(img3.ravel(),256,[0,256],alpha=0.5, label="Cipher Image DES")
# plt.legend(loc='upper right')
plt.show()


