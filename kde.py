import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 데이터 포인트
x_i = 5  # 특정 데이터 포인트
h = 2.0  # 밴드위스

# x 축 범위
x = np.linspace(0, 10, 500)

# 커널 함수 계산
kernel = norm.pdf((x - x_i) / h) / h

# 시각화
plt.plot(x, kernel, label=f'Kernel centered at x_i={x_i}')
plt.axvline(x=x_i, color='red', linestyle='--', label='Data Point x_i')
plt.title("Kernel Function Centered at x_i")
plt.legend()
plt.show()
