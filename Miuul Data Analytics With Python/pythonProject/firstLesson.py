# SAYILAR ve KARAKTER DIZILERI

print("hello AI world")

print(9)
type(98)
print(type(9))

# ATAMALAR VE DEGISKENLER
a=9

b="hello AI wolrd"
print(type(b))

#################################
# Virtual Environment (Sanal Ortam) ve (Package Managment) Paket Yönetimi
#################################
# Sanal ortamların listelenmesi:
# cond env list

# Sanal ortam oluşturma:
# conda creat -n zaferOrtam

# Sanal ortamı aktif etme:
# conda activate zaferEnv

# Yüklü paketlerin listelenmesi:
# conda list

# Paket yükleme:
# conda install numpy

# Aynı anda birden çok paket yüklemek istersek bir boşluk bırakarak diğer paket isimlerini yazmamız yeterli:
# conda install numpy scipy pandas

# Paket silme
# conda remove package_name

# Belirli bir versiyon paketi kurma:
# conda install numpy=1.25.2

# Pkaet yükseltmek için:
# conda upgrade numpy

# Tüm paketlerin yükseltilmesi için:
# conda uprgrade -all

#pip: pypi (python package index) paket yönetim aracı

# Paket yükleme:
# pip install package_name

# Paket yükleme versiyona göre:
# pip install package_name==1.2.1

# Kullandığımız paketleri ve versiyonlarını bir dosya içerisinde görmek için:
# conda env export > environment.yaml komutunu çalıştırarak proje klasörünün içerisinde payl uzantılı bir dosya oluşturuyoruz. Bu dosya bize farklı bir projede aynı paketleri kullanmamıza yarımdı olacak.

# Başka bir projede bu ortamı tekrar nasıl aktif edebiliyoruz:
# environment.yaml dosyasını kullanmak istediğimiz projede conda env export > environment.payl komutu sayesinde var olan bir ortamı tekrardan ister kendi bilgisayramızda ister başka bir bilgisayarda oluşturabiliyoruz.












