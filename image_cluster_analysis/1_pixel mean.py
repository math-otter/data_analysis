import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from imgtoarray import load_images, draw_images

# 데이터 로드
apple = load_images("Training\Apple Red 1") # 492장
banana = load_images("Training\Banana 1") # 490장
cherry = load_images("Training\Cherry 1") # 492장

# 각 과일 이미지들의 픽셀 평균 계산
apple_means = np.mean(apple, axis=(1, 2))
banana_means = np.mean(banana, axis=(1, 2))
cherry_means = np.mean(cherry, axis=(1, 2))
# print(len(apple_means), len(banana_means), len(cherry_means)): 이미지 수가 달라서 배열 길이가 안 맞는 것을 확인

# 배열 길이 조정 작업
max_length = max(len(apple_means), len(banana_means), len(cherry_means))
apple_means = np.concatenate((apple_means, [np.nan] * (max_length - len(apple_means))), axis=0)
banana_means = np.concatenate((banana_means, [np.nan] * (max_length - len(banana_means))), axis=0)
cherry_means = np.concatenate((cherry_means, [np.nan] * (max_length - len(cherry_means))), axis=0)
# print(len(apple_means), len(banana_means), len(cherry_means)): 배열 길이가 맞는 것을 확인

# 데이터 프레임 생성 작업
fruit_names = ["apple", "banana", "cherry"]
fruit_means = [apple_means, banana_means, cherry_means]
dic = {} # 데이터 프레임 생성을 위한 빈 딕셔너리
for name, mean in zip(fruit_names, fruit_means):
    dic[f"{name}_means"] = mean
df = pd.DataFrame(dic)
# print(df.tail()): banana의 배열 길이가 짧았고, 빈 부분은 결측치 처리했음을 확인

# 분포 시각화(히스토그램)
for column in df.columns:
  plt.hist(df[column], label=column, alpha=0.8)
plt.ylabel("frequency")
plt.legend()
plt.savefig(r"Images\1_pixel mean histogram")
# 픽셀의 평균값 만으로 바나나를 구별해낼 수 있음을 확인.
# 사과와 체리는 비슷하여 분포에서 겹치는 부분이 존재함.

# 픽셀의 평균값 범위를 이용하여 모든 이미지에서 바나나만 골라내기
fruit = np.concatenate((apple, banana, cherry), axis=0)
mean = np.mean(fruit, axis=(1, 2))
inf, sup = df["banana_means"].min(), df["banana_means"].max()
banana1 = fruit[(mean >= inf) & (mean <= sup)]
draw_images(banana1, ncols=50, save=r"Images\1_banana1")
