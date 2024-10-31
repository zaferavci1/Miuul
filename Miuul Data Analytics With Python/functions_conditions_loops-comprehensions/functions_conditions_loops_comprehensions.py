# Fonksiyonlar (Functions)

## Fonksiyon Okur-Yazarlığı

#?print # bu ifade bu fonksiyonun neler yaptığını, hangi argümanları kullandığını bize anlatır.

help(print()) # help fonksiyonu da aynı işe yarar.
print("a", "b", sep="__")

## fonksiyon tanımlama

def calculate(x):
    print(x*2)

calculate(5)

## iki argümanlı

def summer(a,b):
    print(a+b)

summer(8,7)
summer(b=10, a=15)

# Docstring : bilgi notu
# docstring 3 bölümden oluşur
#  1- fonksiyonun ne yaptığı
#  2- parametreleri neler
#  3- return'ün ne olacağı
def summer(a,b):
    """
    iki parametreli toplama fonksiyonu
    :param a:int,float

    :param b:int,float

    :return:
    """
    print(a+b)



def calculate(x):
    print(x*2)

# Fonksiyonların Gövde (Statment) Bölümü

# def function_name(parametes/argumans):
#     statemnet(function body)

def say_hi(string):
    print(string)
    print("hello")
    print("hi")

say_hi("merhaba")

def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10,9)

# girilen değerleri bir liste içerisinde saklayacak fonksiyon

list_stor = []

def add_element(a, b):
    list_stor.append((a * b))
    print(list_stor)

add_element(10,3)
add_element(45,8)

# Ön tanımlı argümanlar/parameterler

def divide(a, b):
    print(a / b)

divide(4,2)

def divide(a, b = 1):
    print(a / b)

divide(8)


# En zaman fonksiyon yazılır

# varm moisture charge

# DRY - Don't Repeat Yourself
# kendini tekrar etmemen lazım bu durumdan kendini tekrar etmeye başladığını anladığında fonksiyon yaz


# Retun fonksiyonlar:

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge

type(calculate(10,50,20))


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output =(varm + moisture) / charge
    return varm, moisture, charge, output


type(calculate(10,50,20)) # calculate metodu tuple bir nesne olarak dönüş sağladı

varm, moisture, charge, output = calculate(10,50,20)


# Koşullar

if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(9)

def number_check(number):
    if number > 10:
        print("number grather than 10")
    elif number <= 10:
        print("number equal or less than 10")
    else:
        print("number less than 10")
number_check(9)


# LOOPS

# for
students = ["zafer", "boran", "serkan"]
for i  in students:
    print(i)

for i in students:
        print(i.upper())

salaries = [1000, 2000, 3000, 4000]

for salary in salaries:
    if salary < 2010:
        print(int(new_salary(salary, 20)))
    else:
        print(int(new_salary(salary, 10)))
def new_salary(salaries, rate):
    return salaries + salaries * rate / 100

new_salary(1000,10)

string ="zafer"
def upper_string(str):
    new_string = ""
    for string_index in range(len(str)):
        if string_index % 2 == 0:
            new_string += str[string_index].upper()

        else:
            new_string += str[string_index].lower()

    print(new_string)

upper_string(string)


# Break-Continue-While

salaries = [1000, 2000, 3000, 4000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)
    

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

number = 0
while number < 5:
    print(number)
    number += 1


# Enumerate: Otomatik indeks üretici/ Counter

students = ["zafer", "boran", "serkan"]
students2 = []
students3 = []
# for index, student in enumerate(students, 1):
for index, student in enumerate(students):
    print(index, student)

for index, student in enumerate(students):
    if index % 2 == 0:
        students2.append(student)
    else:
        students3.append(student)

def divide_students(list):
    for index, student in enumerate(students):
        if index % 2 == 0:
            students2.append(student)
        else:
            students3.append(student)
    students2.append(students3)
    return students2

divide_students(students)

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.lower()
        else:
            new_string += letter.upper()
    print(new_string)

alternating_with_enumerate("hi my name is zafer and i am learning python")


students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

departments = [23, 30, 26, 22]

list(zip(students, departments, departments))


# lambda, map, filter, reduce

# lambda bize kullan at tarzında bir fonksiyon tanımlamamızı sağlar

new_sum = lambda a, b: a+b

new_sum(5 + 9)

# map


salaries = [1000, 2000, 3000, 4000]
def new_salary(salary):
    return salary * 20 / 100 + salary

new_salary(2000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries)) #map fonksiyonu bizden önce bir fonksiyon ister ardından üzerinde gezebileceğimiz iteratif bir nesne ister

list(map(lambda x: x * 20 / 100 + x, salaries)) # lambda'yı burada daha iyi bir şekilde anlayabildik.

list(map(lambda x: x ** 2, salaries))

# FILTER  filtreleme işlemleri için kullanılır. Map fonksiyonu gibi kendisine üstünde gezebileceği iteratif bir nesne lazım

list_store = [1, 2, 3, 4, 5, 6, 7]

list(filter(lambda x: x % 2 == 0, list_store))


# REDUCE

from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store) # list store içerisindeki değerleri toplayarak bize verdi.


string = "abracadabra"
group = []
for index, letter in enumerate(string, 1):
    if index * 2 % 2 == 0:
        group.append(letter)
print(group)







