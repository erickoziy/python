MetalBase = {"01крст3":2, "02крст45":5, "03угст3":4, "04угст45":7, "05лсст3":8, "06лсст45":2}
MetalBase["02крст45"]=6
MetalBase["03угст3"]=10
MetalBase["04угст45"]=3
MetalBase["07трст3"]=11
MetalBase["08трст45"]=9
kluch=MetalBase.keys()
print (kluch)
def recomend ():
    num=MetalBase[n]
    i=num
    if i <= 5:
        recomendation = 6-i
        print ("рекомендуется пополнить запасы ", n, " на ", recomendation)
    elif i > 5:
        recomendation = i-5
        print ("запасы ", n, " превышают минимум на ", recomendation)
for n in kluch:
    recomend ()