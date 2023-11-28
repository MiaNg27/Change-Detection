from glob import glob


import spectral
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio as rasterio

import rasterio as rio
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import ListedColormap


np.seterr(divide='ignore', invalid='ignore')

bands = glob("imgs_1/*B??*.tif")
bands2 = glob("imgs_2/*B??*.tif")
bands.sort()
bands2.sort()

a = []

for i in bands :
    with rio.open(i,'r') as b:
        print(b.shape)
        a.append(b.read(1))

print("band2")
for i in bands2 :
    with rio.open(i,'r') as b:
        print(type(b))
        a.append(b.read(1))

#find max shape, use np.pad to change all shapes
for i in a:
    i.resize((799,799),refcheck=False)
stack = np.stack(a)
ep.plot_bands(stack,
              cmap = 'gist_earth',
              figsize = (20, 12),
              cols = 6,
              cbar = False)
plt.show()

colors = ['tomato', 'navy', 'MediumSpringGreen', 'lightblue', 'orange', 'blue',
          'maroon', 'purple','brown','maroon', 'purple','brown','navy','tomato', 'navy', 'MediumSpringGreen', 'lightblue', 'orange', 'blue',
          'maroon', 'purple','brown','maroon', 'purple','brown','navy']

ep.hist(stack,
        colors = colors,
        title=[f'Band-{i}' for i in range(1, 27)],
        cols=3,
        alpha=0.5,
        figsize = (12, 10))

plt.show()

