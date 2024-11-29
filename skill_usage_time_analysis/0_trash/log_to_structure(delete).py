import pandas as pd

# 로그 데이터를 데이터 프레임으로 정형화하는 함수
# e.g. [2024-11-27 20:07:50.5] A used
def log_to_structure(logs):
    
    # 로그 데이터 가공
    logs_time = [] # 시점 기록용 리스트
    logs_action = [] # 행위 기록용 리스트
    for log in logs:
        time, action = log.split(']') # 시점과 행위 분리
        time = time.replace('[', '')
        action = action.strip()
        logs_time.append(time) # 시점 기록
        logs_action.append(action) # 행위 기록

    # 데이터 프레임으로 정형화
    df = pd.DataFrame({'time': logs_time, 'action': logs_action}) # 데이터 프레임 생성
    df['time'] = pd.to_datetime(df['time'])  # 시점을 datetime 형식으로 변환
    df = df.sort_values(by='time').reset_index(drop=True)  # 로그를 시간 순으로 정렬
    actions = sorted(df['action'].unique()) # 모든 종류의 행위 추출
    for action in actions: # 모든 종류의 행위에 대해
        df[f'{action}'] = (df['action'] == action) # 매 시점에서 행위의 발생 여부 기록

    return df

# 정형화된 데이터 프레임에서 1초 간격으로 행위의 발생 횟수를 집계하는 함수
def action_per_seconds(df):
    df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S.%f').str[:-7]
    df = df.drop('action', axis=1).groupby('time').sum().reset_index()
    return df