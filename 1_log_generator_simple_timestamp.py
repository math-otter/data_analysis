from datetime import datetime, timedelta

# 매크로 로그 생성 함수
def generate_log_macro(n=1000, start_time=datetime.now()): # 기본값: (현재 시점) 포함 (1000)개의 시점을 기록
    time_points = range(0, n)  # 시점 리스트
    log_data = []  # 로그 기록용 리스트
    last_used = {'A': -999, 'B': -999, 'C': -999}  # 각 스킬의 마지막 사용 시간 체크
    cooldown = {'A': 5, 'B': 25, 'C': 70}  # 각 스킬의 쿨다운 시간 체크

    for time_point in time_points:
        current_time = start_time + timedelta(seconds=0.1*time_point) # 시점의 단위는 0.1초
        for skill in ['C', 'B', 'A']:  # C > B > A 순으로 판단
            if time_point - last_used[skill] >= cooldown[skill]:  # 특정 스킬이 사용 가능하면
                log_data.append(f'[{current_time}] {skill} used')  # 스킬 사용 후 해당 스킬 사용 로그를 기록
                last_used[skill] = time_point  # 최종 사용 시점을 현재 시점으로 업데이트
                break  # 스킬을 사용 했으면 다른 스킬을 확인할 필요 없음
        else:
            log_data.append(f'[{current_time}] No action') # 어떤 스킬도 사용하지 못했다면, No action을 기록
    
    return log_data

# 로그 파일 저장
logs = generate_log_macro(600) 
with open('logs.txt', 'w') as file:
    for log in logs:
        file.write(log + '\n')