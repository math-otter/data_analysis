import numpy as np

# 1. 정의
x = np.array(['x(0)', 'x(1)', 'x(2)'])
n = len(x)
for tau in range(n):
    r = f'Rxx({tau}) = '
    for t in range(n - tau):
        r = r + f'+ {x[t + tau]}*{x[t]} '
    print(r)

# 2. 함수 만들기
def autocorr(x):
    n = len(x)
    autocorr = []
    for tau in range(n):
        r = 0
        for t in range(n - tau):
            r += x[t + tau]*x[t]
        autocorr.append(r)
    return autocorr

# 3. 간결화
def autocorr(x):
    n = len(x)
    return [np.sum(x[:n - tau] * x[tau:]) for tau in range(n)]

