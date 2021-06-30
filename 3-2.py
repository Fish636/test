import os  
import  matplotlib.pyplot as plt
import numpy as np
from thinkdsp import decorate
from thinkdsp import Chirp
from thinkdsp import normalize,unbias

PI2 = 2 * np.pi

class SawtoothChirp(Chirp):   
    def evaluate(self, ts):
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys

signal = SawtoothChirp(start = 220,end =440)   
wave = signal.make_wave(duration = 1,framerate=10000)  
wave.apodize()
wave.make_audio()
sp=wave.make_spectrogram(512).plot(high= 5000)
decorate(xlabel = 'Time(s)',ylabel = 'Frequency(HZ)')
wave.plot()
spect = signal.make_wave()  
spect.write('output1.wav')    
plt.show()