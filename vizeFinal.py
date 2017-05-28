#!/usr/bin/python3
#-*-coding:utf-8-*-

# Hakan Mustak
# hmustak@gmail.com
# 28.05.2017 14:37
# Python3 Antreman : Basit Vize Hesaplama Uygulaması

# 40-60 oranına göre hesaplanmıştır

vize = float(input("Vize girin : "))
final = float(input("Final girin : "))
gereken = (60-(vize*40/100))*100/60

# Kural2 : Final 60'ın altındaysa kalınır
# Kural3 : Vize 40 üzerinde, final 60 altındaysa büte girilir
if (final < 60):
    but = float(input("Büt girin : "))
    final = but

print("-"*50)
ortalama = ((vize*40/100)+(final*60/100))
print("İhtiyacınız olan not : {0:.2f}".format(gereken))
print("-"*50)

if (vize < 40) or (final < 60):
    print("Dersten Kaldınız! : {0:.2f}".format(ortalama))
else:
    # Kural4 : Ortalama 60'ın altındaysa kalınır
    if (ortalama>=60):
        print("Dersten Geçtiniz: {0:.2f}".format(ortalama))
    else:
        print("Kaldınız: {0:.2f}".format(ortalama))
