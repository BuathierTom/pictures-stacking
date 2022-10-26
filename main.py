import numpy as np
import matplotlib.pyplot as plt
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

def moyenne():

    hdu_img1 = fits.open('./fits_tests/mini/mini0.fits')
    hdu_img1.info()
    image_data1 = hdu_img1[0].data #type: ignore
    hdu_img1.close()

    hdu_img2 = fits.open('./fits_tests/mini/mini1.fits')
    hdu_img2.info()
    image_data2 = hdu_img2[0].data #type: ignore
    hdu_img2.close()


    image_list = [image_data1, image_data2]


    final_image = np.zeros(shape=image_list[0].shape)
    for image in image_list:
        final_image += image
        

    plt.imshow(final_image)
    plt.colorbar()
    plt.show(block=True)
    
if __name__ == '__main__':