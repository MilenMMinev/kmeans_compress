import scipy.misc
# from sklearnself.cluster import KMeans
from kmeans import KMeans

import numpy as np


def compress(image, out_path, n_colors):
    im_arr = scipy.misc.imread(image)
    im_arr = np.array(im_arr, dtype=np.float32)

    pixels = im_arr.reshape(im_arr.shape[0] * im_arr.shape[1], 3)

    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)

    labels = kmeans.predict(pixels)

    w = im_arr.shape[0]
    h = im_arr.shape[1]
    d = im_arr.shape[2]
    assert d == 3

    for x in range(w):
        for y in range(h):
            im_arr[x][y] = kmeans.cluster_centers_[labels[x * h + y]]

    scipy.misc.imsave(out_path, im_arr)
