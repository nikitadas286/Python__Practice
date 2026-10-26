a=[45,12,74,65,25,10]
b=[52,10,23,96,100]
c=a+b
print(c)
# for i in range(1,len(c)):
#     for j in range(i+1,len(c)):
#         if(c[i]>c[j]):
#             temp=c[i]
#             c[i]=c[j]
#             c[j]=temp
#         else:
#             j+=1
# print(c)
c.sort()
print(c)