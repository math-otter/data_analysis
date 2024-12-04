import numpy as np

# f(x): 임의의 제곱 적분 가능 함수
f = np.array([3,4,5,6]) 
print(f'f(x): {f}\n'+'-'*100)

# C(n): 분석식, 푸리에 계수, 이산 푸리에 변환(DFT)
analysis = np.fft.fft(f) 
print(f'C(n): {analysis}\n'+'-'*100)

# f(x)=Sum[C(n)u(x;n)]: 합성식, 푸리에 급수, 이산 푸리에 역변환(IDFT)
synthesis = np.fft.ifft(analysis) 
print(f'f(x)=Sum[C(n)u(x;n)]: {synthesis}\n'+'-'*100)