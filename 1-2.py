import matplotlib.pyplot as plt
from thinkdsp import read_wave

wave = read_wave(r'E:\170255__dublie__trumpet.wav')
wave.normalize()
wave.make_audio()
plt.subplot(331)
wave.plot()

segment = wave.segment(start=1.1, duration=0.3)
segment.make_audio()
plt.subplot(332)
segment.plot()
plt.subplot(333)
segment.segment(start=1.1, duration=0.005).plot()


spectrum = segment.make_spectrum()
plt.subplot(334)
spectrum.plot(high=1000)

spectrum.low_pass(1000)
plt.subplot(335)
spectrum.plot(high=10000)
spectrum.high_pass(1000)
plt.subplot(336)
spectrum.plot(high=10000)
spectrum.band_stop(1000,5000)
spectrum.make_wave().make_audio()
plt.subplot(337)
spectrum.plot(high=10000)

wave.write('output1-2.wav')
#play_wave('output1-2.wav', player='')
plt.show()

