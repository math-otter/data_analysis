import numpy as np
import pandas as pd
from scipy.stats import norm

# 데이터 프레임에서 이산 시계열 생성
def time_series_descrete(df=pd.DataFrame()):
    positions = df.reset_index(drop=True).index.values
    values = []
    for column in df.columns:
        values.append(df[column].values)
    return positions, values

# 커널 밀도 계산 함수 정의
def weighted_kde(positions, range, values, bandwidth=0.5):
    density = np.zeros_like(range)
    for position, value in zip(positions, values):
        density += value * norm.pdf(range, loc=position, scale=bandwidth)  # 값에 비례한 커널 높이
    return density

# 데이터 프레임에서 커널 밀도를 이용한 연속 시계열 생성
def time_series_continuous(df=pd.DataFrame()):
    positions = df.reset_index(drop=True).index.values
    range = np.linspace(min(positions), max(positions), 1000)
    density = []
    for column in df.columns:
        values = df[column].values
        density.append(weighted_kde(positions, range, values))
    return range, density