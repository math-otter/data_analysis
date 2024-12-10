import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# 1. 가상 데이터 생성 (스킬 사용 빈도)
# 예: 특정 스킬이 사용된 횟수를 1초 단위로 기록
np.random.seed(42)
time = np.arange(0, 600)  # 600초 데이터
skill_usage = np.random.poisson(2, size=600)  # 랜덤한 스킬 사용 빈도 생성

# 2. 파워 스펙트럼 밀도 계산
# `welch` 메서드는 윈도우를 적용하여 PSD를 계산
freqs, psd = welch(skill_usage, fs=1, nperseg=256)  # fs=1Hz(1초 단위)

# 3. PSD 시각화
plt.figure(figsize=(10, 6))
plt.semilogy(freqs, psd)  # y축 로그 스케일로 변환
plt.title("Power Spectral Density (PSD)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power/Frequency (dB/Hz)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
