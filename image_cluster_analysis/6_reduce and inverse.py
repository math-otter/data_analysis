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
pca = PCA(n_components=100)
pca.fit(fruit.reshape(-1, 100*100))

# 차원축소와 복원
fruit_pca = pca.transform(fruit.reshape(-1, 100*100))
fruit_inverse = pca.inverse_transform(fruit_pca)
print(f"축소된 데이터: {fruit_pca.shape}")
print(f"복원된 데이터: {fruit_inverse.shape}")

# 축소된 데이터 시각화
draw_images(fruit_pca.reshape(-1, 10, 10)[0:492], ncols=25, save=r"Images\6_reduced apples")
draw_images(fruit_pca.reshape(-1, 10, 10)[492:982], ncols=25, save=r"Images\6_reduced bananas")
draw_images(fruit_pca.reshape(-1, 10, 10)[982:1474], ncols=25, save=r"Images\6_reduced cherries")

# 복원된 데이터 시각화
draw_images(fruit_inverse.reshape(-1, 100, 100)[0:492], ncols=25, save=r"Images\6_inversed apples")
draw_images(fruit_inverse.reshape(-1, 100, 100)[492:982], ncols=25, save=r"Images\6_inversed bananas")
draw_images(fruit_inverse.reshape(-1, 100, 100)[982:1474], ncols=25, save=r"Images\6_inversed cherries")