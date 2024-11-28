import numpy as np
from scipy.stats import norm

# 커널 밀도 계산 함수 정의
def weighted_kde(positions, range, values, bandwidth=0.5):
    density = np.zeros_like(range)
    for position, value in zip(positions, values):
        density += value * norm.pdf(range, loc=position, scale=bandwidth)  # 값에 비례한 커널 높이
    return density