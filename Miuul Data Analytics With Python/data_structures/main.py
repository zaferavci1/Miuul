# Veri Yapıları(Data Structures)

## Veri yapılarına giriş ve Hızlı Özet:
### Sayılar integer:
a=46
type(a)

### Sayılar float:
a=10.3
type(a)

### Sayılar complex:
x=2j+1
type(x)

### Sayılar string:
a="zafer"
type(a)

### Sayılar bool:
a=True
type(a)

### Sayılar liste:
x = ["sdad", "adfasf", "zafer"]

### Sayılar sözlük:
x = {"zafer": "zafer", "age": 21}
# sözlükler key:value tarzında oluşturulur.
type(x)

### Sayılar tuple:
x = ("adsd", "zafer", "merhaba")
type(x)

### Sayılar set:
x = {"merhaba", "herkese"}
# sözlüklerden farklı olarak key : value yok
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak da ifade edilir.

## Sayılar (Numbers): int, float, complex

a = 5
b = 10.5

a * 3  # pep8 kanunları python yazanlar arasında uygulanan kuralları içerir.
a / 7
a * b / 10
a ** 10

# Tipleri değiştirme

int(b)
float(a)
int(a * b / 10)

# Karakter dizilieri (Strings)

print("zafer")
print('zafer')

name="zafer"
print(name)

# Çok satırlı karakter dizileri

""" Merhaba ben zafer,
Veri yapilari hizli özet,
Long string"""

long_str = """ Merhaba ben zafer,
Veri yapilari hizli özet,
Long string"""
print(long_str)

# Karakter dizilerinin elemanlarına erişmek:

long_str[3]

# Karakter dizilerinde slice işlemi
name[3:10]

 # String içerisinde karakter sorgulamak

"Veri" in long_str


# String dizisi metodları
dir(int)

dir(str)
name = " merhabalar "

# len
len(name)
len("vahitkeskin")

# Eğer bir fonksiyon class yapısı içerisinde tanımlandıysa buna metod denir. Class yapısı içerisinde değilse fonksiyondur.

# upper() & lower(): küçük-büyük dönüşümleri

"miuul".upper()
"miuul".lower()

#replace : karakter değişimi
hi = "Hello AI era"
hi.replace("l","p")

#split böler
"Hello AI era".split()

# strip : boşlukları kırpar
" opopo ".strip("o")

# capitalize : ilk harfi büyük yapar

"miuul".capitalize()

"miuul".startswith("f")



# Liste : List
# Değiştirilebilir
# Sıralıdır. Index islemleri yapılabilir.
# Kapsayicidir.

notes = [1,2,3,4,5,6]
type(notes)

names = ["zafer", "mustafa", "ilkkan"]

not_nam = [1, 2, 3, "ersoy", True, [1,2,3]]

not_nam[4]
not_nam[5][1]

type(not_nam[5])
type(not_nam[5][1])

not_nam[0] = 9
not_nam[0]

# Liste metotları (Lİst methods)
dir(not_nam)

## append : eleman ekler
names.append(100)

## pop indexe göre siler
names.pop(3)

## insert : indexe ekler
names.insert(2,"99")


# Sözlük : (Dictionary)

# değiştirileblir
# sırasız
# kapsayıcı

# key-value

dictionary = {"REG" : "regression",
              "LOG" : "logistik regression",
              "CART" : "Classsification and Reg"}

dictionary = {"Reg" : ["regression", 10, "Dictionary içerisinde liste oluşturduk"]}

dictionary["Reg"][2]

dictionary = {"Reg" : 10,
              "Log" : 45}


# Key sorgulama
"Reg" in dictionary

# Value değiştirmek

dictionary["Reg"] = ["Ysa", 10]

# Tüm keylere erişme
dictionary.keys()

# Tüm Value değerlere erişmek
dictionary.values()

# Tüm çiftleri TUPLE halinde listeye çevirme
dictionary.items()

# Key value değerlerini güncellemek
dictionary.update({"Reg" : 11})

# Yeni key value değerleri eklemek
dictionary.update({"zafer" : "avcı"})

# Demet (Tuple)
# tuple'lar listelerin değişime kapalı halleridir.
# -Değiştirilemez
# -Sıralıdır
# -Kapsayıcıdır. Birden farklı veri yapısını tutabiliyor.

t = ("zafer", 1)
type(t)

t[0]
t[0:3]
# tuple elemanları değiştirlemez. Değiştirmek için tuple nesnesini ilk olarak bir listeye çevirip liste üzerinden elemanı değiştirip tekrar tuple yaparsak olur.
# Tuple bize listelerden daha güvenli bir çalışma imkanı sağlıyor.

t = list(t)
t[0] = "Boran"
t = tuple(t)
t[0]

# Set
# Değiştirilebilir
# Sırasız + Eşsizdir
# Kapsayıcıdır


# difference() : iki kümenin farkı

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1 de olup set2 de olamayanlar
set1.difference(set2)
set1 - set2 # matematiksel olarak da yapabiliriz.

# set2 de olup set1 de olamayanlar
set2.difference(set1)
set2 - set1

# symmetric_difference(): iki kümede de birbirlerine göre olmayanlar

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

# intersection(): iki kümenin kesişimi

set1.intersection(set2)
set2.intersection(set1)

set1 & set2

# union() : birleşim işlemi
set2.union(set1)
set1.union(set2)

# isdisjoint() : İki kümenin birleşimi boş mu değil mi ?

set1.isdisjoint(set2)
set2.isdisjoint(set1)

# issubset() : Bir küme diğer kümeyi kapsıyor mu ?

set1 = set([1, 2, 3])
set2 = set([1, 2, 3, 5, 6, 78, 8])

set1.issubset(set2) # true
set2.issubset(set1)














