import numpy as np
import pandas as pd
from scipy.stats import norm

class LogData:

    # 객체 호출시 초기화 메서드
    def __init__(self, logs):
        self.logs = logs
        self.df = None
        self.is_structured = False

    # 로그 데이터 정형화 메서드
    def structured(self):
        if not self.is_structured:
            
            # 로그 데이터 정형화 (형식: ['[2024-11-27 20:07:50.5] 특정 행위', ...])
            times, actions = zip(*(log.split(']') for log in self.logs)) # 시점 튜플과 행위 튜플로 분리
            times = [time.replace('[', '').strip() for time in times] # 가공된 시점 리스트
            actions = [action.strip() for action in actions] # 가공된 행위 리스트
            self.df = pd.DataFrame({'time': times, 'action': actions}) # 시점, 행위 데이터 프레임 생성
            self.df['time'] = pd.to_datetime(self.df['time']) # 시점 열을 datetime 객체로 변환
            self.df = self.df.sort_values(by='time').reset_index(drop=True) # 시간 순 정렬

            # 행위별 발생 여부 기록
            actions = sorted(self.df['action'].unique()) # 로그에 포함된 행위들을 추출하여 정렬
            for action in actions:
                self.df[action] = (self.df['action'] == action).astype(int) # 매 시점에서 각 행위의 발생 여부 체크
            
            # 정형화 완료
            self.is_structured = True

        return self.df # 데이터프레임 반환

    # 1초 간격으로 각 행위의 빈도를 집계하는 메서드 (이산 시계열 생성)
    def per_second(self):
        if not self.is_structured: # 정형화되지 않았다면
            self.structured() # 자동으로 정형화
            self.is_structured = True # 정형화 완료
        
        self.df['time'] = self.df['time'].dt.strftime('%Y-%m-%d %H:%M:%S') # 초 단위만 남기기
        self.df = self.df.drop('action', axis=1).groupby('time').sum().reset_index() # 초 단위로 집계
        self.df.insert(1, 'time points', range(len(self.df))) # 시점 설정
        
        return self.df  # 데이터프레임 반환

###################################################################################################################

# 커널 밀도 함수
def kde(positions, range, values, bandwidth=0.5):
    density = np.zeros_like(range)
    for position, value in zip(positions, values):
        density += value * norm.pdf(range, loc=position, scale=bandwidth)  # 값에 비례한 커널 높이
    return density

# 이산 시계열을 부드럽게 변환하는 함수 (커널 밀도를 이용하여 연속 시계열 생성)
def smoothed(df=pd.DataFrame(), bandwidth=0.5, n=10):
    time_points = df.reset_index(drop=True).index.values
    time_range = np.linspace(min(time_points), max(time_points), n*len(df))
    series = {}
    columns_to_exclude = ['time', 'time points']
    valid_columns = [col for col in df.columns if col not in columns_to_exclude]
    for column in valid_columns:
        values = df[column].values
        series[column] = kde(time_points, time_range, values, bandwidth)
    df = pd.DataFrame(series)
    df.insert(0, 'time range', time_range)
    return df

# 자기상관함수
def autocorr(x):
    n = len(x)
    return [np.sum(x[:n - tau] * x[tau:]) for tau in range(n)]