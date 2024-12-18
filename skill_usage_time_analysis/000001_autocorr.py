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

action = 'No action' # 분석 하려는 행위

index = df2.index # 인덱스: 0, 1, ..., N-1
x = df2[action] # 신호
r = autocorr(x) # 자기상관함수
s = np.fft.fft(r) # 파워 스펙트럼 밀도(PSD)

fig, ax = plt.subplots(3, 1)

ax[0].plot(index, x) # 신호 그래프
ax[1].plot(index, r) # 자기상관함수 그래프
ax[2].plot(index, np.abs(s)) # PSD 그래프

plt.tight_layout()
plt.show()
