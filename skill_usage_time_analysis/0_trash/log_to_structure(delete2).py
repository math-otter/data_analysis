import pandas as pd

class LogData:
    def __init__(self, logs):
        self.logs = logs
        self.df = None  # 데이터프레임 초기화

    # 로그 데이터를 데이터프레임으로 정형화하는 메서드
    def log_to_structure(self):
        logs_time = []  # 시점 기록용 리스트
        logs_action = []  # 행위 기록용 리스트
        for log in self.logs: # 모든 로그에 대해
            time, action = log.split(']')  # 시점과 행위 분리
            time = time.replace('[', '').strip() # 시점 텍스트 정리
            action = action.strip() # 행위 텍스트 정리
            logs_time.append(time)  # 시점 기록
            logs_action.append(action)  # 행위 기록

        # 데이터프레임 생성 및 시간 순 정렬
        self.df = pd.DataFrame({'time': logs_time, 'action': logs_action}) # 데이터 프레임 생성
        self.df['time'] = pd.to_datetime(self.df['time'])  # 시점을 datetime 형식으로 변환
        self.df = self.df.sort_values(by='time').reset_index(drop=True)  # 시간 순 정렬

        # 행위별 발생 여부 기록
        actions = sorted(self.df['action'].unique()) # 행위 추출
        for action in actions: # 모든 행위에 대해
            self.df[f'{action}'] = (self.df['action'] == action).astype(int)  # 발생 여부 기록
        return self.df  # 데이터프레임 반환

    # 1초 간격으로 행위의 발생 횟수를 집계하는 메서드
    def action_per_seconds(self):
        self.df['time'] = self.df['time'].dt.strftime('%Y-%m-%d %H:%M:%S.%f').str[:-7] # 1초 간격으로 시점 추출
        self.df = self.df.drop('action', axis=1).groupby('time').sum().reset_index() # 시점별 집계
        return self.df  # 데이터프레임 반환


