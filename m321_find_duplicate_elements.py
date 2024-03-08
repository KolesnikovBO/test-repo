unordered_list = [1, 4, 1, 6, "hello", "a", 5, "hello"]
duplicate_elements = []
for i in unordered_list:
	unordered_list.remove(i)
	for k in unordered_list:
		if i == k:
			duplicate_elements.append(i)
print(duplicate_elements)