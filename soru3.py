import random
# random sayıyı tahmin etme oyunu

def tahmin(kackere,sayı):
    for i in range(0,kackere,1):
        tahmin=int(input("1 ile 30 arasında bir sayı giriniz"))
        if tahmin<sayı and tahmin<=30 and tahmin>0:
            print("sayınızı büyütün lütfen {} tahmin hakkınız kaldı".format(kackere))
        elif tahmin>sayı and tahmin<30 and tahmin>0:
            print("sayınızı küçültün lütfen {} tahmin hakkınız kaldı".format(kackere))
        elif tahmin==sayı and tahmin<30 and tahmin>0:
            print("tebrikler doğru tahmin")
            break
        elif tahmin>30 or tahmin<=0:
            print("tahmin aralığına dikkat ediniz lütfen {} tahmin hakkınız kaldı".format(kackere))
        kackere-=1




sayı=random.randint(1,30)
print("random sayı : ",sayı)
kackere=int(input("kaçkere tahmin edeceğinizi yazınız"))
tahmin(kackere,sayı)
