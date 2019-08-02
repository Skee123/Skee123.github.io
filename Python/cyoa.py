# choose your own adventure game 
#background story for adventure
print ("You are feeling hungry and decide to eat an apple.")
print ("Little do you know, this apple has magical properties and transports you to another dimension.")
print ("You find yourself in a dark, mysterious woods, and are surrounded by tall trees.")
print ("You are surprised and shocked.")
print ("You finally realize that it was the apple that transported you here")
print ("And the only way to return home is to find a similar magical apple")
print ("Suddnely two weapons appear, along with a magical voice that starts asking all these questions...")

 
weapon = input ("Do you want to take the sword or the shield? ")
#if the user chooses sword
if weapon == "sword": 
	print ("Suddenly a fire breathing dragon pops out of nowhere!!")
	print ("Once again that magical voice starts speakinng...")
	answer1 = input ("Do you want to fight the dragon with your sword? ")
	if answer1 == "yes" or answer1 == "Yes":
		print ("Right choice!")
		print ("You were able to defeat the dragon and realized it was guarding a magic apple tree!")
		print ("This magic apple tree allowed you to go home! Good job!")
	if answer1 == "no" or answer1 == "No":
		print ("Wrong choice!")
		print ("The dragon saw your sword and deemed you a threat!")
		print ("It ended your life before you could even move...")
#if the user chooses shield
if weapon == "shield":
	print ("Suddenly a fire breathing dragon pops out of nowhere!!")
	print ("Once again that magical voice starts speakinng...")
	answer1 = input ("Do you want to fight the dragon with your shield? ")
	if answer1 == "yes" or answer1 == "Yes":
		print ("Wrong choice!")
		print ("The dragon was able to burn through your wooden shield and kill you")
	if answer1 == "no" or answer1 == "No":
		print ("Right choice!")
		print ("You were able to escape before the dragon saw you, and were able to find the magic apple tree another way!")
		print ("Great job getting back home!")
		
	
