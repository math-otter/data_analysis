import numpy as np
import matplotlib.pyplot as plt

# 심박수 데이터
data = np.array([72, 75, 80, 85, 90, 85, 80, 75, 72, 70, 72])

# 지연 임베딩 함수
def delay_embedding(data, delay, dim):
    n = len(data)
    return np.array([data[i:n-(dim-1)*delay+i:delay] for i in range(dim)]).T

# 2차원 임베딩 적용
embedded_data = delay_embedding(data, delay=1, dim=2)

# 시각화
plt.figure(figsize=(6, 6))
plt.scatter(embedded_data[:, 0], embedded_data[:, 1], label="Embedded Points")
plt.plot(embedded_data[:, 0], embedded_data[:, 1], linestyle="--", color="blue", label="Trajectory")
plt.title("2D Embedded Heartbeat Data")
plt.xlabel("Current Heartbeat (x_t)")
plt.ylabel("Previous Heartbeat (x_{t-1})")
plt.legend()
plt.show()
