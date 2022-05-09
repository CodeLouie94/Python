num1 = 42 #variable declaration -numbers
num2 = 2.3 #variable declaration -numbers
boolean = True #variable declaration -Boolean
string = 'Hello World' #variable declaration -Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declratation, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuples
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #function parameter
print(person['name']) #log statement
person['name'] = 'George' #variable declaration, dictionary
person['eye_color'] = 'blue' #variable declaration, dictionary
print(fruit[2]) #log statement

if num1 > 45: #if statement
    print("It's greater") #log statement
else: #else
    print("It's lower") #log statement

if len(string) < 5: #if statement
    print("It's a short word!") #log statement
elif len(string) > 15: #else if
    print("It's a long word!") #log statement
else: #else
    print("Just right!") #log statement

for x in range(5): #for loop, start
    print(x) #log statement
for x in range(2,5): #for loop start
    print(x) #log statement
for x in range(2,10,3): #for loop start
    print(x) #log statement
x = 0#variable declaration
while(x < 5): #while loop start
    print(x) #log statement
    x += 1 #increment

pizza_toppings.pop() #function
pizza_toppings.pop(1) #function 

print(person) #log statement
person.pop('eye_color') #function
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if statement
        continue #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': # if statement
        break #break

def print_hello_ten_times(): #function 
    for num in range(10): #for loop
        print('Hello') #log statement

print_hello_ten_times() #function

def print_hello_x_times(x): #function parameter
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_times(4) #function #argument

def print_hello_x_or_ten_times(x = 10): # function, parameter
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_or_ten_times() #function
print_hello_x_or_ten_times(4) #function argument


"""
Bonus section
"""

# print(num3) #- NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean) unexpected indent
# fruit.append('raspberry')
# fruit.pop(1)