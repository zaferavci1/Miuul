#########################
# PANDAS
########################

# Pandas Series
# Veri Okuma (reading data )
# Veriye Hızlı Bakış (Quick look at data)
# Pandas'ta seçim işlemleri
# Toplulaştırma ve Gruplandırma
# Apply ve Lamda
# Birleştirme İşlemleri



# Pandas Series
# yaygın kulllanım budur

import pandas as pd
s = pd.Series([10, 20, 30, 23, 43])  # pandas serisine çevirdi - indexli bir seri
type(s) #pandas.core.series.Series
s.index
s.dtype
s.size
s.ndim  # boyut bilgisi
s.values

type(s.values) #numpy.ndarray - numpy array
s.head(3)
s.tail(3)

### VERİ OKUMA ###

dfs = pd.read_csv("D:\DERSLER\Python\Miuul\data_analysis_with_python_pandas\Advertising.csv")
dfs.head()
# pandas cheatsheet

### Veriye Hızlı Bakış ###
import seaborn as sns

dataF = sns.load_dataset("titanic")
dataF.head()
dataF.tail()
dataF.shape()
dataF.info()
dataF.columns
dataF.index
dataF.describe().T
dataF.isnull().values.any()  # boş olan en az 1 tane değer var mı?
dataF.isnull().sum()
dataF["sex"].head()
dataF["sex"].value_counts()



### Pandas'ta Seçim İşlemleri

df = sns.load_dataset("titanic")
df.head()


df.index
df[0:13]
df.drop(0, axis=0).head()

delete_index = [1, 3, 5, 7]
df.drop(delete_index, axis=0).head() # kalıcı değil
 # df = df.drop(delete_index, axis=0).head()
# df.drop(delete_index, axis=0, inplace=True).head() inplace yaptığımız değişkenin kalıcı mı yoksa geçiçi mi oldupunu belirtmemizi sağlıyor.


# Değişkeni İndexe Çevirme #
df["age"].head()
df.age.head() # seçim işlemi

df.index = df["age"]
df.drop("age", axis=1, inplace=True)
df.head()

df["age"] = df.index

df.drop("age", axis=1, inplace=True)
df = df.reset_index().head()



### Değişkenler Üzerinde İşlemler ###

"age" in df

s = df["age"].head()

type(df["age"].head())

type(s) # pandas serie oldu

s = df[["age"]].head()

type(s) # data frame oldu

df[["age", "alive"]]

df["age2"] = df["age"] ** 2
df["age3"] = df["age"] / 2

df.drop("age2", axis=1, inplace=True)
df.head()

col_names = ["sex", "parch", "pclass"]

df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains("age")].head()
# loc dataframelerde seçme işlemlerinde kullanılan bir özel yapıdır.

## loc ve iloc ##

# iloc seçimleri index numaralarına göre yapar
# iloc : integer based selection

df.iloc[0:3]  # 0 dan 3 e kadar gitti
df.iloc[0:3, "age"] # hata çünkü bizden index istiyo
df.iloc[0:3, 0:3]
df.iloc[0, 0]

# loc: label based selection

df.loc[0:3]
df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]


### KOŞULLU SEÇiM ###


df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

df[df["age"] > 50]["class"].head()
df.loc[df["age"] > 50, ["class", "age"]].head()

# birden çok koşulda koşulları parantez içerisine yerleştirmemiz lazım
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["class", "age"]].head()

df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & (df["embark_town"] == "Cherbourg")
       | (df["embark_town"] == "Southampton"),
       ["class", "age", "embark_town"]].head()


### TOPLULAŞTIRMA VE GRUPLANDIRMA ###

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})


df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})


df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"],
                                        "survived": "mean"}) # yolcuların bindikleri yere göre ve cinsiyete göre gruplandırıldı ve bunların yaş ortalaması, toplamı; hayatta olma durumlarının ortalaması alındı.



df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "sum"],
                                        "survived": "mean"})


df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean", "sum"],
    "survived": "mean",
    "sex": "count"})


### PIVOT TABLE ####

df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", "embarked", aggfunc = "std")


df.pivot_table("survived", "sex", ["embarked", "class"])

df.pivot_table("survived", "sex", ["embarked", "class"])

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex", ["new_age", "class"])


### APPLY Ve LAMBDA ###


# - apply satırlara belirli fonksiyonları kullanabilme yeteneği sağlar
# - lambda bize kullan at fonksiyonlar sağlar

df.head()
df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = (df[col]/10).head()

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()


df.head()



### Birleştirme Join işlemleri ###

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)

## Merge

df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})


pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")





















