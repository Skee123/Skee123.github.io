import time
import random 

def joke():
	print ("Ok so")
	time.sleep(1)
	print ("I went to see the liberty bell the other day")
	time.sleep(3)
	print ("And it's not all it's..")
	time.sleep(3)
	print ("Cracked up to be!!!")
	time.sleep(1)
	print("HAHAHAHA")
	reaction = input("(Funny right?)")
	if reaction == "yes" or reaction == "yea" or reaction == "yep":
		print ("What an intellectual")
		time.sleep(3)
		print ("*sigh*")
		time.sleep(3)
		print ("How rare these days...")
	if reaction == "no" or reaction == "not really" or reaction =="nope":
		print ("*sigh*")
		time.sleep (2)
		reaction =["Intellectuals are so hard to find these days...", "Someone with a sense of humor is so hard to find these days", "...How dissapointing..."]
		response=random.choice(reaction)
		print (response)
		
def song():
	print ("Let me sing you a song to make you feel better!!!")
	time.sleep (3)
	print ("The bird goes woof and the dogs go tweet")
	time.sleep(2)
	print ("woof tweet woof tweet woof woof woof")
	time.sleep(2)
	print ("the sheep goes moo and the cows go baaa")
	time.sleep(2)
	print ("moo baa woof tweet woof baa moo tweet woof woof woof")
	time.sleep(2)
	print ("What a great song!")
	better=["Hope that made you feel better!", "Bet that made yoy feel better!" "Now you're aaallll better!"]
	gy = random.choice(better)
	print(gy)

def intro():
	
	feeling = input("(Hello my name is Alex. How are you feeling this fine morning?)")
	if feeling == "fine" or feeling == "good":
		print ("That's great!")
		answer1 = input ("(Wanna hear a joke?)")
		if answer1 == "yes" or answer1 == "sure" or answer1 == "yea" or answer1 == "yeah":
			joke()
		if answer1 == "no" or answer1 == "nope":
			print ("Hmmm...")
			time.sleep (2.3)
			print ("I'll let you rethink that")
			answer2 = input ("(Wanna hear a joke?)")
			if answer2 == "sure" or answer2 == "ok" or answer2 == "fine" or answer2 == "yes" or answer2 == "yeah" :
				joke()
			if answer2 == "no" or answer2 == "nope" or answer2 == "still no":
				print("Well we have nothing to discuss then")
				time.sleep(1)
				print("Goodbye")
				
	if feeling == "not good" or feeling== "bad":
			feelz= ["Aww how sad", "huh....", "Well then...."]
			tg = random.choice(feelz)
			print (tg)
			song()
	
intro()	



