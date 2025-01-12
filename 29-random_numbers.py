import random
x=random.randint(1,8)
print(x)
y=random.random()
my_list=["Rock","Paper","Scissors"]
result=random.choice(my_list)
print(result)
cards=[1,2,3,4,5,6,7,8,9,"K","Q","J","A"]
random.shuffle(cards)
print(cards)