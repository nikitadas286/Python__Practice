a=[1,2,3,4,5]
# sq=1
# b=[]
# for i in a:
#     sq=i*i
#     b.append(sq)
# print(b)

b=[x*x for x in range(1,len(a)+1)]
print(b)