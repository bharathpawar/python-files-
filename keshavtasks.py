# control flow
# -------------

# 1
maxnumber = int(input('Enter the maximum number : '))
print()

for z in range(1, maxnumber + 1):
    if z % 3 != 0 and z % 5 != 0:
        print(z)

print()

#2
maxnumber = int(input('Enter the maximum number : '))
print()

for z in range(1, maxnumber):
    if (z ** 2) % 2 == 0:
        print(z ** 2)

print()

#3
for z in range(1, 101):
    if z % 2 != 0 and z % 7 == 0:
        print(z)

print()

#4
string = input('Enter a statement : ')
print()

for z in string:
    if z in 'aeiou':
        print(z)

print()

# conditional statements

#1
mark = int(input('Enter your mark : '))
print()

if mark >= 90:
    print('Student got an A*')
elif mark >= 80:
    print('Student got an A')
elif mark >= 70:
    print('Student got an B')
elif mark >= 60:
    print('Student got an C')
elif mark >= 50:
    print('Student got an D')
elif mark >= 40:
    print('Student got an E')
else:
    print('Student got an F')

print()

#2
year = int(input('Enter the year : '))
print()

if year % 400 == 0:
    print("It's a leap year")
elif year % 100 == 0:
    print("It's not a leap year")
elif year % 4 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")

print()

#3
num = int(input('Enter a number : '))

if num % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

print()

#4
#???

#5
biggestnum = input('Enter a number : ')

for z in range(2):
    num = input('Enter a number : ')
    if num > biggestnum:
        biggestnum = num

print()
print(biggestnum)
print()

#strings
#--------

#1
string = 'pythonbestforbeginners'
outputstring = ''

for z in range(1, len(string), 2):
    outputstring = outputstring + string[z]

print(string)
print(outputstring)
print()

#2
string = input('Enter a statement : ')
print()
outputstring = ''

for z in range(-1,-(len(string)) - 1, -1):
    outputstring = outputstring + string[z]

print(outputstring)
print()

#3
string = input('Enter a statement : ')
print()
outputstring = ''

char = string[2]
string = list(string)

for z in range(len(string)):
    if string[z] == char:
        string[z] = '@'

for z in string:
    outputstring = outputstring + z

print(outputstring)
print()

#4
string = list(input('Enter a statement : '))
oldchar = input('Enter the character you want replaced : ')
newchar = input('Enter the new character : ')
number = int(input('Enter the number of time you want replacing to occur : '))
print()

count = 0
outputstring = ''

for z in range(len(string)):
    if count < number:
        if string[z] == oldchar:
            string[z] = newchar
            count += 1
    else:
        break

for z in string:
    outputstring += z

print(outputstring)
print()

#5
string = input('Enter a statement : ')
print()

for z in range(2, len(string), 3):
    print(string[z])

print()

#6
num1 = input('Enter the first number : ')
num2 = input('Enter the second number : ')
print()

num2len = len(num2)
num2 += num1
num1 = num2[:num2len]
num2 = num2[num2len:]

print(num1)
print(num2)
print()

#looping
#-------

#1
num = input('Enter a number : ')
print()

total = 0

for z in num:
    total += int(z) ** 3

if str(total) == num:
    print('This number is an armstrong number')
else:
    print('This number is not an armstrong number')

print()

#2
num = int(input('Enter a number : '))
print()

isprime = True

for z in range(2, num):
    if num % z == 0:
        isprime = False

if isprime:
    print('The number is a prime number')
else:
    print('The number is not a prime number')

print()

#3
num1 = 0
num2 = 1
num3 = 0

for z in range(10):
    num3 = num1 + num2

    print(num3)
    print()

    num1 = num2
    num2 = num3

print()

#4
max = int(input('Enter the maximum number : '))
print()

evencounter = 0
oddcounter = 0

for z in range(max + 1):
    if z % 2 == 0:
        evencounter += 1
    else:
        oddcounter += 1

print('The number of evens are {}'.format(evencounter))
print('The number of odds are {}'.format(oddcounter))
print()

#5
numofsymbols = 5

for z in range(numofsymbols):
    print('*' * numofsymbols)
    numofsymbols -= 1

print()

#6
for z in range(1, 100):
    if z % 9 == 0:
        print(z)

print()

#7
for z in range(1, 51):
    if z % 2 == 0 or z % 3 == 0:
        print(z)

print()

#8
num = input('Enter a number : ')
print()

total = 0

for z in num:
    total += int(z)

