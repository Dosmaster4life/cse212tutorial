coolSet = {"Cool Person 1", "Cool Person 2",5 , 100, "Million"}
numberSubset = {1, 2 ,523432 , 100,500}
numberSetSuper = {1, 2 ,523432 , 100,500,100000,12343204021034,432040032143214}


coolSet.add(100000) # add item to set
coolSet.remove("Cool Person 2") # remove item from set

print("-----------------") 
print("Just printing a set: ",coolSet) # output set
print("-----------------") 
print("Using .difference: ",numberSetSuper.difference(numberSubset)) # The items that are unique to numberSet2
print("-----------------") 
print("Printing a set that has been cleared: ",coolSet.clear()) # Empty the set, output is None
print("-----------------") 
print("Checking if numberSetSuper is a superset: ",numberSetSuper.issuperset(numberSubset))
print("-----------------") 
print("Checking if numberSetSuper is a subset: ",numberSetSuper.issubset(numberSubset))

#### More set features, try practing with ones below
'''
.add(value) # add an element
.remove(value) # remove an element
.clear() # clear set
.copy() # returns a copy of the set
.pop() # removes an element of the set
.union() # Used when doing union with another set
.difference() # unique items in the first set are returned
.discard() # removes an element from the set only if it exist, good for error handling
.intersection() # returns elements that are in both sets
.issubset() # returns whether another set is a subset of the superset
.issuperset() # returns whether the set is a superset of the subset
.symmetric_difference() # returns unique values in both sets, shared values are not returned
.isdisjoint() # returns true only if the two sets intersection is null
.difference_update() # removes elements in another set that match the elements in the set using .difference_update()
.intersection_update() # changes the set to elements that intersect in both sets
.symmetric_difference_update() # changes the set to contain only elements that are unique to both sets
'''