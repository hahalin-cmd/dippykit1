import dippykit as dip
import numpy as np
X = dip.im_read("images/cameraman.tif")
X = dip.im_to_float(X)
X *=255
Y = X + 75
Y = dip.float_to_im(Y/255)
dip.im_write(Y,"cameraman_add.tif")
Z = X**2
Z = dip.float_to_im(Z/255)
dip.im_write(Z,"cameraman_square.tif")

fX = dip.fft2(X)
fX = dip.fftshift(fX)
fX = np.log(np.abs(fX))
dip.imshow(fX)
dip.show()


