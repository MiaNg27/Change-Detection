# Change-Detection

Overview
This repository contains Python code for satellite image change detection using raster data. The code utilizes libraries such as rasterio, spectral, earthpy, and matplotlib to perform tasks such as loading, processing, and visualizing satellite images. The primary goal is to identify changes in the landscape over time by comparing different sets of satellite images.

Requirements
Python 3.x
Required Python libraries: rasterio, spectral, earthpy, matplotlib, numpy
Installation
You can install the required libraries using the following command:


```pip install rasterio spectral earthpy matplotlib numpy```

Usage
Clone the repository:


```git clone https://github.com/yourusername/satellite-change-detection.git```
```cd satellite-change-detection```

Organize your satellite image data:

Place images for the first timestamp in the "imgs_1" directory.
Place images for the second timestamp in the "imgs_2" directory.
Run the change detection script:


```python change_detection_script.py```
This script reads satellite images from the specified directories, processes the data, and generates visualizations to identify changes.

Code Explanation
The provided Python script (change_detection_script.py) performs the following steps:

Loading Data:

Reads satellite images from the specified directories (imgs_1 and imgs_2).
Prints the shape of each image.
Resizing Images:

Resizes images to a common shape using np.pad.
Visualization:

Plots the bands of the stacked images using earthpy.plot_bands.
Displays a histogram for each band using earthpy.hist.
Results
The script generates visualizations that can be used to analyze changes in the landscape between the two timestamps. The band plots provide a visual representation, while the histograms offer insights into the distribution of pixel values for each band.

Customization
Feel free to customize the script according to your specific project requirements. You may adjust colormap, image directory paths, or add additional processing steps as needed.

License
This project is licensed under the MIT License.
