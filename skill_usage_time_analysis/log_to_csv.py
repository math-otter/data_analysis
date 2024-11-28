import pandas as pd

# 로그 파일에서 각 스킬 사용 횟수를 초 단위로 집계하여 정형 데이터로 저장하는 함수
# 로그 기록 예시: [2024-11-27 20:07:50.567268] A used
def log_to_csv(log_file, csv_file):
    # 로그 파일 가공
    logs_time = [] # 시점 기록용 리스트
    logs_action = [] # 행위 기록용 리스트
    with open(log_file, 'r') as logs:
        for log in logs:
            time, action = log.split(']') # 시점과 행위 분리
            time = time.split('.')[0].replace('[', '') # 초 단위로 시점 추출
            action = action.replace('\n', '') # 줄바꿈 제거
            logs_time.append(time) # 시점 기록
            logs_action.append(action) # 행위 기록

    # 스킬 사용 횟수의 합을 초 단위로 집계하여 저장
    df = pd.DataFrame() # 데이터 프레임 생성
    df['time'] = logs_time # 시점 열
    df['action'] = logs_action # 행위 열

    skills = ['A', 'B', 'C']
    for skill in skills:
        df[f'{skill}_used'] = df['action'].str.contains(skill) # 매 시점에서 스킬 사용 여부 체크
    df = df.drop('action', axis=1).groupby('time').sum() # 각 스킬 사용 횟수를 초 단위로 집계
    df['total_used'] = df.sum(axis=1) # 스킬 사용 횟수의 합을 초 단위로 집계
    df.to_csv(csv_file, index=False) # csv 파일로 저장