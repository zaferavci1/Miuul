# List_Comprehension

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


[salary * 2 for salary in salaries]  # Herhangi bir metot yazmadan bütün maaşların iki katını aldık.

[salary * 2 for salary in salaries if salary < 3000]  # Comprehesion'da sadece if bloğu kullanılacak ise for if bloğunun sol tarafında kalır ama if-else bloğu birlikte kullanılacak ise for en sonda yer alır.

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]
[student.upper() if student not in students_no else student.lower() for student in students]

# Dict Comprohension

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()  # list yapısında key value çiftlernin döndürüyor.

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v ** 2 for (k, v) in dictionary.items()}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

new_dict = {}

new_dict = {num: num ** 2 for num in numbers if num % 2 == 0}


# List & Dict Comprehension Uygulamaları


# Bir veri setindeki değişken isimlerini değiştirmek:


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# görev columns isimlerini büyük harf yapıp kaydetmek.
# eski yöntem

A = []
for col in df.columns:
    A.append(col.upper())

df.columns = A

# Comprehension

df.columns = [colm.upper() for colm in df.columns]

# İsminde ”INS” olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.

df.columns = ["FLAG_" + colm if "INS" in colm else "NO_FLAG" + colm for colm in df.columns]







import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_colms = [col for col in df.columns if df[col].dtype != "O"]  #türü object olmayan nesneleri ayırdık

agg_list = ["mean", "min", "max", "sum"]

new_dict = {colm: agg_list for colm in num_colms} # dictionary de değişken key değerlerine karşın sabit value değerlerini ekleyerek oluşturduk.

df[num_colms].head()  #elimizdeki verilerin sadece numerik olanlarını aldık

df[num_colms].agg(new_dict)  #aggregation fonksiyonumuz bizim akıllı fonksiyonlarımızdan biridir. Aggrigation fonksiyonumuza biz bir dictionary gönderdik
                    #   ve bu dict de olan key değerleri o tabloda olan head ler ile  eşleşirse value değerlerindeki fonksiyonlar o headlardaki değerlere uygulanır.




