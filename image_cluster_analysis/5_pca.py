import numpy as np
from imgtoarray import load_images, draw_images
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 데이터 로드
apple = load_images("Training/Apple Red 1")  # 492장
banana = load_images("Training/Banana 1")    # 490장
cherry = load_images("Training/Cherry 1")    # 492장
fruit = np.concatenate((apple, banana, cherry), axis=0)  # 1474장

# 주성분 분석
pca = PCA(n_components=10)
pca.fit(fruit.reshape(-1, 100*100))

# 각 주성분의 설명력과 누적 설명력을 계산
evr = pca.explained_variance_ratio_
evr_cum = np.cumsum(evr)
for i, j in zip(evr, evr_cum):
    print(round(i, 2), round(j, 2))

# Scree Plot과 누적 Scree Plot
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Scree Plot
ax[0].plot(np.arange(1, len(evr) + 1), evr, marker="o", linestyle="--", color="red")
ax[0].set_title("Scree Plot")
ax[0].set_xlabel("Principal Component")
ax[0].set_ylabel("Explained Variance Ratio")
ax[0].set_xticks(np.arange(1, len(evr) + 1))
ax[0].set_yticks(evr)
ax[0].set_yticklabels([f"{y:.2f}" for y in evr])
ax[0].grid(True)

# 누적 Scree Plot
ax[1].plot(np.arange(1, len(evr_cum) + 1), evr_cum, marker="o", linestyle="--", color="blue")
ax[1].set_title("Cumulative Scree Plot")
ax[1].set_xlabel("Principal Component")
ax[1].set_ylabel("Cumulative Explained Variance")
ax[1].set_xticks(np.arange(1, len(evr_cum) + 1))
ax[1].set_yticks(evr_cum)
ax[1].set_yticklabels([f"{y:.2f}" for y in evr_cum])
ax[1].grid(True)

# 서브플롯 간의 간격만 늘리고 좌우 여백 제거
plt.subplots_adjust(left=0.05, right=0.95, wspace=0.4)  # 좌우 여백을 줄이고, 서브플롯 간 간격을 조정

# 그래프 저장
plt.savefig(r"Images/5_scree plot.png")

# 주성분 시각화
draw_images(pca.components_.reshape(-1, 100, 100), 
            ncols=5, 
            ratio=2,
            titles=[f"pc{n + 1}({evr[n]:.2%})" for n in range(len(evr))],
            save=r"Images/5_principal components.png")

# 차원축소와 복원
fruit_pca = pca.transform(fruit.reshape(-1, 100*100))
fruit_inverse = pca.inverse_transform(fruit_pca)
print(fruit.shape)
print(fruit_pca.shape)
print(fruit_inverse.shape)
