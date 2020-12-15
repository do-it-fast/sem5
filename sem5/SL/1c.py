n = int(input("Enter number of elements"))

ls = []

def find_max(ls):
	if len(ls) == 1:
		return ls[0]
	else:
		return max(ls[0],find_max(ls[1:]))	

for i in range(n):
	ls.append(int(input()))
print(ls)
count = find_max(ls)
print(count)