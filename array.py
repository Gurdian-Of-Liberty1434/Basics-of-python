import array as arr

array_num=arr.array('i',[1, 3, 5, 3, 7, 9, 3])
print("origanal array"+str(array_num))
print("Number of occurance of 3 is "+str(array_num.count(3)))

array_num.reverse()
print("Reversed order of the array:")
print(array_num)