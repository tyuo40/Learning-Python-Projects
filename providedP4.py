import platform
import imp

from graphics import *
from time import *
from random import *

##############################################
## settings for the actual game
##############################################

# how long to wait before moving down automatically (2 seconds)
delay = 2

# when they get 100 points, how much to speed up
delay_inc = 0.02

# how tall the world is
height = 20.0 

# how wide the world is
width = 10.0 

# how many pixels wide/tall a square is
box_pixel_size = 30 

# valid shape abbreviations
shapes = "OITLJSZ" 

# uncomment this if you want always play the same game over and over
#seed(0) 

# how many points for placing a single tetromino
piece_score = 10 

# how many points for completing a line
line_score = 100 

# points multiplier for completing four lines at once
four_multiplier = 2 

##############################################
## current game scores
##############################################

# starting score
score = 0 

# keep track of how many points earned since last speed up
score_since_inc = 0 

# score text box settings
score_text = Text(Point((width//2),1), "Score: " + str(score))
score_text.setTextColor("Blue")
score_text.setStyle("bold")

##############################################
## Plays a game of patchwork tetrominoes!
##############################################

def play_game(show_score, show_hint):
	'''Actually play a game. show_score should be set to true if scoring.'''

	global delay, height, width, shapes, score
	
	# import helper code written by students
	import student

	# draw a window
	win = GraphWin('tetrominoes', width*box_pixel_size,
		height*box_pixel_size, autoflush=False)
	win.setBackground("white")

	# set up the coordinate system (0,0) is upper left, 
	# (width-1, height-1) is lower right
	win.setCoords(0.0, height, width, 0.0)

	# make grid with items listed
	grid = student.make_grid(int(width),int(height))
	
	# draw dots in a grid
	for x in range(int(width)):
		for y in range(int(height)):
			win.plot(x, y, "blue")
	
	# draw the score text if we're keeping score
	if show_score:
		update_score(win, grid, True)
		
	# store "phantom" tetromino if we're giving hints
	tetr_hint = None
	
	# outer loop controls the dropping of tetrominoes
	while(True):
		# get a random tetromino
		s_index = randint(0,len(shapes)-1)
		
		# make "phantom" graphical representation if we're doing hints
		if show_hint:
			# undraw the last hint
			if tetr_hint != None:
				tetr_hint.undraw_all()
			
			# figure out if there is a new hint
			hint_pos = student.pos_for_hint(grid, shapes[s_index])
			if hint_pos != None:
				hint_color = 100
				tetr_hint = Tetromino(win, hint_pos, (hint_color, hint_color, hint_color))
				# print("hint: " + str(hint_pos))
			else:
				tetr_hint = None
		
		# move shape over to the center to start
		
		# determine where the center is
		shift = int(width//2)-2
		if shapes[s_index] == "O":
			shift += 1
			
		# keep track of the offset of the piece from center as it moves
		tetr_loc = [shift,0]
			
		# get positions for the shape and shift them over
		positions = student.default_pos_of_shape(shapes[s_index])
		positions = student.pos_if_shifted(positions, tetr_loc)
		
		# make graphical representation
		tetr = Tetromino(win, positions)
		
		# end game if not a valid position
		if not student.can_place_at(grid, positions):
			text = "GAME OVER!"
			if show_score:
				text += "\nScore: " + str(score)
			score_text.setText(text)
			score_text.undraw()
			score_text.draw(win)
			update()
			while(win.getKey() != "Escape"):
				pass
			win.close()
			quit()
		
		# keep track of time so we know when to lower the piece
		t = time()
		
		# inner loop controls 
		while True:
			# make score display on top of other things
			if show_score:
				score_text.undraw()
				score_text.draw(win)
			
			# "pulse" the hint
			if show_hint and tetr_hint != None:
				hint_color += 1
				if hint_color > 200:
					hint_color = 100
				tetr_hint.update_color((hint_color, hint_color, hint_color))
		
			# possibly moving the tetromino, so take off grid
			# if we don't do this, the tetromino could bump into
			# itself
			student.clear_positions(grid, tetr.positions)
			
			# determine if it's time to lower the tetromino automatically
			curT = time()
			if curT - t > delay:
				# if they can move down, then do so
				if student.can_move_down(grid, tetr.positions):
					tetr.move(student.pos_if_shifted_down(tetr.positions))
					tetr_loc[1] += 1
					t = curT
				# otherwise finish moving the tetromino
				else:
					# put graphics boxes on grid so we can undraw boxes later
					for i in range(len(tetr.positions)):
						student.set_positions(grid, (tetr.positions[i],),
							tetr.boxes[i])
					
					# update the scores
					if(show_score):
						update_score(win, grid)
					
					# update graphics
					update()
					
					# exit loop so we can drop another tetromino
					break
			
			# maybe the user wanted to move the tetromino?
			else:
				key = win.checkKey()
				# if key != "":
				#	print(key)
				
				# determine what the user wanted to do and do it
				if key == "Left" or key == "a" or key == "A":
					if student.can_move_side(grid, tetr.positions, True):
						tetr.move(student.pos_if_shifted_side(
							tetr.positions, True))
						tetr_loc[0] -= 1
				elif key == "Right" or key == "d" or key == "D":
					if student.can_move_side(grid, tetr.positions, False):
						tetr.move(student.pos_if_shifted_side(
							tetr.positions, False))
						tetr_loc[0] += 1
				elif key == "Down" or key == "s" or key == "S":
					if student.can_move_down(grid, tetr.positions):
						tetr.move(student.pos_if_shifted_down(
							tetr.positions))
						tetr_loc[1] += 1
				elif key == "Up" or key == "w" or key == "W":
					while student.can_move_down(grid, tetr.positions):
						tetr.move(student.pos_if_shifted_down(
							tetr.positions))
						tetr_loc[1] += 1
					# trigger timeout for a new tetromino
					t -= delay
				elif key == "e" or key == "E":
					if student.can_rotate(grid, shapes[s_index], 
						tetr.positions, tetr_loc, True):
						tetr.move(student.pos_if_rotated(
							shapes[s_index], tetr.positions, tetr_loc, 1))
				elif key == "q" or key == "Q":
					if student.can_rotate(grid, shapes[s_index], 
						tetr.positions, tetr_loc, False):
						tetr.move(student.pos_if_rotated(
							shapes[s_index], tetr.positions, tetr_loc, 3))
				elif key == "Escape":
					win.close()
					quit()
				
			# we've finish moving tetromino, put it back on grid
			student.set_positions(grid, tetr.positions, shapes[s_index])
			
			# update graphics
			update()


##############################################
## Keep track of the score and drawing it
##############################################

def update_score(win, grid, first_time = False):
	'''	Clears rows of tetrominoes.
		Speeds up the game.
		Updates and re-draws the current score.
		Called after each tetromino drop.
	'''
	global score, score_since_inc, piece_score, delay
	
	# draw score on top of everything
	score_text.undraw()
	score_text.draw(win)

	if first_time:
		return
		
	# update the score
	clear_score = clear_full_rows(grid)
	score += piece_score + clear_score
	score_text.setText("Score: " + str(score))
	
	# speed up the game if need be
	score_since_inc += piece_score + clear_score
	while score_since_inc >= 100:
		delay -= delay_inc
		score_since_inc -= 100


##############################################
## Clears out full rows of tetrominoes
##############################################

def clear_full_rows(grid):
	''' Handles all the clearing of tetrominoes.
		Deals with the graphics and also updates collision grid.
		Returns score from completed rows.
	'''
	global line_score, four_multiplier

	# need student helper code for this.
	import student
	
	# determine if any rows are full
	rows = student.get_complete_row_indexes(grid)
	
	# undraw graphical representation of boxes we need to remove
	for y in rows:
		row = student.get_row(grid, y)
		for box in row:
			box.undraw()
	
	# shift values down in collision grid
	shift_value = 0
	for y in range(len(grid)-1, -1, -1):
		# delete rows from collision grid
		while y-shift_value in rows:
			student.delete_row(grid, y)
			shift_value += 1
		
		# update graphics
		row = student.get_row(grid, y)
		for value in row:
			if type(value) == Rectangle:
				value.move(0,shift_value)
	
	# determine score for clearing the rows
	total = len(rows)
	return len(rows) * line_score * (four_multiplier if total == 4 else 1)
	

##############################################
## This is a demo environment for incomplete games
##############################################

def show_a_grid(place_tetrominoes, allow_interactions):
	'''Demo environment while developing the game.'''
	
	global shapes
	
	# import helper code written by students
	import student

	# set up world size
	grid_size_w = 30
	grid_size_h = 10

	# draw a window
	win = GraphWin('tetrominoes', grid_size_w*box_pixel_size, grid_size_h*box_pixel_size,
		autoflush=False)
	win.setBackground("white")
	
	# set up the coordinate system (0,0) is upper left, 
	# (grid_size_w-1, grid_size_h-1) is lower right
	win.setCoords(0.0, grid_size_h, grid_size_w, 0.0)
	
	# draw dots in a grid
	for x in range(int(grid_size_w)):
		for y in range(int(grid_size_h)):
			win.plot(x, y, "blue")
			
	# draw instructions
	text = "Hit Escape to close."
	if allow_interactions:
		text += "\nUp/Down/Left/Right or W/S/A/D keys move. Q/E keys rotate."
		text += "\nIn full game Up or W will \"drop\" tetrominoes."
	instructions = Text(Point(grid_size_w//2,1), text)
	instructions.setTextColor("Blue")
	instructions.setStyle("bold")
	instructions.draw(win)

	# place some demo tetrominoes
	if(place_tetrominoes):
		# keep a list of tetrominoes and their offsets for later
		tetrs = []
		tetr_locs = []
		
		shift_y = 5
		shift_x = 2
		for i in range(len(shapes)):		
			# show each shape shifted over for demo
			tetr_locs.append([shift_x, shift_y])
			
			if shapes[i] == 'O':
				shift_x += 3
			elif shapes[i] == 'I':
				shift_x += 5
			else:
				shift_x += 4
			
			# get positions for the shape and shift them over
			positions = student.default_pos_of_shape(shapes[i])
			positions = student.pos_if_shifted(positions, tetr_locs[i])
			
			# make graphical representation
			tetrs.append(Tetromino(win, positions))
	
	# are we demoing motion?
	if(allow_interactions):
		while True:
			key = win.checkKey()
			# if key != "":
			#	print(key)
			
			# determine what the user wanted to do and do it
			if key == "Left" or key == "a" or key == "A":
				for i in range(len(tetrs)):
					tetr = tetrs[i]
					tetr.move(student.pos_if_shifted_side(tetr.positions, True))
					tetr_locs[i][0] -= 1
			elif key == "Right" or key == "d" or key == "D":
				for i in range(len(tetrs)):
					tetr = tetrs[i]
					tetr.move(student.pos_if_shifted_side(tetr.positions, False))
					tetr_locs[i][0] += 1
			elif key == "Down" or key == "s" or key == "S":
				for i in range(len(tetrs)):
					tetr = tetrs[i]
					tetr.move(student.pos_if_shifted_down(tetr.positions))
					tetr_locs[i][1] += 1
			elif key == "Up" or key == "w" or key == "W":
				for i in range(len(tetrs)):
					tetr = tetrs[i]
					tetr.move(student.pos_if_shifted(tetr.positions, (0,-1)))
					tetr_locs[i][1] -= 1
			elif key == "e" or key == "E":
				for i in range(len(tetrs)):
					tetr = tetrs[i]
					tetr.move(student.pos_if_rotated(shapes[i], tetr.positions, tetr_locs[i], 1))
			elif key == "q" or key == "Q":
				for i in range(len(tetrs)):
					tetr = tetrs[i]
					tetr.move(student.pos_if_rotated(shapes[i], tetr.positions, tetr_locs[i], 3))
			elif key == "Escape":
				win.close()
				quit()
					
			update()
	else:
		update()
		while(win.getKey() != "Escape"):
			pass
		win.close()
		quit()
		

##############################################
## Represents a tetromino graphic
##############################################

class Tetromino():

	# locs is list of four x,y tuples
	def __init__(self, win, locs, color=None):
		''' Sets up the tetromino graphics.'''
		
		self.positions = locs
		self.boxes = []
		for loc in locs:
			box = Rectangle(Point(loc[0],loc[1]), Point(loc[0]+1,loc[1]+1))
			
			if color != None:
				# don't use full range to avoid white
				c = "#"+("%02x%02x%02x"%(color[0],color[1],color[2]))
				box.setFill(c)
				box.setOutline(c)
			else:
				# don't use full range to avoid white
				box.setFill("#"+("%02x%02x%02x"%(randint(0,230),randint(0,230),randint(0,230))))
				box.setOutline("#888888")
				
			box.draw(win)
			self.boxes.append(box)
			
	def move(self, locs):
		''' "Moves" the graphical representation.
			No collision detection for graphics...
		'''
		for i in range(len(locs)):
			dx = locs[i][0] - self.boxes[i].getP1().getX()
			dy = locs[i][1] - self.boxes[i].getP1().getY()
			self.move_box(self.boxes[i], dx, dy)
		self.positions = locs

	def move_box(self, box, dx, dy):
		''' "Moves" one box of the tetromino.
			No collision detection for graphics...
		'''
		global width, height
	
		box.move(dx,dy)
		
		x = box.getP1().getX()
		y = box.getP1().getY()
		# if x < 0 or x > width-1 or y < 0 or y > height-1:
		# 	raise Exception("Tetromino out of bounds!")

	def update_color(self, color):
		for box in self.boxes:
			c = "#"+("%02x%02x%02x"%(color[0],color[1],color[2]))
			box.setFill(c)
			box.setOutline(c)
			# box.undraw()
			# box.draw(win)

	def undraw_all(self):
		for box in self.boxes:
			box.undraw()
			

##############################################
## Gets student code from their file
##############################################	

def import_student_code(filename):
	'''Gets student code from file into module "Student"'''
	f = open(filename)
	code = f.read()
	f.close()
	
	module = imp.new_module("student")
	sys.modules["student"] = module
	exec(code, module.__dict__)
	
	return module
	

##############################################
## Main method - handles command line args
##############################################
def main():
	global python_command
	
	python_command = "python" if platform.system() == 'Windows' else "python3"

	if len(sys.argv) < 2:
		raise Exception("needed student's file name as command-line argument:" \
			+ "\n\t\""+python_command+" provided.py gmason76_2xx_Px.py stage\"")
	
	# get student code
	import_student_code(sys.argv[1])
	
	# run whichever stage student wants to test
	if(len(sys.argv) < 3 or sys.argv[2] == '0'):
		show_a_grid(False, False)
	elif(sys.argv[2] == '1'):
		show_a_grid(True, False)
	elif(sys.argv[2] == '2'):
		show_a_grid(True, True)
	elif(sys.argv[2] == '3'):
		play_game(False, False)
	elif(sys.argv[2] == '4'):
		play_game(True, False)
	elif(sys.argv[2] == '5'):
		play_game(True, True)


##############################################
## Play the game if this file is called directly
##############################################
if __name__ == "__main__":
	main()
