from tools.log_generator import *
from tools.log_analyzer import *
import matplotlib.pyplot as plt

# 유저 아이디와 플레이 로그
user_id = '000001'
logs = log_macro()
write_log(logs, r'data/{}.txt'.format(user_id))

# 시계열 생성
df = LogData(logs).freq_per_seconds() # 초 단위로 행위 빈도 집계
df = df.drop('time', axis=1)
time_points, values = time_desc(df)
time_range, density = time_cont(df)

# 시각화
action = 'C used'
fig, ax = plt.subplots(2, 1, figsize=(10, 4))
ax[0].scatter(time_points, values[action])
ax[0].set_yticks(values[action])
ax[1].plot(time_range, density[action])
ax[1].set_yticks([min(density[action]), max(density[action])])
plt.tight_layout()
plt.savefig(r'images/{}_visualization_{}.png'.format(user_id, action))
