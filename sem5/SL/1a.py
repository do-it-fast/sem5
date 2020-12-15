def remove_dups(lis):
	res = []
	for i in lis:
		if i not in res:
			res.append(i)
	return res	



n  = int(input("Enter number of elements"))
ls = []

for i in range(n):
	i = input("Enter elements")
	ls.append(i)
print(ls)
new_ls = remove_dups(ls)
print(new_ls)
even_ls = [x for x in range(n) if x%2 == 0]
print(even_ls)
ls.reverse()
rev_lis = ls
print(rev_lis)