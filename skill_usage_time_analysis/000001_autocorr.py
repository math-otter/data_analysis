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

# 자기상관함수 계산 및 시각화
import matplotlib.pyplot as plt

action = 'B used'
x = df1[action]
t = df1['time points']

r = autocorr(x)
tau = range(len(x))

fig, ax = plt.subplots(2, 1)
ax[0].plot(t, x)
ax[1].plot(tau, r)

plt.show()