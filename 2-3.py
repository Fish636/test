from thinkdsp import decorate
from thinkdsp import SinSignal
from thinkdsp import SquareSignal
import matplotlib.pyplot as plt

square = SquareSignal(1500).make_wave(duration=0.5, framerate=10000)

square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
square.make_audio()

SinSignal(1100).make_wave(duration=0.5, framerate=10000).make_spectrum().plot()

plt.show()