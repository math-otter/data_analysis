import random

random.seed = 42 # 랜덤 시드 설정

# 매크로 로그 생성 함수 (기본값: 1000개의 시점을 기록)
def generate_log_macro(t=1000):
    time_points = range(1, t + 1) # 시점 리스트
    log_data = []  # 로그 기록용 리스트
    last_used = {"A": -999, "B": -999, "C": -999}  # 각 스킬의 마지막 사용 시간 체크
    cooldown = {"A": 5, "B": 25, "C": 70}  # 각 스킬의 쿨다운 시간 체크
    
    for time_point in time_points:
        for skill in ["C", "B", "A"]:  # C > B > A 우선 순위
            if time_point - last_used[skill] >= cooldown[skill]:
                log_data.append(f"[{time_point}] {skill} used") # 스킬 사용 후 로그 기록
                last_used[skill] = time_point  # 최종 사용 시점을 현재 시점으로 업데이트
                break  # 쿨다운이 된 스킬을 사용하면 다음 루프로 이동
            else:
                # 사용 가능한 스킬이 없을 때
                log_data.append(f"[{time_point}] No action")
    return log_data

for log in generate_log_macro(100):
    print(log)