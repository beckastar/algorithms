d = {"Sam": 27, "Sara":22, "Andrew":41, "James":22, "Rose":27}

def transform(d):
	new_d ={}
	for k in d:
		new_d[d[k]] =[]
	for k in d:
		new_d[d[k]].append(k)
	return new_d
 
  