#-------------------------------------------------------------------------------
# Name: John Parsons, jparson6, G00961220	
# Project 1
# Due Date: 2/4/18 11:59PM
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (zybook Chapter 1+2 content, lectures)
#-------------------------------------------------------------------------------
# Comments and assumptions: 
#Assumptions-
#1. The user will always enter an integer when we ask for an integer, a string 
#when we ask for a string, etc.
#2. The user will only answer with usable values. Diameters won’t have negative 
#distances, inner cutouts won’t be larger than wheels, etc. We are assuming the
#user behaves, so your program doesn't need to
#identify or address these kinds of situations.
#3. We assume the millimeters and cents will be the smallest units input (and
#will therefore have integer values). So there will be no inputs of 0.5 cents,
#0.25 mm, etc.
#
#Comments-
#I had a lot of trouble with the tester at first because I paraphrased
#the questions and statements in the program. After resolving this, I passed
#9/10 of the tests. The final test was passed by changing Q1 and Q2 inputs to 
#float values instead of integers.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#------------------------------------------------------------------------------- 
pi = 3.14										    #Created two variables to be
wheel_volume = 0								    #used in calculating initial 
#                                                   #wheel volume             
print('------------------------------')			                    #Format line

############################# SECTION 1 END ####################################
q1 = 'What is the diameter of the wheel (in centimeters)? '                  #Q1

wheel_diam = float(input(q1))         #Q1 Displayed/Input assigned to wheel_diam

q2 = 'How thick is the wheel (in millimeters)? '                             #Q2

wheel_thick = float(input(q2))       #Q2 Displayed/Input assigned to wheel_thick

radius = ((wheel_diam*10)/2)         #Converts given cm diameter to radius in mm

height = wheel_thick   #Makes wheel_thick equal to height for volume calculation

wheel_volume = pi*(radius**2)*height     #Calc. volume of the wheel using inputs
 
print('The volume of the wheel without the inner cutout is:' , 
int(wheel_volume) , 'mm^3')					       #Displays volume of the wheel
 
print('------------------------------')                             #Format line

############################# SECTION 2 END ####################################
q3 = ('What is the ratio of the inner cutout diameter (as a decimal)? ')     #Q3
 
cutout_ratio = float(input(q3))     #Q3 Displayed/Input assigned to cutout_ratio

cut_volume = (pi*((cutout_ratio*radius)**2)*height)         #Cutout volume calc.

wheel_volume_new = (wheel_volume) - (cut_volume)   #Calc. wheel w/ cutout volume

print('The volume of the inner cutout is:' , int(cut_volume) , 'mm^3')
#                                                        #Displays cutout volume

print('The volume of the wheel with cutout is:' , 
int(wheel_volume_new) , 'mm^3')          #Displays wheel volume with cut removed
#                                    
print('------------------------------')                             #Format line

############################# SECTION 3 END ####################################
q4 = 'How many wheels are you making? '                                      #Q4

wheel_num = int(input(q4))             #Q4 Displayed/Input assigned to wheel_num

q5 = 'What is the cost of the material (in cents per cubic inch)? '          #Q5

cost = int(input(q5))                       #Q5 Displayed/Input assigned to cost

total_mat = int(wheel_volume_new*wheel_num)    #Calc. total material in mm^3 and
#                                              #assigns result to total_mat 

inch_per_side = ((total_mat**(1/3))/(25.4))             #Converts mm^3 to inches

total_cub = inch_per_side**3   #Cubes the side length (in inches) to create in^3

total_cents = (cost*int(total_cub+1)-int(int(total_cub+1)-total_cub))%100
#          #Calculates the amount of change in cents needed to purchase material

total_dollars = (cost*int(total_cub+1)-int(int(total_cub+1)-total_cub))//100
#                    #Calculates the cost in dollars needed to purchase material

print('The total material needed is:' , total_mat , 'mm^3')
#                            #Displays the total amount of material need in mm^3

print('The total number of cubic inches to purchase is:' ,
int(total_cub+1)-int(int(total_cub+1)-total_cub) , 'cube(s)')
#      #Displays the number of cubes needed to make the desired amount of wheels

print('The cost will be:' , 
int(total_dollars+1)-int(int(total_dollars+1)-total_dollars) , 'dollar(s)' ,
'and' , int(total_cents+1)-int(int(total_cents+1)-total_cents) ,
'cent(s)!')
#            #Displays the total cost in dollars in cents of the material needed

print('------------------------------')                             #Format line

############################# SECTION 4 END ####################################
 
 
