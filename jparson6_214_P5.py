#-------------------------------------------------------------------------------
# Name: John Parsons, jparson6, G00961220	
# Project 5
# Due Date: 4/22/2018
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (All zybook chapters and lectures)
#-------------------------------------------------------------------------------
# Comments and assumptions: 
#Assumptions-
# See Project 5 pdf and Project basics
#
#
#
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------
print("""                                                                                                                                                                                                                                       
================================================================================

      #         #          #         #              #   # #     #   ######   
  ##########   ########   #######   ######## ########## # #     #            
  #        #  #    #     #     #   #       #       ##          #  ########## 
         ##  #    #     # #   #   #      ##      ## #         #        #     
       ##        #         ###         ##      ##   #       ##         #     
     ##         #         ##         ##      ##    ##     ##          #      
   ##          #        ##         ##               #   ##          ##      

      :::::::: ::::::::::: :::::::::  :::    ::: :::::::::: :::::::::   :::::::: 
    :+:    :+:    :+:     :+:    :+: :+:    :+: :+:        :+:    :+: :+:    :+: 
   +:+           +:+     +:+    +:+ +:+    +:+ +:+        +:+    +:+ +:+         
  +#+           +#+     +#++:++#+  +#++:++#++ +#++:++#   +#++:++#:  +#++:++#++   
 +#+           +#+     +#+        +#+    +#+ +#+        +#+    +#+        +#+    
#+#    #+#    #+#     #+#        #+#    #+# #+#        #+#    #+# #+#    #+#     
######## ########### ###        ###    ### ########## ###    ###  ########       



By J.C. Parsons 2018 v1.0

================================================================================

""")
def main():
	print("""
What would you like to do? (Press 'e' to ENCODE / Press 'd' to DECODE)
	""")
	while True:
		choice = input()
		if choice == 'e':
			print('E')
			break #Main function acts as a menu (unfinished)
		elif choice == 'd':
			print('D')
			break
		else:
			print('Invalid input, please try again.')
	return

########################## SUBSTITUTION CIPHER #################################

def is_valid_mapping(mapping):
	valid = True
	keyz = []
	valz = []
	for (k,v) in mapping.items():
		keyz.append(k)
		valz.append(v)
	lk = len(keyz)
	lv = len(valz)
	keyz = list(set(keyz))
	valz = list(set(valz))
	for x in range(len(keyz)):
		if x > 0:
			if len(keyz[x]) != len(keyz[x-1]): #Determines key lengths
				valid = False
	for x in range(len(valz)):
		if x > 0:
			if len(valz[x]) != len(valz[x-1]):#Determines value lengths
				valid = False
	if lk != len(keyz):
		valid = False
	if lv != len(valz):
		valid = False
	return valid

def is_valid_mapping_for_message(mapping, message):
    valid = True
    k = list(mapping.keys())
    l = len(k[0])
    new = []
    count = 0
    while count < len(message):
        end = count+l
        new.append(message[count:end])
        count += l
    new = list(set(new))
    num = 0
    for x in range(len(new)):
        for y in k:
            if new[x] == y: #Loops to check if any keys are = to message pieces
                num += 1
    if num != len(new):
        valid = False
    return valid
	
def reverse_mapping(mapping):
	new = {}
	keyz = []
	valz = []
	for (k,v) in mapping.items():
		keyz.append(k)
		valz.append(v)
	for x in range(len(mapping)):
		new[valz[x]] = keyz[x] #Creates reversed dictionary k/v pairs
	return new
	
def combine_mapping(mapping1, mapping2):
	new = {}
	keyz = []
	valz = []
	keyz2 = []
	valz2 = []
	for (k,v) in mapping1.items():
		keyz.append(k)
		valz.append(v)
		new[k] = v
	for (k,v) in mapping2.items():
		keyz2.append(k)
		valz2.append(v)
		new[k] = v
	for x in range(len(keyz)):
			for y in range(len(keyz2)):
				if keyz[x] == keyz2[y]:
					new = None #Checks for duplicates
	if mapping1 != {} and len(keyz[0]) != len(keyz2[0]):
		new = None 
	if mapping1 != {} and len(valz[0]) != len(valz2[0]):
		new = None
	return new

#def message_statistics(message, encoded_message):
#	stat = {}
#	m = []
#	for x in range(len(message)):
#		m.append(message[x])
#	for y in range(len(encoded_message)):
#		m.append(encoded_message[y])
#	m = list(set(m))
#	for x in range(len(m)):
#		stat[m]
#		
#	return stat
	

def substitution_encode(mapping, message):
	k = list(mapping.keys())
	v = list(mapping.values())
	l = len(k[0])
	new = []
	count = 0
	while count < len(message):
		end = count+l
		new.append(message[count:end]) #Creates list with chopped message parts
		count += l
	for x in range(len(new)):
		change = False
		for y in range(len(k)):
			if new[x] == k[y] and change != True:
				new[x] = v[y]
				change = True
	new = ''.join(new)        	
	return new

def substitution_decode(mapping, message):
	reverse = reverse_mapping(mapping) #Reverse mapping and decode
	new = substitution_encode(reverse, message)
	return new 

############################# CAESAR CIPHER ####################################

def get_caesar_mapping(shift, message):
	new = {}
	for x in range(len(message)):
		if ord(message[x])+shift > 126:
			mod = (ord(message[x])+ shift) - 95
			new[message[x]] = chr(mod)
		elif ord(message[x]) + shift < 32:
			mod = (ord(message[x]) + shift) + 95 #Shifts character per scenario
			new[message[x]] = chr(mod)
		else:
			new[message[x]] = chr(ord(message[x]) + shift)
	return new
	
def caesar_encode(shift, message):
	mapping = get_caesar_mapping(shift, message)
	new = substitution_encode(mapping, message)
	return new

def caesar_decode(shift, message):
	s = -shift
	mapping = get_caesar_mapping(s, message)
	new = substitution_encode(mapping, message)
	return new

########################## VIGINERE CIPHER #####################################

def vigenere_encode(secret, message):
	l = len(secret)
	count = 0
	new = ''
	for x in range(len(message)):
		if count == l:
			count = 0
		shift = ord(secret[count])-97 #Sets a to 0
		m = caesar_encode(shift, message)
		new = new + m[x]
		count += 1
	return new

def vigenere_decode(secret, message):
	l = len(secret)
	count = 0
	new = ''
	for x in range(len(message)): #Same as encode just shifting negatively
		if count == l:
			count = 0
		shift = ord(secret[count])-97
		m = caesar_encode(-shift, message)
		new = new + m[x]
		count += 1
	return new
	

########################## RAIL-FENCE CIPHER ###################################

#def rail_encode(num_rails, message):

#def rail_decode(num_rails, message): 





