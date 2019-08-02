#This is an example when the input is a string 
name = input("What is your name? ")
show = input ("What is your favorite show on Netflix? ")
print ("My name is", name, "and I like to watch", show, "on Netflix")

#This is an example when the input is an interger
age = int(input("How old are you?"))
favNum = int(input("What is your favorite number?"))
print ("I am", age, "years old, " "and my favorite number is ", favNum) 

#This is an example when the input is a float:
weight = float(input("What is the weight of the suitcase?"))
if weight >50.0:
	print ("Over weight")
if weight < 50.0:
	print ("Add some more weight sis you're going on vacay")