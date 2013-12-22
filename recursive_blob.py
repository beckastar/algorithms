import random

n = raw_input("How many columns and rows in your square grid?")
#create grid
n = int(n)

def create_mine_grid(n):
	mine_list = []
	while len(mine_list)<n:
		mine_list.append([]) 
	for i in range(n):
		while len(mine_list[i])<=n:
			mine_list[i].append('x')  
	maxmines = n**2
	# print maxmines
	minmines = n*2
	# print minmines
	# #determines number of mines
	print maxmines, minmines
	x = random.randrange(minmines, maxmines) 
	print "this is x", x
	#determines placement of mines
	while i<=x:
		mine_list[random.randrange(1, n)][random.randrange(1, n)] = "-"
		i+=1
	return mine_list

mine_grid = create_mine_grid(n)

def create_cover_grid(n):
	x_list = []
	for i in range(n):
		while len(x_list[i])<n:
			x_list[i].append('/')
	return x_list

cover_grid = create_cover_grid(n)

def print_cover_grid(cover_grid):
	for i in cover_grid:
		print i 

def get_x(n):
	x_coordinate = raw_input("what x coordinate would you like?")
	if x_coordinate > n:
		print("Try again.")
		take_user_guess()
	else:
		return x_coordinate

def get_y(n):
	y_coordinate = raw_input("input your y coordinate")
	if y_coordinate >n:
		print("Try again.")
		take_user_guess()
	else:
		return y_coordinate

get_x()
get_y()

x = get_x
y = get_y

def coords_to_grid(n, x, y, mine_grid):
	a = n-y
	b = x+1
	if mine_grid[a][b] == '-':
		return "This was a hit. Game over."
	else:
		return "No hit. You're still alive. Continue." 


# grid_list = []
# x_list = []
# for i in range(n):
# 	grid_list.append([])
# 	x_list.append([])
# for i in grid_list:
# 	i.append(range(n))
# for i in range(n):
# 	while len(x_list[i])<n:
# 		x_list[i].append('x')
# print grid_list
# print x_list
# for i in grid_list:
# 	print i 
# for i in x_list:
# 	print i

# x = 
 