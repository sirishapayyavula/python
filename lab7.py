list1 = [10, 20, 4, 45, 99]

a=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
	if list1[i]>a:
		secondmax=a
		a=list1[i]
	elif list1[i]>secondmax and \
		a != list1[i]:
		secondmax=list1[i]

print("Second highest number is : ",\
      str(secondmax))
