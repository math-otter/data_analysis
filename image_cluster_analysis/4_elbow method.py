import numpy as np
from imgtoarray import load_images
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 데이터 로드
apple = load_images("Training\Apple Red 1") # 492장
banana = load_images("Training\Banana 1") # 490장
cherry = load_images("Training\Cherry 1") # 492장
fruit = np.concatenate((apple, banana, cherry), axis=0) # 1474장

# k의 변화에 따른 이너셔 그래프
inertia = []
k_range = range(2,7)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42) # 모델 객체 생성
    km.fit(fruit.reshape(-1, 100*100)) # 모델 객체 훈련
    inertia.append(km.inertia_ / 1000)

plt.plot(k_range, inertia)
plt.xlabel("k")
plt.ylabel("inertia / 1000")
plt.xticks(k_range)
plt.savefig(r"Images\4_elbow method")