unordered_list = [1, 4, 1, 6, "hello", "a", 5, "hello"]
duplicate_elements = []
x1 = 0
x2 = 0
for i in unordered_list:
	x1 = i
	unordered_list.remove(i)
	for k in unordered_list:
		x2 = k
		if x1 == x2:
			duplicate_elements.append(x1)
print(duplicate_elements)