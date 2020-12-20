# real-time_equalizer

This work develops an audio equalizer in real time capable of filtering up to 10 frequencies simultaneously. Possible frequencies are 200Hz, 400Hz, 600Hz, 800Hz, 1000Hz, 1200Hz, 1400Hz, 1600Hz, 1800Hz and 2000Hz

An important objective of the work is to design a bandpass filter capable of filtering the audio at the above frequencies. For this, initially, a low-pass filter was created, in which the ideal filter is truncated by the Blackman window. Then, a high-pass filter was also designed, in which the ideal filter is also truncated through the Blackman window. Finally, both filters are converted to obtain a bandpass filter. (see filters.py).

As it is about real-time filtering, the audio was cut into pieces (chunks = 4096) and each piece is filtered at the chosen frequency. After that, the fft is calculated to generate the resulting frequency spectrum and compare it with the frequency spectrum before filtering.
