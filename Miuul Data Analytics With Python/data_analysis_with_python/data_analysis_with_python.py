# PYTHON İLE VERİ ANALİZİ (data_analysis_with_python)
import string

# - NUMPY
# - PANDAS
# - VERİ GÖRSELLEŞTİRME: Matplotlib & Seaborn
# - GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ



#      NUMPY

# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arpays)
# NumPy Array Özellikleri (Attibutes of Numpy Arpays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da KOŞULLU İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)


import numpy as np

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 5, 6])
a * b

# NumPy arrayi oluşturma

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype = int)  # 10 tane 0 içeren array oluşturdu.

np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))  # ortalaması 10 standart sapması 4 olan 3 * 4 lk bir array oluşturdu.


# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi


a = np.random.randint(1, 10, size=10)

a.ndim
a.shape
a.size
a.dtype


# reshaping

ar = np.random.randint(1, 10, size=9).reshape(3, 3)
ar.reshape(3, 5) # olamaz çünkü arrayimiz 9 elemanlı ve 3 * 5 de 15 eleman gerekiyor bunu da göz önünde bulundurmak lazım



# INDEX SECIMI (Index Selection)

import numpy as np # Numpy sabit tipli bir arraydir.
a = np.random.randint(10, size=10)

a[0]
a[0:5] # sol taraftaki dahil sağ taraftaki dahil değil.
a[0] = 999

m = np.random.randint(10, size=(3, 5))
m[0]
m[0, 0]
m[2, 3] = 999
m[2, 3] = 2.9

m[0:2, 0:3]
m[0:2, 0:5]


# Fancy Index

import numpy as np

a = np.arange(0, 30, 4)

a[0]
a[3]

catch = [1, 2, 3, 4]
a[catch]


# Numpy'da Koşullu İşlemler (Conditions on Numpy)

import numpy as np
m = np.arange(1, 6, 1)


# Klasik Yöntem
ab = []

for i in m:
    if i < 3:
        ab.append(i)

# Numpy Array ile

m < 3
m[m < 3]
m[m > 3]
m[m == 3]
m[m != 3]
m[m >= 3]

c = m[m < 3]


# Matematiksel İşlemler

import numpy as np
c = np.arange(1, 6, 1)

c / 5
c * 5 / 10
c ** c
c - 1

np.subtract(c, 1)
np.add(c, 10)
np.mean(c)
np.sum(c)
np.max(c)
np.min(c)
np.var(c)

# İki bilinmeyenli denklem çözümü

# 5*x0 +   c1 = 10
# 3*x0 + 3*c1 = 25

a = np.array([[5, 3], [1, 3]])
b = np.array([10, 25])

np.linalg.solve(a, b)











