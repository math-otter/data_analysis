import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd
from tools.log_generator import *
from tools.log_to_csv import log_to_csv

# 데이터 생성
log_file_name = r'data/000001_skill_usage_log.txt'
csv_file_name = r'data/000001_skill_usage_time.csv'
macro(log_file_name)
log_to_csv(log_file_name, csv_file_name)
df = pd.read_csv(csv_file_name)

# 커널 밀도 계산 함수 정의
def weighted_kde(positions, range, values, bandwidth=0.5):
    density = np.zeros_like(range)
    for position, value in zip(positions, values):
        density += value * norm.pdf(range, loc=position, scale=bandwidth)  # 값에 비례한 커널 높이
    return density

# 생성된 데이터로 밀도 계산, 시각화
skills = ['A', 'B', 'C', 'D', 'total']
for skill in skills:
    positions = df.index
    range = np.linspace(min(positions), max(positions), 1000)
    values = df[f'{skill}_used'].values
    density = weighted_kde(positions, range, values)
    fig, ax = plt.subplots(2, 1, figsize=(10, 4))
    ax[0].scatter(positions, values)
    ax[0].set_yticks(values)
    ax[1].plot(range, density)
    ax[1].set_yticks([min(density), max(density)])
    plt.tight_layout()
    plt.savefig(r'images/1_visualization_macro_{}.png'.format(skill))
