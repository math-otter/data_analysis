from datetime import datetime, timedelta
import os

# 1. 로그 파일 쓰기 함수
def write_log(logs, file_path):
    directory = os.path.dirname(file_path)
    if directory: # 디렉터리가 ''인 경우만 실행
        os.makedirs(directory, exist_ok=True)
    with open(file_path, 'w') as file:
        for log in logs:
            file.write(log + '\n')

# 2. 로그 생성 함수

# 매크로 로그
def log_macro(n=600): # 기본값: 시작 시점 포함 (600)개의 시점을 기록
    
    # 설정
    start_time= "2024-09-19 00:00:00.0"
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")
    time_points = range(0, n)  # 시점 리스트
    logs = []  # 로그 기록용 리스트
    cooldown = {'A': 5, 'B': 25, 'C': 70}  # 각 스킬의 쿨다운 시간

    # 행동 메커니즘
    last_used = {'A': -999, 'B': -999, 'C': -999}  # 각 스킬의 마지막 사용 시간 체크
    for time_point in time_points: # 모든 시점에서 이하 과정 반복
        current_time = start_time + timedelta(seconds=0.1*time_point) # 시점의 단위는 0.1초
        current_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-5] # 0.1초 단위로 포맷
        for skill in ['C', 'B', 'A']:  # 스킬의 성능이 좋은 C > B > A 순으로 판단
            if time_point - last_used[skill] >= cooldown[skill]:  # 특정 스킬이 사용 가능하면
                logs.append(f'[{current_time}] {skill} used')  # 스킬 사용 후 해당 스킬 사용 로그를 기록
                last_used[skill] = time_point  # 최종 사용 시점을 현재 시점으로 업데이트
                break  # 스킬을 하나라도 사용 했으면 다른 스킬을 확인할 필요 없음
        else:
            logs.append(f'[{current_time}] No action') # 어떤 스킬도 사용하지 못했다면, No action을 기록
    
    return logs