import numpy as np
from imgtoarray import load_images, draw_images
from sklearn.cluster import KMeans

# 데이터 로드
apple = load_images("Training\Apple Red 1") # 492장
banana = load_images("Training\Banana 1") # 490장
cherry = load_images("Training\Cherry 1") # 492장
fruit = np.concatenate((apple, banana, cherry), axis=0) # 1474장

# k평균 군집 알고리즘 모델 생성, 훈련
km = KMeans(n_clusters=3, random_state=42) # 모델 객체 생성
km.fit(fruit.reshape(-1, 100*100)) # 모델 객체 훈련
# 훈련 데이터를 2차원 배열로 전달하기 위한 reshape 사용

# 훈련 결과
result = km.labels_
n_iter = km.n_iter_
print(result)
print(n_iter)

# 군집 중심과 실제 평균을 시각화 하여 비교
centroids = km.cluster_centers_.reshape(3, 100, 100) # 시각화를 위해 다시 100*100 정사각형 형태로 되돌린다.
means = np.array([np.mean(fruit, axis=0) for fruit in [apple, banana, cherry]])
centroids_and_means = np.concatenate((centroids, means), axis=0)
draw_images(centroids_and_means, 
            ncols=3,
            ratio=3, 
            titles=["cent_0", "cent_1", "cent_2", "mean_apple", "mean_banana", "mean_cherry"], 
            axis="on", 
            save=r"Images\3_centroids and means")

# 군집 분석 결과 시각화
draw_images(fruit[km.labels_ == 0], ncols=25, save=r"Images\3_fruit with cent_0")
draw_images(fruit[km.labels_ == 1], ncols=25, save=r"Images\3_fruit with cent_1")
draw_images(fruit[km.labels_ == 2], ncols=25, save=r"Images\3_fruit with cent_2")