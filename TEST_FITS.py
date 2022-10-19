from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

image_file = get_pkg_data_filename('./fits_tests/M13_blue/M13_blue_0001.fits')

fits.info(image_file)
image_data = fits.getdata(image_file, ext=0)

plt.figure()
plt.imshow(image_data, cmap='gray')
plt.colorbar()  