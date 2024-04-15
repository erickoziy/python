MetalBase = {"01крст3":2, "02крст45":5, "03угст3":4, "04угст45":7, "05лсст3":8, "06лсст45":2}
print (MetalBase)
print (MetalBase["01крст3"])
MetalBase["02крст45"]=6
MetalBase["03угст3"]=10
MetalBase["04угст45"]=3
print (MetalBase)
MetalBase["07трст3"]=11
MetalBase["08трст45"]=9
print (MetalBase)
MetalBase["04угст45"]=[]
print (MetalBase)
i=MetalBase["01крст3"]
if i <= 5:
    print ("нужно докупить")
elif i > 5:
    print ("всё в порядке")