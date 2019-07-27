import numpy as np

CROP_MS = 1000  # クロップする範囲(ms)
OVERLAP_MS = 500  # クロップ時に重ねる範囲(ms)
DIVISION = 150  # ペリオドグラムの時間分割数
PERIODOGRAM_SIZE = [28, 28]  # ペリオドグラムのプーリング後サイズ


def _discrimination_algorithm_threshold(part_mean):
    return part_mean > 127


def crop(buffers, sample_rate):
    if CROP_MS <= OVERLAP_MS:
        print("[NOTICE] overlap_ms is more than crop_ms")
        exit()

    """各クロップサイズ、オーバーラップ数をmsからサンプル数に変換"""
    crop_size = int((sample_rate * CROP_MS) / 1000)  # 切り取るサンプル数
    overlap_size = int((sample_rate * OVERLAP_MS) / 1000)  # オーバーラップするサンプル数
    increase_size = crop_size - overlap_size  # 繰り返しのときに進めるサンプル数
    literal_max = int(((buffers.shape[0] - crop_size) / (crop_size - overlap_size)) + 1)  # buffersをはみ出ない繰り返し切り取り回数

    cropped_buffers = []
    for i in range(literal_max):
        cropped = buffers[(increase_size * i):((increase_size * i) + crop_size)]  # クロップ
        part_mean = np.mean(np.abs(cropped))  # 区間の最大値

        # 区間に音声が含まれているか識別
        if not _discrimination_algorithm_threshold(part_mean):
            continue
        cropped_buffers.append(cropped)

    return cropped_buffers


def create_periodogram(data):
    N = data.shape[0]  # データ全体のサンプル数
    Nd = int(N / DIVISION)  # 分割時のサンプル数
    periodogram = np.zeros(int(int(Nd / 2) * DIVISION))

    for t in range(DIVISION):
        data_p = data[(Nd * t):(Nd * (t + 1))]  # 分割数ごとにクロップ

        hanningWindow = np.hanning(Nd)  # ハニング窓
        dft = np.fft.fft(hanningWindow * data_p)  # 離散フーリエ変換
        dft_abs = np.log(np.abs(dft) ** 2)  # 振幅特性

        periodogram[(int(Nd / 2) * t):((int(Nd / 2) * (t + 1)))] = dft_abs[:int(Nd / 2)]

    periodogram = np.reshape(periodogram, (DIVISION, int(Nd / 2)))

    # 28*28にブーリング
    periodogram_pool = np.zeros(PERIODOGRAM_SIZE)
    a = int(periodogram.shape[0] / PERIODOGRAM_SIZE[0])
    b = int(periodogram.shape[1] / PERIODOGRAM_SIZE[1])
    for j in range(PERIODOGRAM_SIZE[1]):
        for i in range(PERIODOGRAM_SIZE[0]):
            periodogram_pool[j, i] = np.mean(periodogram[(j * a):(j * a + a), (i * b):(i * b + b)])

    # 正規化
    periodogram_regu = np.floor(
        (periodogram_pool - np.min(periodogram_pool)) * 127 / (np.max(periodogram_pool) - np.min(periodogram_pool)))
    return periodogram_regu
