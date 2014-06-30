import numpy as np
from pylab import * 
x = np.random.rand(100) # create 100 random numbers of which we want the fourier transform
x = ([(-1.)**(i/4) for i in range(1,100)]) # make sure the average is zero, so we don't get a huge DC offset.
dt = 1 #[s] 1/the sampling rate
fftx = np.fft.fft(x) # the frequency transformed part
# now discard anything  that we do not need..
fftx = fftx[range(int(len(fftx)/2))]
# now create the frequency axis: it runs from 0 to the sampling rate /2
freq_fftx = np.linspace(0,2/dt,len(fftx))
# and plot a power spectrum
plot(freq_fftx,abs(fftx)**2)
show()