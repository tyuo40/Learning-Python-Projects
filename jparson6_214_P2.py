#-------------------------------------------------------------------------------
# Name: John Parsons, jparson6, G00961220	
# Project 2
# Due Date: 2/18/18 11:59PM
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (zybook Chapter 1,2,3,4,5 content and lectures)
#-------------------------------------------------------------------------------
# Comments and assumptions: 
#Assumptions-
#
#
#Comments-
#Passed 10/52 tests with the first function. Passed 36/52 with second 
#function. 
#
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
################################ FUNCTION 1 ####################################

def check_special_time(start_hr, start_min, day):
	if 840<=((start_hr*60)+start_min)<=989 and 1<=day<=5:
		special = True
	else:
		special = False
	return special
	
################################ FUNCTION 2 ####################################

def get_hour_cost(num_children, num_adults, kids_eat_free, afternoon_special):
	if kids_eat_free == True:
		if num_children>num_adults:
			discountkids = (num_children-num_adults)
		else:
			discountkids = 0
		cost = (num_adults*20)+(discountkids*10)
	elif kids_eat_free == False:
		cost = (num_adults*20)+(num_children*10)
		
	kidcost = cost
	
	if afternoon_special == True:
		cost = (num_children*10+num_adults*20)*(.8)
	elif afternoon_special == False:
		cost = (num_children*10+num_adults*20)
	
	if kidcost<cost:
		cost = kidcost
	else:
		cost = cost
	return int(cost)	

################################ FUNCTION 3 ####################################

def get_order(day, start_hr,start_min,num_children,num_adults,num_hours):
	afternoon_special = check_special_time(start_hr, start_min, day)
	if (((num_children-num_adults)>0 or num_adults-num_children>=0)
	and day == 2):
		kids_eat_free = True
	else:
		kids_eat_free = False
	kef = kids_eat_free
		
	total = int(get_hour_cost(num_children, num_adults,kids_eat_free,
	afternoon_special)*(num_hours))
	
	if (afternoon_special == True) and (day == 2):
		message = "Tuesday afternoon, best deal! Total: $" + str(total) 
	elif (afternoon_special == False) and (kef == True):
		message = "Kids eat free special! Total: $" + str(total) 
	elif (afternoon_special == True) and (kef == False):
		message = "Afternoon special! Total: $" + str(total)  
	elif (afternoon_special == False) and (kef == False):
		message = "Total: $" + str(total)  
	
	return message
	


#################################### END OF PROGRAM ############################
