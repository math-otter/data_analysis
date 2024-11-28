from datetime import datetime, timedelta
import random

# 매크로 로그 생성 함수
def macro(title, n=600, start_time=datetime.now()): # 기본값: (현재 시점) 포함 (600)개의 시점을 기록
    time_points = range(0, n)  # 시점 리스트
    logs = []  # 로그 기록용 리스트
    last_used = {'A': -999, 'B': -999, 'C': -999}  # 각 스킬의 마지막 사용 시간 체크
    cooldown = {'A': 5, 'B': 25, 'C': 70}  # 각 스킬의 쿨다운 시간 체크

    for time_point in time_points:
        current_time = start_time + timedelta(seconds=0.1*time_point) # 시점의 단위는 0.1초
        for skill in ['C', 'B', 'A']:  # 스킬의 성능이 좋은 C > B > A 순으로 판단
            if time_point - last_used[skill] >= cooldown[skill]:  # 특정 스킬이 사용 가능하면
                logs.append(f'[{current_time}] {skill} used')  # 스킬 사용 후 해당 스킬 사용 로그를 기록
                last_used[skill] = time_point  # 최종 사용 시점을 현재 시점으로 업데이트
                break  # 스킬을 하나라도 사용 했으면 다른 스킬을 확인할 필요 없음
        else:
            logs.append(f'[{current_time}] No action') # 어떤 스킬도 사용하지 못했다면, No action을 기록
    
    with open(title, 'w') as file:
        for log in logs:
            file.write(log + '\n')

# 인간 로그 생성 함수 (노이즈 삽입)
def human(title, n=600, start_time=datetime.now()):  # 기본값: (현재 시점) 포함 600개의 시점을 기록
    time_points = range(0, n)  # 시점 리스트
    logs = []  # 로그 기록용 리스트
    last_used = {'A': -999, 'B': -999, 'C': -999, 'D': -999}  # 각 스킬의 마지막 사용 시간 체크
    cooldown = {'A': 5, 'B': 25, 'C': 70, 'D': 10}  # 각 스킬의 쿨다운 시간
    randomness = {'A': 8, 'B': 30, 'C': 100, 'D': 15}  # 각 스킬에 추가되는 랜덤 지연 (상한)
    
    for time_point in time_points:
        current_time = start_time + timedelta(seconds=0.1 * time_point)  # 시점 단위는 0.1초
        
        for skill in random.sample(['A', 'B', 'C'], k=3):  # 무작위 우선순위로 스킬 확인
            effective_cooldown = cooldown[skill] + random.randint(0, randomness[skill])  # 유효 쿨다운 = 쿨다운 + 랜덤 지연
            if time_point - last_used[skill] >= effective_cooldown:  # 특정 스킬이 사용 가능하면
                logs.append(f'[{current_time}] {skill} used')  # 스킬 사용 로그 기록
                last_used[skill] = time_point  # 최종 사용 시점을 현재 시점으로 업데이트
                break  # 스킬을 하나라도 사용했다면 다른 스킬은 확인하지 않음
        else: # A, B, C 스킬 중 하나도 사용하지 못했다면, D 스킬 사용을 시도
            if time_point - last_used['D'] >= effective_cooldown:
                logs.append(f'[{current_time}] D used')  # 스킬 사용 로그 기록
            else:
                logs.append(f'[{current_time}] No action') # 어떤 스킬도 사용하지 못했다면, No action을 기록
    
    # 로그를 파일에 저장
    with open(title, 'w') as file:
        for log in logs:
            file.write(log + '\n')
