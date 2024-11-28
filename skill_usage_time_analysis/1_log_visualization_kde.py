import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd
from log_generator import macro
from log_to_csv import log_to_csv

log_file_name = '000001_skill_usage_log.txt'
csv_file_name = '000001_skill_usage_time.csv'

macro(log_file_name)
log_to_csv(log_file_name, csv_file_name)

df = pd.read_csv('000001_skill_usage_time.csv')

positions = df.index
range = np.linspace(min(positions), max(positions), 1000)
values = df['total_used'].values

# 커널 밀도 계산 함수
def weighted_kde(positions, range, values, bandwidth=0.5):
    density = np.zeros_like(range)
    for position, value in zip(positions, values):
        density += value * norm.pdf(range, loc=position, scale=bandwidth)  # 값에 비례한 커널 높이
    return density

# 밀도 계산
density = weighted_kde(positions, range, values)

# 시각화
fig, ax = plt.subplots(2, 1, figsize=(10, 4))
ax[0].scatter(positions, values)
ax[0].set_yticks(values)
ax[1].plot(range, density)
plt.tight_layout()
plt.savefig('visualization.png')
