John_Traits = {'Low Self Esteem', 'Loyal', 'Friendly', 'Loving', 21, 'Thrifty', "Clean", "Giving", "Thoughtful", "Positive"}
Friend1_Traits = {'High Self Esteem', 'Angry', 'Cunning', 'Awesome', 21, 'Thrifty', "Cool"}
Friend2_Traits = {'Low Self Esteem', 'Friendly', 'Loving', 21, 'Thrifty', "Clean"}

print("John, you are ",John_Traits.difference(Friend1_Traits).difference(Friend2_Traits))