import numpy as np
import matplotlib.pyplot as plt

# 1. 신호 생성
t = np.linspace(0, 2 * np.pi, 1000)  # 시간 축: 0 ~ 2π, 샘플 개수 1000개
s = 0.3 * np.sin(t) + 0.7 * np.sin(2 * t)  # s(t) = 0.3sin(x) + 0.7sin(2x)

# 2. 푸리에 변환
fft_result = np.fft.fft(s)  # 푸리에 변환
print(fft_result)