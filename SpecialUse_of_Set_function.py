li = [1, 2 , 3,4,5,6,78,78,56,2,5,1,3,5]
print(len(li))
print(set(li))
print(li)

for l in set(li):
    print(l, ': ', li.count(l))
