class MetalBase:
    def __init__(self,c,w,m,n=0):
        self.code = c
        self.what = w
        self.material = m
        self.numbers = n
    def recomend (self, n):
        i=n
        if i <= 5:
            recomendation = 6-i
            print ("рекомендуется пополнить запасы на", recomendation)
        elif i > 5:
            recomendation = i-5
            print ("запасы превышают минимум на", recomendation)  
    def operation (self, p):
        inp=input("загрузить(за) или выгрузить(вы)?  ")
        if inp == "за":
            self.numbers = self.numbers + p
            print("операция выполнена")
        elif inp == "вы":
            self.numbers = self.numbers - p
            if self.numbers < 0:
                self.numbers = self.numbers + p
                print("ERROR")
            else:
                print("операция выполнена")
m01 = MetalBase("крст3", "круг", "сталь 3", 2)
m02 = MetalBase("крст45", "круг", "сталь 45", 6)
m03 = MetalBase("угст3", "уголок", "сталь 3", 10)
m04 = MetalBase("угст45", "уголок", "сталь 45", 3)
m05 = MetalBase("лсст3", "лист", "сталь 3", 8)
m06 = MetalBase("лсст45", "лист", "сталь 45", 2)
m07 = MetalBase("трст3", "труба", "сталь 3", 11)
m08 = MetalBase("трст45", "труба", "сталь 45", 9)
#m01.recomend(7)
#m01.operation(5)
#print(m01.numbers)