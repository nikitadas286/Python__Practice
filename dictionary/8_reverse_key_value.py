d={"a":10,"b":20,"c":30,"d":40}
rev={}
for key,val in d.items():
    rev[val]=key
print(rev)