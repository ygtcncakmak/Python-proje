# sınav puanına göre harf notunu ekrana yazdıran uygulama
def harfdeger(a):

    if (a >= 85 and a < 100):
            {
                print("A")
            }
    elif (a >= 75 and a < 85):
            {
                print("B")
            }
    elif (a >= 60 and a < 74):
            {
                print("C")
            }
    elif (a >= 45 and a < 59):
            {
                print("D")
            }
    elif( a >= 30 and a < 44):
            {
                print("E")
            }
    elif (a >= 0 and a < 29):
            {
                print("F")
            }


b=int(input("lütfen sınav puanınızı giriniz"))
harfdeger(b)





