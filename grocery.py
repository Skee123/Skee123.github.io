#build a basic grocery list

groceries = []
print (groceries)

groceries = ["milk", "eggs", "bread", "bacon", "airheads"]
print (groceries)

#play around with the list
groceries.append("spinach")
print (groceries)
groceries.remove ("bacon")
print (groceries)

print (groceries [0])
print (groceries [2])

groceries.del(0)
print (groceries)

if "butter" not in groceries:
	#add butter to the end of list
	groceries.append("butter")
	
print (groceries)


groceries.insert(2, "poptarts")
print (groceries)