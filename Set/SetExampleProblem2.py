John_Traits = {'Low Self Esteem', 'Loyal', 'Friendly', 'Loving', 21, 'Thrifty', "Clean", "Giving", "Thoughtful", "Positive"}
Friend1_Traits = {'High Self Esteem', 'Angry', 'Cunning', 'Awesome', 21, 'Thrifty', "Cool"}
Friend2_Traits = {'Low Self Esteem', 'Friendly', 'Loving', 21, 'Thrifty', "Clean"}

print("----")
print("Friend1 similarities to John",Friend1_Traits.intersection(John_Traits))
print("----")
print("Friend2 similarities to John",Friend2_Traits.intersection(John_Traits))