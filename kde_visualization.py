import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

# 이진화된 스킬 사용 시각 (초 단위)
skill_usage_times = np.array([623, 635, 370, 775]).reshape(-1, 1)  # 2D 배열로 변환
time_length = 3600  # 1시간 (3600초)

# 이진화된 배열 생성 (0과 1로만 이루어진 배열)
skill_usage = np.zeros(time_length)
skill_usage[623] = 1
skill_usage[635] = 1
skill_usage[370] = 1
skill_usage[775] = 1

# 이진화된 데이터 (막대 그래프) 시각화
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.plot(skill_usage, label="Binarized Data", drawstyle='steps-post')
plt.title("Binarized Data (Step Graph)")
plt.xlabel("Time (seconds)")
plt.ylabel("Skill Usage (0 or 1)")
plt.legend()

# KDE 적용하여 부드러운 곡선으로 변환
kde = KernelDensity(kernel='gaussian', bandwidth=30).fit(skill_usage_times)

# 밀도 추정값 계산
x = np.linspace(0, 3600, 3600).reshape(-1, 1)
log_dens = kde.score_samples(x)

# KDE 결과 시각화
plt.subplot(1, 2, 2)
plt.plot(x, np.exp(log_dens), label="KDE Smoothed Curve", color='r')
plt.title("KDE Smoothed Curve")
plt.xlabel("Time (seconds)")
plt.ylabel("Density")
plt.legend()

plt.tight_layout()
plt.show()
