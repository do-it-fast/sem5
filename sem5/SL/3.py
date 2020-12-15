class senten:
	st = ""
	def __init__(self,st):
		self.st = st

	def rev(self):
		ls = list(self.st.split(" "))
		ls.reverse()
		new_st = ' '.join(ls)
		return new_st

def print_vow(ls2):
	for i in ls2:
		vow = 0
		count ={}
		fin = {}
		string = i.st.lower()
		print(type(string))
		for j in string:
			if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j=='u':
				vow = vow+1
		count[string] = vow
		
		#print(count)
		#fin.update(count)
	#print(fin)
	

#	a= sorted(count.items(),key = lambda x:x[1],reverse = True)
#	print(a)
st_class = senten("This is a test case")
st2_class = senten("hello world")
st3_class = senten("good morning")
ls2 = [st_class,st2_class,st3_class]
print_vow(ls2)
rev_string = st_class.rev()
print(rev_string)