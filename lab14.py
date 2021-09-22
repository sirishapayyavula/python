from itertools import chain
test_list = [(11, 4), (3, 9), (1, 10), (95, 2)]
print("The original list is : " + str(test_list))
temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for sub in temp:
	for ele in sub:
		res.add(ele)
print("The extracted digits : " + str(res))
