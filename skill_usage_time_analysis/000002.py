import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd
from tools.log_generator import *
from tools.log_to_csv import log_to_csv
from tools.csv_to_time_series import *

# 데이터 생성 (로그 파일, csv 파일)
user_id = '000002'
log_file_name = r'data/{}_skill_usage_log.txt'.format(user_id)
csv_file_name = r'data/{}_skill_usage_time.csv'.format(user_id)
log_likehuman(log_file_name)
log_to_csv(log_file_name, csv_file_name)

# 데이터 칼럼에 대해 다음 작업 수행
skills = ['A', 'B', 'C', 'D', 'total']
for skill in skills:

    # 이산, 연속 시계열로 변환
    column_name = f'{skill}_used'
    positions, values = time_series_descrete(csv_file_name, column_name)
    range, density = time_series_continuous(csv_file_name, column_name)

    # 시각화
    fig, ax = plt.subplots(2, 1, figsize=(10, 4))
    ax[0].scatter(positions, values)
    ax[0].set_yticks(values)
    ax[1].plot(range, density)
    ax[1].set_yticks([min(density), max(density)])
    plt.tight_layout()
    plt.savefig(r'images/{}_visualization_{}.png'.format(user_id, skill))
