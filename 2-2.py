from thinkdsp import decorate
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import SinSignal
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import SawtoothSignal
import numpy as np
import matplotlib.pyplot as plt

sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)
sawtooth.make_audio()

plt.subplot(311)
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

plt.subplot(312)
sawtooth.make_spectrum().plot(color='red')
square = SquareSignal(amp=0.5).make_wave(duration=0.5, framerate=40000)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

plt.subplot(313)
sawtooth.make_spectrum().plot(color='green')
triangle = TriangleSignal(amp=0.79).make_wave(duration=0.5, framerate=40000)
triangle.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

plt.show()