
lst = [[1,2,3], [4,5,6],[7,8,9]]


def get_averages(lists):
	avgs = []
	for l in lists:
		s =0 
		for i in l:
			s += i
			a = s/len(l)
			avgs.append(a)
	return avgs

def find_largest(l):
	big = l[0]
	for i in l[1:]:
		if i > big:
			big = i
	return big


lst = [[1,2,3], [4,5,6],[7,8,9]]
print find_largest(get_averages(lst))
		