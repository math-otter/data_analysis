import numpy as np

# f(x): 임의의 제곱 적분 가능 함수
p = 60
x = np.linspace(0, p-1, p)
f = np.cos(2*np.pi*(10/p)*x)
print(f'f(x): {f}\n'+'-'*100)

# C(n): 분석식, 푸리에 계수, 이산 푸리에 변환(DFT)
analysis = np.fft.fft(f) 
print(f'C(n): {analysis}\n'+'-'*100)

# f(x)=Sum[C(n)u(x;n)]: 합성식, 푸리에 급수, 이산 푸리에 역변환(IDFT)
synthesis = np.fft.ifft(analysis)
print(f'f(x)=Sum[C(n)u(x;n)]: {synthesis}\n'+'-'*100)

# 시각화
import matplotlib.pyplot as plt
fig, ax = plt.subplots(3, 1, figsize=(10, 4))

ax[0].plot(x, f)
ax[0].set_yticks([min(f), max(f)])

magnitude = np.abs(analysis)
ax[1].plot(x / p, magnitude)
ax[1].set_yticks([min(magnitude), max(magnitude)])

ax[2].plot(x, synthesis)
ax[2].set_yticks([min(synthesis), max(synthesis)])

plt.tight_layout()
plt.show()