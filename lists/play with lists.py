L=[4,5,1,2,9,7,10,8]
print("Origanal list :",L)

count=0

for i in L:
    count += 1

avg = count/len(L)

print("sum=",count)
print("average=",avg)

L.sort()

print("The smallest element is",L[0])

print("The largest element is",L[-1])