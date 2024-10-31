# Veri yapılarını inceleme

# GÖREV 1
def data_structure(data):
    print(type(data))


x = 8

y = 3.2

z = 8j + 18  # complex

a = "Hello World"

b = True

c = 23 < 22

d = {"Name": "Jake",
     "Agel": 27,
     "Adress": "Downtown"}

t = ("Data Scüence", "Machine Learning")  # tuple

s = {"Python", "Machine Learning", "Data Science"}  # set

data_structure(s)

# GÖREV 2

text = "The goal is to turn data into Information, and information into insight. "
text = text.upper()
text = text.replace(",", " ")
text = text.replace(".", " ")
text = text.split()
print(text)

# GÖREV 3
list_data = ["D", "A", "T", "A", "S", "I", "C", "I", "E", "N", "C", "E"]

len(list_data)
print(list_data[0], list_data[10])

new_list = []

for index, listed in enumerate(list_data):
    if index < 4:
        new_list.append(listed)

print(new_list)

list_data.pop(8)
list_data.append("Z")
list_data.insert(8, "N")

# GÖREV 4

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Daniel': ["Italy", 25]}

dict.keys()

dict.values()

dict.update({"Daisy": ["Italy", 13]})

del dict["Antonio"]

# GÖREV 5

l = [2, 3, 13, 18, 19, 93, 22]
single = []  # tek
pair = []  # cift


def single_pair(listed):
    for list in listed:
        if list % 2 == 0:
            pair.append(list)
        else:
            single.append(list)
    return pair, single


print(single_pair(l))  # ([2, 18, 22], [3, 13, 19, 93])

# GÖREV 6

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

a = 1


def muhendislik(ogr, a):
    print(f"Mühendislik Fakültesi {a}. öğrencisi : {ogr}")
    a += 1


def tip(ogr, a):
    print(f"Tıp Fakültesi {a}. öğrencisi : {ogr}")
    a += 1


for index in range(len(ogrenciler)):
    if a < 4:
        muhendislik(ogrenciler[index], a)
        a += 1
    else:
        a = 1
    tip(ogrenciler[index], a)
    a += 1

# GÖREV 7

ders_kodu = ["CMP1005", "PSYIOOI", "HUK1005", "SEN2204"]

kredi = [3, 4, 2, 4]

kontenjan = [30, 75, 150, 25]

a = list(zip(ders_kodu, kredi, kontenjan))
for dersKodu, kredi, kontenjan in a:
    print(f"Kredisi {kredi} olan {dersKodu} kodlu dersin kontenjanı {kontenjan}")

# GÖREV 8

kume1 = set(["data", "python"])

kume2 = set(["python", "miuul", "functionl", "qcut", "lambda", "data"])


def fark(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))


fark(kume1, kume2)

