MetalBase = {"01крст3":2, "02крст45":5, "03угст3":4, "04угст45":7, "05лсст3":8, "06лсст45":2}
MetalBase["02крст45"]=6
MetalBase["03угст3"]=10
MetalBase["04угст45"]=3
MetalBase["07трст3"]=11
MetalBase["08трст45"]=9
def recomend ():
    i=MetalBase[name]
    if i <= 5:
        recomendation = 6-i
        print ("рекомендуется пополнить запасы на", recomendation)
    elif i > 5:
        recomendation = i-5
        print ("запасы превышают минимум на", recomendation)
def chek_existence ():
    if name in keys:
        recomend ()
    else:
        print ("данный артикул отсутствует")
def chek_all ():
    kluch=list(MetalBase.keys())
    for n in kluch:
        num = MetalBase[n]
        i=num
        if i <= 5:
            recomendation = 6-i
            print ("рекомендуется пополнить запасы ", n, " на ", recomendation)
        elif i > 5:
            recomendation = i-5
            print ("запасы ", n, " превышают минимум на ", recomendation)
while True:
    name=input("введите код товара    ")
    if name == "проверить все":
        chek_all ()
        print ("PLEASE STAND BY")
        break
    else:
        keys=list(MetalBase.keys())
        chek_existence ()
        contin=input("продолжить проверку? (да/нет)    ")
        if contin == "нет" or contin == "Нет":
            print ("PLEASE STAND BY")
            break