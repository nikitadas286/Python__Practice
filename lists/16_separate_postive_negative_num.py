a=[10,20,-74,30,40,50,-10,-31]
positive=[]
negative=[]
for i in a:
    if(i>=0):
        positive.append(i)
    else:
        negative.append(i)
print("Positive part:",positive)
print("Negative part:",negative)