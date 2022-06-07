import colorama # pip install colorama
colorama.init()

import numpy as np # pip install numpy

# ( Programı çalıştırmak için numpy kütüphanesini yükleyiniz )


# Numpy ile liste oluşturma

# örnek
liste=np.array([1,2,3,4,5,6,7,8,9,10])
print(colorama.Fore.BLUE+"array liste = ",colorama.Fore.RED,liste,"\n")

# örnek

meyveler=["muz","armut","elma","portakal"]
listeMeyveler=np.array(meyveler)
print(colorama.Fore.BLUE+"meyveler listesi = ",colorama.Fore.RED,listeMeyveler,"\n")


# Numpy kütüphanesi ile belirlenen sayı aralığındaki sayıları bulma metodu

# örnek

result=np.arange(1,10) # to arange
print(colorama.Fore.BLUE+"range = ",colorama.Fore.RED,result,"\n")

# örnek

sayi=np.arange(50,100,5)
print(colorama.Fore.BLUE+"range = ",colorama.Fore.RED,sayi,"\n")


# Numpy ile 0 ve 1'den oluşan elemanları listeleme

# örnek

sifir=np.zeros(10)
print(colorama.Fore.BLUE+"sıfırlardan oluşan liste =",colorama.Fore.RED,sifir,"\n")

# örnek

bir=np.ones(10)
print(colorama.Fore.BLUE+"birlerden oluşan liste =",colorama.Fore.RED,bir,"\n")


# Numpy ile istenilen kadar ve istenilen aralıklarda sayı üretme

# örnek

aralik=np.linspace(0,100,5)
print(colorama.Fore.BLUE+"belirtlen aralıktaki sayılar = ",colorama.Fore.RED,aralik,"\n")


# Numpy ile random sayı oluşturma

# örnek

randoms=np.random.randint(1,100)
print(colorama.Fore.BLUE+"random üretilen sayı = ",colorama.Fore.RED,randoms,"\n")

# örnek

randoms1=np.random.randint(1,100,5)   # 1 ile 100 arasında 5 adet random sayı üretimi
print(colorama.Fore.BLUE+"random üretilen sayı 5 adet = ",colorama.Fore.RED,randoms1,"\n")


# Numpy ile matris oluşturma

# örnek

sayi1=np.random.randint(1,100,15)  # 3x5'lik matris oluşturmak için random olarak 15 adet sayı istendi

matris=sayi1.reshape(3,5)

print(colorama.Fore.BLUE+"matris = ",colorama.Fore.RED,matris,"\n")

# örnek (üretilen matrisin satır ve sütun toplamları)

matris_satirToplami=matris.sum(axis=1) # satır toplamı
print(colorama.Fore.BLUE+"matris satır toplamı = ",colorama.Fore.RED,matris_satirToplami,"\n")

matris_sutunToplami=matris.sum(axis=0) # sütun toplamı
print(colorama.Fore.BLUE+"matris sütun toplamı =",colorama.Fore.RED,matris_sutunToplami,"\n")


# örnek (üretilen matrisin ortalaması)

matris_ortlama=matris.mean()
print(colorama.Fore.BLUE+"matrisin ortalaması =",colorama.Fore.RED,matris_ortlama,"\n")

# örnek ( Üretilen matrisin en büyük ve en küçük değerlerin indexi)

matris_Argmax=matris.argmax()
print(colorama.Fore.BLUE+"üretilen matrisin en büyük değerin indexi =",colorama.Fore.RED,matris_Argmax)

matris_Argmin=matris.argmin()
print(colorama.Fore.BLUE+"üretilen matrisin en küçük değerin indexi =",colorama.Fore.RED,matris_Argmin,"\n")


# Numpy ile bir listedeki elemanların sadece istenilen bölümünü çağırma metodu

# örnek

sayi_elemanlari=np.arange(10,20)
print(colorama.Fore.BLUE+"istenilen sayılar =",colorama.Fore.RED,sayi_elemanlari[:3])

sayi_elemanlari1=np.arange(1,100)
print(colorama.Fore.BLUE+"istenilen sayılar =",colorama.Fore.RED,sayi_elemanlari1[5:7],"\n")

sayi_ornek=np.arange(1,10)
print(colorama.Fore.BLUE+"tersten  yazdırılan liste =",colorama.Fore.RED,sayi_ornek[::-1],"\n")  # belirtilen aralığı tersten yazdırma


# Üretilen matrisin istenilen alanlarını çağırma metodları

uretilen_sayi=np.random.randint(1,50,40)

uretilen_Matris=uretilen_sayi.reshape(4,10)

print("Matris\n",uretilen_Matris)
print(colorama.Fore.BLUE+"Matris ilk satır =",colorama.Fore.RED,uretilen_Matris[0],"\n") # matrisin ilk satırı

print("Matris\n",uretilen_Matris)
print(colorama.Fore.BLUE+"Matrisin 3.satır 2.elemanı =",colorama.Fore.RED,uretilen_Matris[2,1],"\n")


karesi=uretilen_Matris**2
print(colorama.Fore.RED+"Matris\n",uretilen_Matris)
print(colorama.Fore.BLUE+"Üretilen matrisin kareleri\n",colorama.Fore.RED,karesi)   # üretilen matrisin kareleri

# Numpy ile belirlenen sayıların istenilen özelliklerini bulma metodları

sayim=np.arange(-50,50+1)
print(colorama.Fore.YELLOW+"\nSayılar\n",colorama.Fore.RED,sayim)
pozitifTekSayilar=sayim[sayim%2==0]
print(colorama.Fore.BLUE+"Pozitif çift sayılar\n",colorama.Fore.RED,pozitifTekSayilar[pozitifTekSayilar>=0]) # Belirtilen aralıktsaki pozitif çift sayılar


negatifCift=sayim[sayim%2==1]
print(colorama.Fore.BLUE+"negatif tek sayılar \n",colorama.Fore.RED,negatifCift[negatifCift<0],"\n") # Belirtilen aralıktaki negatif tek sayılar

















