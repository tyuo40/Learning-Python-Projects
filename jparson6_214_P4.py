#-------------------------------------------------------------------------------
# Name: John Parsons, jparson6, G00961220	
# Project 4
# Due Date: April 1st 2018 11:59PM
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (All zybooks and lectures)
#-------------------------------------------------------------------------------
# Comments and assumptions: 
#Assumptions-
#See projectbasics.pdf and Project4.pdf
#Comments-
#How elses can I do pos_if_rotated? It took me a really long time and it doesn't
#look very efficient. Overall project went well, passed 60/60.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
################################ FUNCTION 1 ####################################

def default_pos_of_shape(shape):
	coord = []
	if shape == 'I':
		coord = [(0,0),(1,0),(2,0),(3,0)]
	elif shape == 'O':
		coord = [(0,0),(1,0),(0,1),(1,1)]
	elif shape == 'T':
		coord = [(0,1),(1,0),(1,1),(2,1)]
	elif shape == 'J':
		coord = [(0,1),(0,0),(1,1),(2,1)] #Defines each shape's default 
	elif shape == 'L':
		coord = [(0,1),(2,0),(1,1),(2,1)]
	elif shape == 'S':
		coord = [(1,0),(2,0),(0,1),(1,1)]
	elif shape == 'Z':
		coord = [(0,0),(1,0),(1,1),(2,1)]
	return coord

################################ FUNCTION 2 ####################################

def pos_if_shifted(positions, shift):
	new = []
	for t in positions:
		mod = list(t)
		mod[0] = mod[0] + list(shift)[0] #Changes pos to list and adds shift 
		mod[1] = mod[1] + list(shift)[1]
		new.append(tuple(mod)) #Appends shifted values to empty list
	return new

################################ FUNCTION 3 ####################################

def pos_if_shifted_down(positions):
	newpos = pos_if_shifted(positions,(0,1))
	return newpos

################################ FUNCTION 4 ####################################

def pos_if_shifted_side(positions, go_left):
	if go_left == True:
		newpos = pos_if_shifted(positions,(-1,0))
	if go_left == False:
		newpos = pos_if_shifted(positions,(1,0))
	return newpos

################################ FUNCTION 5 ####################################

def pos_if_rotated(shape, positions, loc, number_rotations):
	count = 0
	origin = list(loc)
	origin[0] = (-origin[0])
	origin[1] = (-origin[1])
	displaced = pos_if_shifted(positions,(origin)) #New list of shape 
												   #returned to origin
	while count < number_rotations:
		if shape == 'I':
			displaced = pos_if_shifted(displaced, (-1,0)) #Offset for I shapes
		if shape == 'O':
			break
		new = []
		largest = 0
		for t in displaced:
			mod1 = list(t)
			mod2 = list(t)
			if mod1[0] > largest:
				largest = mod1[0]
			if mod1[1] > largest:
				largest = mod1[1]
			mod1[0] = (-mod1[1]) #Rotation around origin math
			mod1[1] = (mod2[0])
			new.append(mod1)
		
		count+=1
		new = pos_if_shifted(new,(largest,0))
		displaced = new
	
	final = pos_if_shifted(displaced,loc)


	return final
    
	
################################ FUNCTION 6 ####################################

def make_grid(width, height):
	grid = []
	count = 0
	while count < height:
		grid.append([]) #Create height lists
		count += 1
	for x in grid:
		count2 = 0
		while count2 < width:
			x.append(None) #Create width values
			count2 += 1
	
	return grid
	
################################ FUNCTION 7 ####################################

def is_valid_pos(grid, pos):
	valid = True
	height = (len(grid))-1
	width = len(grid[0])-1
	if list(pos)[0] > width: #If position is to wide
		valid = False
	if list(pos)[1] > height: #If position is to high
		valid = False 
	if (pos[0] or pos[1]) < 0: #If position is off the grid
		valid = False
	
	return valid

################################ FUNCTION 8 ####################################

def is_open_pos(grid, pos):
	valid = True
	if is_valid_pos(grid,pos) == False:
		valid = False
	elif grid[list(pos)[1]][list(pos)[0]] != None: #Check if positions are open
		valid = False
	return valid

################################ FUNCTION 9 ####################################

def set_positions(grid, positions, value):
	for x in positions:
		if is_valid_pos(grid,x) == True: #Checks if pos is valid and = value
			grid[list(x)[1]][list(x)[0]] = value
	return 

################################ FUNCTION 10 ###################################

def clear_positions(grid, positions):
	set_positions(grid,positions,None)
	return

################################ FUNCTION 11 ###################################

def can_place_at(grid, positions):
	valid = True 
	for x in positions:
		if is_open_pos(grid,x) == False:	#Checks if positions are open+valid
			valid = False
		if is_valid_pos(grid,x) == False:
			valid = False
	return valid

################################ FUNCTION 12 ###################################

def can_move_down(grid, positions):
	valid = True
	for x in positions:
		new = pos_if_shifted_down(positions) #Shift positions down by 1 vertical
	if can_place_at(grid, new) == False: #Checks if it can be placed
		valid = False
	return valid

################################ FUNCTION 13 ###################################

def can_move_side(grid, positions, go_left):
	valid = True
	for x in positions:
		new = pos_if_shifted_side(positions,go_left) #Shift positions left/right
	if can_place_at(grid, new) == False:  #Checks if new positions can be placed
		valid = False
	return valid

################################ FUNCTION 14 ###################################

def can_rotate(grid, shape, positions, loc, clockwise):
	valid = True
	if clockwise == True:
		new = pos_if_rotated(shape,positions,loc,1) #Clockwise is 1 rotation
		if can_place_at(grid, new) == False:
			valid = False
	if clockwise == False:
		new = pos_if_rotated(shape,positions,loc,3) #Counter-clock is 3 rots
		if can_place_at(grid, new) == False:
			valid = False
	return valid
################################ FUNCTION 15 ###################################

def get_complete_row_indexes(grid):
	full = []
	for i in range(len(grid)):
		count = 0
		for x in grid[i]:
			if x != None: #Checks if all of the items in the row are != to None
				count += 1
				if count == len(grid[i]):
					full.append(i) #Adds indexes of completed rows to list full
			
	return full

################################ FUNCTION 16 ###################################

def get_row(grid, y):
	new = grid[y] #Do I really need to explain this one? >_<
	return new
	
################################ FUNCTION 17 ###################################

def delete_row(grid, y):
	new = []
	count = 0
	grid[y] = grid[y:y+1] = [] #Deletes specified row
	while count < len(grid[0]):
		count += 1 
		new.append(None)
	grid[0:0]=[new] #Puts empty row on top of world grid 
	return 
	
################################ TETRIS! #######################################


