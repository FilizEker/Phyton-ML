

import random
print("Sayı Tahmin Oyununa hosgeldin")

hak=3
sayı=random.randint(0,10)

for i in range(hak):
  
    tahmin=int(input("0-10 arasında bir sayı tahmin ediniz."))
    if sayı==tahmin:
        print("Tebrikler bildiniz.")
        bilindi=True
        break
    elif sayı>tahmin and i!=hak-1:
        print("Daha büyük bir sayı tahmin ediniz.")
        
    elif sayı<tahmin and i!=hak-1:
        print("Daha küçük bir sayı tahmin ediniz.")
    else:
        sayı!=tahmin
        print("Sayı ",sayı," idi.")
