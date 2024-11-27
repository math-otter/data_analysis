import pandas as pd

# 로그 파일 가공
# 로그 기록 예시: [2024-11-27 20:07:50.567268] A used
logs_time = []
logs_action = []
with open('logs.txt', 'r') as log_file:
    for log in log_file:
        time, action = log.split(']')
        time = time.split('.')[0].replace('[', '') # 초 단위로 시간 추출
        action = action.replace('\n', '') # 줄바꿈 제거
        logs_time.append(time)
        logs_action.append(action)

# 스킬 사용 횟수의 합을 초 단위로 집계하여 저장
df = pd.DataFrame()
df['time'] = logs_time
df['action'] = logs_action

skills = ['A', 'B', 'C']
for skill in skills:
    df[f'{skill}_used'] = df['action'].str.contains(skill) # 매 시점에서 스킬 사용 여부 체크
df = df.drop('action', axis=1).groupby('time').sum() # 각 스킬 사용 횟수를 초 단위로 집계
df['total_used'] = df.sum(axis=1) # 스킬 사용 횟수의 합을 초 단위로 집계
df.to_csv('skill_usage_time.csv', index=False) # csv 파일로 저장