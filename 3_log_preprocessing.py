import pandas as pd

logs_time = []
logs_action = []
with open('logs.txt', 'r') as log_file:
    for log in log_file:
        time, action = log.split(']')
        time = time.split('.')[0].replace('[', '')
        action = action.replace('\n', '')
        logs_time.append(time)
        logs_action.append(action)

df = pd.DataFrame()
df['time'] = logs_time
df['action'] = logs_action

skills = ['A', 'B', 'C']
for skill in skills:
    df[f'{skill}_used'] = df['action'].str.contains(skill)
df = df.drop('action', axis=1).groupby('time').sum()
df['total_used'] = df.sum(axis=1)

df.to_csv('skill_usage_time.csv', index=False)