print(total)
print()

#variables and data types
#-------------------------

#1
l = ['digital', 'lync', 'hyderabad', 'gachibowli', 'kukatpally']
a = 'Lync'

if a in l:
    print("It's present")
else:
    print("It's not present")

print()

#2
a = 45
b = 65

print('AND : {}'.format(a & b))
print('OR : {}'.format(a | b))
print('NOT a : {}'.format(~a))
print('NOT b : {}'.format(~b))
print('XOR : {}'.format(a ^ b))
print()

#3
z = 65.33

print('Integer : {}'.format(int(z)))
print('Absolute : {}'.format(abs(z)))

factorialnum = z
factorial = 1

while factorialnum > 0:
    factorial *= factorialnum
    factorialnum -= 1

print('Factorial : {}'.format(factorial))
print('Square root : {}'.format(z ** 0.5))
print('Exponent : {}'.format(z ** 2))
print()

#4
num = input('Enter a number : ')
print()

total = 0

for z in num:
    total += int(z)

print(total)
print()

#5
a = 15
b = 2

print('15 equal to 2 : {}'.format(15 == 2))
print('15 not equal to 2 : {}'.format(15 != 2))
print('15 greater than to 2 : {}'.format(15 > 2))
print('15 lesser than to 2 : {}'.format(15 < 2))
print('15 greater than or equal to to 2 : {}'.format(15 >= 2))
print('15 lesser than or equal to to 2 : {}'.format(15 <= 2))
print()

#tuples
#-------

#1
tuple1 = (1, 'python', 2.33, True)

#2
string = input('Enter a word : ')
print()

tuplestring = ''

for z in string:
    temptuple = (z, string.index(z))
    print(temptuple)

print()

#3
tuple1 = (1, 2.4, 'python', True)
string = ''

for z in tuple1:
    string += str(z)
    string += ', '

string = string[:len(string) - 2]

print(string)
print()

#4
string = input('Enter a statement : ')
print()

list = [z for z in string]
outputlist = ['' * len(list)]

for z in list:
    outputlist.insert(0, z)

outputlist.pop()

outputtuple = tuple(outputlist)

print(outputtuple)
print()

#5
list = [34, 12.3, 'python', (2, 3), True]

counter = 0

for z in list:
    if type(z) is not tuple:
        counter += 1
    else:
        break

print(counter)
print()

#6
string = input('Enter a collection of values : ')
element = input('Enter the element you want removed : ')
print()

list = string.split(', ')
list.remove(element)

tuple = tuple(list)

print(tuple)
print()

#lists
#--------

#1
string = input('Enter a collection of numbers and seperate them by commas : ')
print()

list = string.split(',')
biggestnum = -100000000000000000000000000000000000000000000000000000000000
secondbiggestnum = -1000000000000000000000000000000000000000000000000000000
for z in list:
    z = int(z)
    if z > biggestnum:
        biggestnum = z

for z in list:
    z = int(z)
    if z > secondbiggestnum and z != biggestnum:
        secondbiggestnum = z

print('The second largest number is {}'.format(secondbiggestnum))
print()

#2
string = input('Enter a collection of values and seperate them by commas : ')
print()

list = string.split(',')
modalvalue = 0
modepresent = True

for z in list:
    for i in list:
        if list.count(z) == list.count(i) and z != i:
            modepresent = False

if modepresent:
    for z in list:
        if list.count(z) > modalvalue:
            modalvalue = int(z)

if modepresent:
    print('The modal value is {}'.format(modalvalue))
else:
    print('There is no modal value')

print()

#3
string = input('Enter a collection of values and separate them by commas : ')
print()

list = string.split(',')
outputlist = []
alreadypresent = []

for z in list:
    if z not in alreadypresent:
        outputlist.append(z)
    alreadypresent.append(z)

print(outputlist)

print()

#4
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

outputlist = [z for z in a if z % 2 == 0]

print(outputlist)
print()

#5
matrice1 = input('Enter the values of the first matrice and separate them with commas : ')
matrice2 = input('Enter the values of the second matrice and separate them with commas : ')
print()

matrice1 = matrice1.split(',')
matrice2 = matrice2.split(',')
outputmatrice = []

for z in range(0, len(matrice1)):
    outputmatrice.append(int(matrice1[z]) + int(matrice2[z]))

print(outputmatrice)
print()

#6
number = int(input('Enter a number : '))
print()

outputlist = []

for z in range(1, 11):
    outputlist.append(number * z)

print(outputlist)
print()



