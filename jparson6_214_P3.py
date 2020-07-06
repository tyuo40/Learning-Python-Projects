#-------------------------------------------------------------------------------
# Name: John Parsons, jparson6, G00961220	
# Project 3
# Due Date: 3/4/2018
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (zybook Chapter 1-8 content and lectures)
#-------------------------------------------------------------------------------
# Comments and assumptions: 
#Assumptions-
# See Project 3 pdf
#
#Comments-
#Used Python Visualizer to assist me, had a very difficult time on Function 4
#total cases passed 73/80
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
################################ FUNCTION 1 ####################################

def sum_mult_in_range(start, end, m):
	output = 0
	xs = range(start,(end+1),1)	
	for num in xs:
		if num%m==0: #Determines whether or no the number is a multiple
			output += num
	return output 

################################ FUNCTION 2 ####################################

def find_first_starts_with(list, start_str):
	output = None
	for word in range(len(list)):
		if list[word][0:len(start_str)] == start_str: #Make strings same length
			output = list[word] #Compares the given string with list for matches
			break
	return output

################################ FUNCTION 3 ####################################

def find_all_starts_with(list, start_str):
	output = []
	for word in range(len(list)):
		if list[word][0:len(start_str)] == start_str:
			output.append(list[word]) #Adds all findings to list
	return output

################################ FUNCTION 4 ####################################

def get_invalid_colors(list):
	xs = []
	x = 0
	n = 0
	for color in list:
		invalid = False
		if n == 3:
			x+=1
		n = 0
		for num in color:
			if invalid == True:
				x+=1
				
			if num<0 or num>255: #Determines whether color is valid integer
				invalid = True
				if invalid == True:
					xs.append(x)
					x+=1
			else: #Counts amount of times loop is cycled
				n+=1
			
	return xs

################################ FUNCTION 5 ####################################

def smallest_above_after_div(original, smallest, divisor):
	num = original/divisor 
	while (num/divisor)>smallest: #Continually divides to get the number
			num = num/divisor

	return num
	
################################ FUNCTION 6 ####################################

def simple_board(size):
	divider = '+'
	pipes = '|'
	count = 0
	
	while count < size: #Loops and creates correctly sized lines for board
		pipes = pipes+' |'
		divider= divider+'-+' 
		count += 1
	
	output = ''
	if size == count:
		body = str(divider + '\n' + pipes + '\n')*(size) #Creates iterable body
		output = str(body + divider) #Adds ending divider
		
	return output

################################ PROGRAM END ###################################