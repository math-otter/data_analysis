import numpy as np
from imgtoarray import load_images
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate

# 데이터 로드
apple = load_images("Training/Apple Red 1")  # 492장
banana = load_images("Training/Banana 1")    # 490장
cherry = load_images("Training/Cherry 1")    # 492장
fruit = np.concatenate((apple, banana, cherry), axis=0)  # 1474장

# 주성분 분석
pca = PCA(n_components=2)
fruit = fruit.reshape(-1, 100*100) # 훈련 데이터로 전달하기 위해 2d 배열로 만든다.
pca.fit(fruit)

# 로지스틱 회귀모델 객체 생성, 정답 레이블 설정
lr = LogisticRegression(random_state=42)
y = np.array(["apple"]*492 + ["pineapple"]*490 + ["banana"]*492) # 정답 레이블 설정

# 두 가지 훈련 데이터
x = fruit # 원본
x_pca = pca.transform(x) # 차원축소본

# 원본 데이터를 사용한 훈련결과
cv_results = cross_validate(lr, x, y, cv=5, n_jobs=-1)
test_score = np.mean(cv_results["test_score"])
fit_time = np.mean(cv_results["fit_time"])
print("원본 데이터 사용")
print("폴드별 점수: {}, 최종 점수: {}".format(cv_results["test_score"], test_score))
print("폴드별 훈련시간: {}, 평균 훈련시간: {}".format(cv_results["fit_time"], fit_time))

# 차원축소본 데이터를 사용한 훈련결과
cv_results = cross_validate(lr, x_pca, y, cv=5, n_jobs=-1)
test_score = np.mean(cv_results["test_score"])
fit_time = np.mean(cv_results["fit_time"])
print("\n2개의 특성 사용")
print("폴드별 점수: {}, 최종 점수: {}".format(cv_results["test_score"], test_score))
print("폴드별 훈련시간: {}, 평균 훈련시간: {}".format(cv_results["fit_time"], fit_time))