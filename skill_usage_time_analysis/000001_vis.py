from tools.log_generator import *
from tools.log_analyzer import *

# 유저 아이디와 플레이 로그
user_id = '000001'
logs = log_macro(600)
write_log(logs, r'data/{}.txt'.format(user_id))

# 초 단위 시계열 생성
df1 = LogData(logs).per_second() # 이산 시계열
df2 = smoothed(df1, bandwidth=0.5) # 연속 시계열
print(df1)
print('-' * 100)
print(df2)

# 시각화
import matplotlib.pyplot as plt

actions = df2.drop('time range', axis=1).columns
for action in actions:
    fig, ax = plt.subplots(2, 1, figsize=(10, 4))
    time_points = df1['time points']
    values = df1[action]
    ax[0].scatter(time_points, values)
    ax[0].set_yticks(values)

    time_range = df2['time range']
    density = df2[action]
    ax[1].plot(time_range, density)
    ax[1].set_yticks([min(density), max(density)])

    plt.tight_layout()
    plt.savefig(r'images/{}_{}.png'.format(user_id, action))
    plt.close(fig)