# diziye veri ekleme ve eklenen veriyi ekrana yazdırma

def diziveriekle(kacsayı):

    for i in range(0,kacsayı,1) :
        sayı=int(input("{} : kadar sayı giriniz".format(kacsayı)))
        sayılar.append(sayı)
        kacsayı-=1
def diziyaz():
    for i in sayılar :
        print(i)

kacsayı=int(input("kaç sayı gireceğinizi yazınız"))
sayılar=[]

diziveriekle(kacsayı)

diziyaz()


