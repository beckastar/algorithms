import random
# n = raw_input("How large should your square grid be? Choose a number between 1 and 10.")
# n = int(n)

n=7

def create_mine_grid(n):
	mine_list = []
	while len(mine_list)<n:
		mine_list.append([]) 
	for i in range(n):
		while len(mine_list[i])<=n:
			mine_list[i].append('x') 
	return mine_list 


mine_grid = create_mine_grid(n)

def populate_with_bombs(mine_grid):
	maxmines = n*2
	minmines = n*1 
	# #determines number of mines 
	x = random.randrange(minmines, maxmines)  
	#determines placement of mines
	for i in range(n):
		while i<=x:
			mine_grid[random.randrange(0, n)][random.randrange(0, n+1)] = "b"
			i+=1
	return mine_grid

mine_grid_bombs = populate_with_bombs(mine_grid)

def print_mine_grid(mine_grid_bombs):
	for i in mine_grid:
		yield(i)

print_mine = print_mine_grid(mine_grid)

for i in print_mine:
	print i 

def get_positions(mine_grid, item):
    if isinstance(mine_grid, list):
        for i, it in enumerate(mine_grid):
            for pos in get_positions(it, item):
                yield (i,) + pos
    elif mine_grid == item:
        yield ()

finder = get_positions(mine_grid, 'b')

def get_bomb_list(mine_grid, bomb):
	bombs = []
	for bomb in finder:
		bombs.append(bomb)
	return bombs

bomb_list = get_bomb_list(mine_grid, 'b')
print bomb_list 

def check_neighbors(bomb_list, popped): 
	count = 0
	for i in range(-1, 2):
		for bomb in bomb_list:
			if bomb[0]+i==popped[0] and bomb[1]==popped[1]:
				count +=1 
				bomb_list.remove(bomb)
				check_neighbors(bomb_list, popped) 
			if bomb[0]==popped[0] and bomb[1]==popped[1]+i:
				count +=1 
				bomb_list.remove(bomb)
				check_neighbors(bomb_list, popped)
			if bomb[0]+i==popped[0] and bomb[1]+i == popped[1]:
				count+=1
				bomb_list.remove(bomb)
				check_neighbors(bomb_list, popped)
	return count 

check_neighbors = check_neighbors(bomb_list, popped)

def through_list(bomb_list, popped, check_neighbors):
	all_counts = []
	while len(bomb_list)>0:
		for bomb in bomb_list:
			popped = bomb_list.pop()
			all_counts.append(check_neighbors)




# def convert_coordinates(get_bomb_list):
# 	for bomb in bombs:
# # 	bomb[a][b] = bomb[][]
# def create_new_list(bomb_list, n):
# 	# x= b-1
# 	# y= n-a
# 	xy_list = []
# 	for bomb in bomb_list:
# 		xy_list.append([])
# 	for bomb in bomb_list:
# 		print bomb[0]
# 		for coordinate in xy_list:
# 			coordinate[0] = bomb[1]-1
# 			coordinate[1] = n - bomb[0]
# 	return xy_list

# xy_list = create_new_list(bomb_list, n)
# for i in xy_list:
# 	print i
  

	# #if x == 0 and y == 1

	# if mine_grid[x+1][y] == 'b':

	# if mine_grid[x-1][y] == 'b':


	# if mine_grid[x+1][y+1] == 'b'
	# 	blobs[count]+=1


# gameplay below 

# def create_cover_grid(n):
# 	x_list = []
# 	while len(x_list)<n:
# 		x_list.append([])
# 	for i in range(n):
# 		while len(x_list[i])<=n:
# 			x_list[i].append('/')
# 	return x_list

# x_list = create_cover_grid(n)

# def modify_cover_grid(cover_grid, a, b):
# 	x_list[a][b] = '/'

# def print_cover_grid(cover_grid):
# 	for i in cover_grid:
# 		print i 

# def alter_cover_grid(cover_grid, a, b):
# 	x_list[a][b] = 'o'
# 	return x_list

# #create a class to take care of these two functions and not repeat. 
# def get_x(n):
# 	x_coordinate = raw_input("what x coordinate would you like?")
# 	x_coordinate = int(x_coordinate)
# 	if x_coordinate <= n:
# 		return x_coordinate
# 	else:
# 		print "try again"
# 		get_x(n)

# def get_y(n):
# 	y_coordinate = raw_input("input your y coordinate")
# 	y_coordinate = int(y_coordinate)
# 	if y_coordinate <= n:
# 		return y_coordinate
# 	else:
# 		print "try again"
# 		get_y(n)

 

# def coords_to_grid(n, mine_grid, cover_grid):
# 	x = get_x(n)
# 	y = get_y(n) 
# 	a = n-y
# 	b = x-1
# 	if mine_grid[a][b] == 'b':
# 		print "This was a hit. Game over."
# 		for i in mine_grid:
# 			print i
# 	else:
# 		print "You did not uncover a bomb. You're still alive! Continue."
# 		#alter cover grid
# 		alter_cover_grid(x_list, a, b)
# 		for i in x_list:
# 			print i 
# 		coords_to_grid(n, mine_grid, cover_grid)

# coords_to_grid(n, mine_grid, x_list)

 