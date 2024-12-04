from tools.log_generator import *
from tools.log_analyzer import *

# 유저 아이디와 플레이 로그
user_id = '000001'
logs = log_macro(1200)
write_log(logs, r'data/{}.txt'.format(user_id))

# 초 단위 시계열 생성
df1 = LogData(logs).per_second() # 이산 시계열
df2 = smoothed(df1, bandwidth=0.5) # 연속 시계열
print(df1)
print('-' * 100)
print(df2)
print('-' * 100)

# 푸리에 변환
f = df2['No action']
analysis = np.fft.fft(f) # 푸리에 계수
magnitude = np.abs(analysis) # 푸리에 계수의 크기

# 시각화
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 1, figsize=(10, 4))
time_range = df2['time range']

ax[0].plot(time_range, f)
ax[0].set_yticks([min(f), max(f)])

effective = time_range < 20
time_range = time_range[effective]
magnitude = magnitude[effective]
ax[1].plot(time_range, magnitude)
ax[1].set_yticks([min(magnitude), max(magnitude)])

plt.show()
