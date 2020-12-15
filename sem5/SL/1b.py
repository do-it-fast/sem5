import pprint
file= open("test.txt",'r')
f= list(file.read().split(" "))
count = {}

for i in f:
	
	if i not  in count:
		count[i] = 1
	else:
		count[i] +=1
pprint.pprint(count)
