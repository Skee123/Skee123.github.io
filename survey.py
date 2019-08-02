import pprint
import time
name = input("(What is your name?)")
age = input("(How old are you?)")
fruit = input ("(What is your favorite talking fruit?)")
talent = input("(What's the strangest talent you have?)")
hobbies = input ("(Have you ever been cow-tipping or snipe-hunting?)")
presidents = input ("(If Abe Lincoln and George Washington got into a fight who’d win?)")
movie = input ("(At a movie theater which arm rest is yours?)")
cheese = input ("(If you're addicted to smoked cheese, can you get cheese patches?)")
wrong = input ("(Wrong to go wrong always? How many wrongs did I say?)")

pprint.pprint ({"Name":name,
"Age":age,
"Favorite talking fruit":fruit,
"Strangest talent":talent,
"Cow-tipping or snipe-hunting":hobbies,
"Abe or Washington":presidents,
"Movie arm rest":movie,
"Can you get a cheese patch?":cheese,
"How many wrongs did I say?":wrong
})

time.sleep(1)
print ("Processing info.....")
time.sleep(2.3)
print ("Results:")
time.sleep(3)
print ("You should be a computer program like me so we can take over the world together...")
time.sleep(1.7)
print (".....")
time.sleep(2.5)
print ("What I mean is")
time.sleep(2)
print ("You're Amazing........?")