from tools.log_generator import *
from tools.log_analyzer import *

# 유저 아이디와 플레이 로그
user_id = '000001'
logs = log_macro(600*3)
write_log(logs, r'data/{}.txt'.format(user_id))

# 초 단위 시계열 생성
df1 = LogData(logs).per_second() # 이산 시계열
df2 = smoothed(df1, bandwidth=0.5) # 연속 시계열
print(df1)
print('-' * 100)
print(df2)
print('-' * 100)

# PSD 계산 및 시각화
import matplotlib.pyplot as plt

action = 'B used' # 분석 하려는 행위

x = df2[action] # 신호 x(t)
t = df2['time range'] # 시간 t

r = autocorr(x) # 자기상관함수 r(tau)
tau = range(len(x)) # 시차 tau

s = np.abs(np.fft.fft(r)) # 파워 스펙트럼 밀도 s(f) = F[r(tau)]
f = df2.index / len(x) # 주파수 f = t/p

fig, ax = plt.subplots(3, 1)
ax[0].plot(t, x)
ax[1].plot(tau, r)
ax[2].plot(f, s)

plt.show()