MetalBase = {"01крст3":2, "02крст45":5, "03угст3":4, "04угст45":7, "05лсст3":8, "06лсст45":2}
MetalBase["02крст45"]=6
MetalBase["03угст3"]=10
MetalBase["04угст45"]=3
MetalBase["07трст3"]=11
MetalBase["08трст45"]=9
MetalBase["04угст45"]=[]
while True:
    name=input("введите код товара    ")
    keys=list(MetalBase.keys())
    if name in keys:
        i=MetalBase[name]
        if i <= 5:
            recomendation = 6-i
            print ("рекомендуется пополнить запасы на", recomendation)
        elif i > 5:
            recomendation = i-5
            print ("запасы превышают минимум на", recomendation)
    else:
        print ("данный артикул отсутствует")
    contin=input("продолжить проверку? (да/нет)    ")
    if contin == "нет" or contin == "Нет":
        print ("PLEASE STAND BY")
        break