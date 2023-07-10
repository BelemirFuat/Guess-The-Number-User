import random

def guess(son):
    # durum -1 küçük, durum 0 eşit durum 1 büyük
    durum = -1
    bas=1
    while(durum!=0):
        guess= random.randint(bas,son)
        durum = int(input("{} ?: ".format(guess)))
        if(durum==-1):
            son=guess
        elif(durum==1):
            bas =guess
    print("Congrats!")

guess(1000)