import numpy as np


def histogram_hesapla(goruntu):
    genislik, yukseklik = goruntu.shape
    hist = np.zeros(256)

    for v in range(yukseklik):
        for u in range(genislik):
            i = goruntu[u, v]
            hist[i] += 1

    return hist


# Görüntüyü buraya yerleştirin
goruntu = ...

# Histogramı hesapla
histogram = histogram_hesapla(goruntu)


