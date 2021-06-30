import  matplotlib.pyplot as plt
from thinkdsp import read_wave
from thinkdsp import decorate

wave = read_wave(r'C:\Users\Alan\Desktop\4456\72475__rockwehrmann__glissup02.wav')
wave.normalize() #归一化
wave.make_audio()
#读取音频文件
wave.make_spectrogram(512).plot(high= 5000)
decorate(xlabel = 'Time(s)',ylabel = 'Frequency(HZ)')
wave.plot()   
plt.show()