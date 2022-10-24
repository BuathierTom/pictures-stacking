import numpy as np
import matplotlib.pyplot as plt
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

from astropy.io import fits
image_file = get_pkg_data_filename('./fits_tests/simple/fill0.fits')

hdu_list = fits.open(image_file)
hdu_list.info()
image_data = hdu_list[0].data #type: ignore
print(type(image_data))
print(image_data.shape)
hdu_list.close()


image_data = fits.getdata(image_file)
print(type(image_data)) # Show the Python type for image_data
print(image_data.shape) #type: ignore
plt.imshow(image_data, cmap='gray') #type: ignore
plt.colorbar()
plt.show(block=True)
