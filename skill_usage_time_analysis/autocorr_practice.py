import numpy as np

def autocorrelation_fft(x):
    """
    FFT를 사용한 자기상관 함수 계산
    :param x: 입력 신호 (넘파이 배열)
    :return: 자기상관 함수 값 (넘파이 배열)
    """
    n = len(x)
    # 제로패딩 (2배 크기)
    x_padded = np.pad(x, (0, n), mode='constant')
    # FFT 계산
    fft_x = np.fft.fft(x_padded)
    # 푸리에 계수의 크기 제곱
    power_spectrum = np.abs(fft_x) ** 2
    # 역 FFT로 자기상관 함수 계산
    autocorr = np.fft.ifft(power_spectrum).real
    # 신호 길이에 맞게 슬라이싱
    autocorr = autocorr[:n]
    # 정규화 (R[0] = 에너지)
    autocorr /= autocorr[0]
    return autocorr
