#For Loop
favorite_pizzas = ['cheese','suasage','bacon']
for pizza in favorite_pizzas:
    print('I like ' + pizza.title() + ' pizza.')
print('\nI really enjoy Pizza!')


#Using the range() function and adding to an empty list. 
one_thousand = []
for number in range(1,1001):
    one_thousand.append(number)
print(one_thousand)

print(min(one_thousand)) # tells you the smallest number in the list
print(max(one_thousand)) # tell you the largest number in the list 

#Printing out odd numbers from 1 to 20.

odd_numbers = []
for odd in range(1,20,2):
    odd_numbers.append(odd)

print(odd_numbers)

#Make a list of multiples of 3 from 3 to 30. 

multiples_of_3 = []
for number in range(3,30,3):
    multiples_of_3.append(number)

print(multiples_of_3)

#Make a list of first ten cubes 
first_10cubes = []
for number in range(1,11):
    first_10cubes.append(number**3)

print(first_10cubes)

#or make a list of first ten cubes using Comprehension List

first_ten_cubes = [number**3 for number in range(1,11)]
print(first_ten_cubes)

#print using slicing 
lotr = ['frodo','sam','pippin','merry','aragon','gandalf','gimli','legolas','boromir']
print("The first three items in the list are: ")
print(lotr[:3])
print(lotr[4:7])
print(lotr[6:])

lotr.append('gollum')

new_lotr = lotr[:]

new_lotr.append('faramir')
print(lotr)
print(new_lotr)

#Tuple = unchangeable list. ( same as list but you use () in stead of [] )

favorite_dish = ('momo','chicken','rice','yogurt','eggs')
#favorite_dish[1] = 'milk' # it will print error because you cannot change tuples but you can rewrite the whole varaible again to change a tuple 
favorite_dish =  ('momo','milk','rice','yogurt','eggs')
for dish in favorite_dish:
    print(dish)



