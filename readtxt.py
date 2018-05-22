filename = "56.txt"
mynumbers = [] 
real_line=[]
with open(filename) as f:
	for line in f:
		split_line=line.strip().split(",")
		split_line[:] = [item for item in split_line if item != ""]
		#print split_line
		
		#print "---"
		
		mynumbers.append(split_line)
	#print mynumbers
	print "---"
print len(mynumbers) #number of rows n file (12)
print len(mynumbers[0]) #number of objects in each row (54)

top =[]
bottom =[]
for i in range(12):
	if i <=5:
		top.append(mynumbers[i])
	else:
		bottom.append(mynumbers[i])

print len(top) #number of rows n file (12)
print top
print "-----"
#print len(bottom) 


#crate words from top. start raeding from top, then from bottom and again from top
top_words = []

for i in range (len(top[0])):
	
	if i%2 == 0:

		word = []
		for line in top:
			word.append(line[i])
		top_words.append(word)	
	else:
		word = []
		for line in top:
			word.insert(0,line[i])	
		top_words.append(word)			
print top_words #words is the list of words of top

#crate words from top. start raeding from top, then from bottom and again from top
bottom_words = []

for i in range (len(bottom[0])):
	
	if i%2 == 0:

		word = []
		for line in bottom:
			word.append(line[i])
		bottom_words.append(word)	
	else:
		word = []
		for line in bottom:
			word.insert(0,line[i])	
		bottom_words.append(word)			
print bottom_words #words is the list of words of top

print "++++++++++++++"
key = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","y","Z"]
#print key

top_letter_values=[]
for six_bit in top_words:
	letter = 0
	for bit in range (len(six_bit)): 
		letter+=int(six_bit[bit])*2**((bit))
		#print int(six_bit[bit])*(2**(bit))
		#print (";;;")
	top_letter_values.append(letter)

#print top_letter_values

top_letters = []
for letter_value in top_letter_values:
	top_letters.append(key[letter_value])
#print top_letters


bottom_letter_values=[]
for six_bit in bottom_words:
	letter = 0
	for bit in range (len(six_bit)): 
		letter+=int(six_bit[bit])*2**((bit))
		#print int(six_bit[bit])*(2**(bit))
		#print ("------")
	bottom_letter_values.append(letter)

#print bottom_letter_values

bottom_letters = []
for letter_value in bottom_letter_values:
	bottom_letters.append(key[letter_value])
#print bottom_letters
#for line in mynumbers:

#print mynumbers

all_letters = []
all_letters.append(top_letters)
all_letters.append(bottom_letters)

final_words = []
for i in range (len(top_letters)):
	if i%2==0:
		final_words.append(bottom_letters[i])
		final_words.append(top_letters[i])
	else:
		final_words.append(top_letters[i])
		final_words.append(bottom_letters[i])

f= open("56letters.txt","w")
for item in top_letters:
  f.write("%s," % item)
f.write("\n")
for item in bottom_letters:
	f.write("%s," % item)
f.write("\n")
f.write("--------------")
for item in final_words:
	f.write("%s," % item)
f.close()



print all_letters