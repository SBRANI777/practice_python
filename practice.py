list1=["apple","cherry","mango"]
list2=[10,20,30]
dict1=[(i,j) for i,j in  zip(list1,list2)]
print(dict(dict1))