import matplotlib.pyplot as plt
from thinkdsp import read_wave
from IPython.display import display

wave3 = read_wave(r'E:\170255__dublie__trumpet.wav')
wave3.normalize()
display(data=wave3.ys, rate=wave3.framerate)
wave3.make_audio()

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave3, 0.1)
wave3.make_audio()
wave3.plot()

wave3.write(filename='output1-4.wav')
plt.show()