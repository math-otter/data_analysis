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
print('-' * 100)


arr = np.arange(5)
print(arr)
print('-' * 100)
fft_result = np.fft.fft(np.arange(5))
print(fft_result)