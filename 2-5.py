from thinkdsp import decorate
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import SawtoothSignal
import numpy as np
import matplotlib.pyplot as plt

wave = TriangleSignal(freq=440).make_wave(duration=0.5)
wave1 = SawtoothSignal(freq=440).make_wave(duration=0.5)
wave2 = SquareSignal(freq=440).make_wave(duration=0.5)

def filter_spectrum(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

plt.subplot(311)
spectrum = wave.make_spectrum()
spectrum.plot(high=10000, color='gray')
filter_spectrum(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

plt.subplot(312)
spectrum1 = wave1.make_spectrum()
spectrum1.plot(high=10000, color='red')
filter_spectrum(spectrum1)
spectrum1.scale(440)
spectrum1.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

plt.subplot(313)
spectrum2 = wave2.make_spectrum()
spectrum2.plot(high=10000, color='green')
filter_spectrum(spectrum2)
spectrum2.scale(440)
spectrum2.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

filtered = spectrum.make_wave()
filtered.make_audio()
plt.show()