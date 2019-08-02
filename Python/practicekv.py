#create an empty dictionary
contacts = {} #for a lost, you would use []

##create a non-empty dictionary
fruits = {"apple":"red", "pear":"green"}

##add a key value pair to the dictionary
fruits["banana"] = "yellow"

##change the value for "apple"
fruits["apple"] = "green"

##add an integer as a value
fruits["watermelon"] = 5

##add multiple values for the same key
fruits["strawberries"] = ["red","pink", "green"]#red,pink, and green is now a list

##index into the dictionary and return a value for a particular key
fruits["banana"]

##replace an entry in the dictionary
fruits["banana"] = "green"

print (fruits)

