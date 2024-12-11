import numpy as np

# 데이터 정의
x = np.array([1, 2, 3])
t = np.arange(0, len(x))  # 시간 t = [0, 1, 2]

# 자기상관함수 계산
def autocorrelation_discrete(x):
    n = len(x)
    lags = np.arange(0, n)  # 가능한 지연 값 τ
    autocorr = []

    for tau in lags:
        # τ 만큼 데이터 이동 후 내적 계산
        numerator = np.sum(x[:n-tau] * x[tau:])
        autocorr.append(numerator)
    
    return lags, autocorr

# 결과 계산
lags, autocorr = autocorrelation_discrete(x)

# 결과 출력
print("Lags (τ):", lags)
print("Autocorrelation R_xx(τ):", autocorr)

import matplotlib.pyplot as plt

# 시각화
plt.figure(figsize=(8, 5))
plt.stem(lags, autocorr, use_line_collection=True)
plt.title("Autocorrelation Function $R_{xx}(\\tau)$")
plt.xlabel("Lag $\\tau$")
plt.ylabel("$R_{xx}(\\tau)$")
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()