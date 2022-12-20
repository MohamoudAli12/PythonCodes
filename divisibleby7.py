import pprint
list=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        list.append(str(i))
#pprint.pprint(list)
print(','.join(list))
