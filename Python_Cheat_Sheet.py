Package/Library:
    * Module 1
    * Module 2
        * Class 1
        * Class 2
        * Function 1
        * Function 2

Object = Instance
Attributes = Properties

Function vs Method
    function_name()
    object.method_name()


a = 'Hello' #str
a = 1       #int
a = 1.232   #float
a = True        #Boolean

x//y #Целая часть
x%y  #Остаток
x**y #X in the power of Y

a = input('What is your name?')
print(a)


## List, Dictionary, Tuples

    a = 1,2,3               #tuples
    a = [1,2,3]             #list
    a = {1:'a',2:'b',3:'c'} #dictionary

    #Additions:
        #tuplet
            t = t + (x)

        #list
            append(x)
            extend(x)
            insert(i,x)

        #dictionary
            d[x] = 1


    #Deletion:
        #tuple
            #immutable
        #list
            l.remove(x)
            del l(x)
        #dictionary
            ###



    #Update:
        #tuple
            #immutable
        #list
            l[i] = x
        #dictionary
            d[k] = 1




print (x, end = '\n') #seperate by "seperate line"


    
## Text / String manipulation
    #Conversion
    " Hello ".strip()
    " Hello ".ltrip()
    " Hello ".rtrip()

    "Hello".upper()
    "Hello".lower()  

    " Hello ".count("e")

    "Hello ".replace(" "," Sarkhan") #only for string

    "Sarkhan Azer Nijat".split() #splits STRING to LIST []
    "Sarkhan;Azer;Nijat".split(";") #splits str to the list []
    ";".join(["Sarkhan","Azer","Nijat"])  #Joins LIST to STRING


    #Boolean
    "Hello".endswith("lo")   #true/false
    "Hello".isnumeric() #true/false
    "Hello".isalpha() #true/false


    'Aren\#\'t you hungry'
    # '\' ignores next character


break       #breakes the loop
continue    #skips only 1 loop

#manipulation with Tuple
    Immutable / no manipulation;
    t = t +(x,) #adds values to the tuples
    #cannot be modified, or deleted
    t.count('x')

#manipulation with DICTIONARY
    print(d[k])

    for key,value in A_Dict.items():
        print("{} has {} unique letters".format(key,value))

    dict.get(key, default)          # Returns the element corresponding to key, or default if it's not present
    dict.keys()                     # Returns a sequence containing the keys in the dictionary
    dict.values()                   # Returns a sequence containing the values in the dictionary
    dict.items()
    dict.update(other_dictionary)   # Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
    dict.clear()                    # Removes all the items of the dictionary



#LIST manipulation
l[i] = x #update

fruits = ['alma','armud']
fruits.append('qarpiz')             # only single item
fruits.extend(['Dilbar','Gular'])   # several items
fruits.insert(0,'gilas')

fruits.index('alma')                #if not then error

fruits.remove('alma')               #removes first matching value
fruits.pop('i')                     #removes first matching value
del fruits['i']                      #only index
fruits.sort()                       #modifies current list
sorted(fruits,key = len)                      #new list with changes, do not modify current list
";".join(["Sarkhan","Azer","Nijat"])  #Joins LIST to STRING
list(x)                             #transfer to list
fruits.count('x')                   #counts









min(x) # x could be list, tuple, dictionary
max(x) # x could be list, tuple, dictionary
abs(x) # x could be list, tuple, dictionary
len(x) # x could be list, tuple, dictionary
a in x # x could be list, tuple, dictionary

round(x,2)  # 
pow(x,y)    # x**y







#Advance string manipulation
def replace_ending(sentence, old, new):
	if sentence.split()[-1] == old:
		i = sentence.split()
		new_sentence = " ".join(i[0:-1]) + " " + new
		return new_sentence
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"





#function
def mult(x,y):
	a = x*y
	print(a)


def eq(a,b,c):
    print("",a)
    print("",a)
    print("",a)
    return a-b*c
eq(10,3,2)
eq(b=3,c=2,a=10)




#loops
#1) FOR LOOPS
for x in list:
	print(x, end = ' ')



for x in range (0,100):
    if x %3 == 0:
        print(x)

#or
z = [x for x in range (0,100) if x %3==0]
print (z)



#2) WHILE LOOPS
x = 0 #Initializing
while x <20:
	print (x, end = ' ')
	x+=1



#3) RECURSION
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n
    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15



# Advance FOR loop
#1
def group_list(group, users):
  members = group + ': '
  for x in users:
    members += x + ' '
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"



#2
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  listing = []
  for word in words:
    # Create the pig latin word and add it to the list
    pig_word = word[1:] + word[0] + 'ay'
    # Turn the list back into a phrase
    listing.append(pig_word)
  return ' '.join(listing)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



#3
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                letter -= value
            else:
                result += "-" + result
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------



#4
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for x in filenames:
    if x[-4:] == '.hpp':
        x = x.replace('.hpp','.h')
    newfilenames.append(x)      

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]



#5 - Palindrom
def is_palindrome(input_string):
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for x in input_string.replace(' ','').lower():
		new_string = new_string + x
		reverse_string = x + reverse_string
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True



#6 - multiplication table
def mult_table(start,end):
    list2 = []
    for x in range(start,end+1):
        list = []
        for y in range(start,end+1):
            list.append(x*y)
        list2.append(list)
    for x in list2:
        print (x, end = '\n')
    
mult_table(1,20)



# Advance WHILE loop
#1
x=0
while x<20:
    if x%2 ==0:
        print (x)
    x+=1



#2
def is_power_of_two(n):
  while n % 2 == 0 and n!= 0:   # Check if the number can be divided by two without a remainder
    n = n / 2                   # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False



#3
def sum_divisors(n):
  sum = 0
  x = n-1
  # Return the sum of all divisors of n, not including n
  while x> 0:
    if n%x == 0:
      sum = sum + x
    x = x-1
  return sum

print(sum_divisors(0)) # 0
print(sum_divisors(3)) # Should sum of 1 # 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18 # 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51 # 114



#4
def multiplication_table(number):
	multiplier = 1 # Initialize the starting point of the multiplication table
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) # Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
multiplication_table(5) # Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
multiplication_table(8)	# Should print: 8x1=8 8x2=16 8x3=24



#5
def numb_len(x):
    count = 1
    while x>=10:
        count+=1
        x= x/10
    print("length is :"+str(count))



#Advance recursion
#1
def is_power_of(number, base):
  if number < base: # Base case: when number is smaller than base.
    if number == 1: # If number is equal to 1, it's a power (base**0).
      return True
    else:
      return False
  return is_power_of(number/base, base) # Recursive case: keep dividing number by base.

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False



#2 - recursion loops factorial 1*2*3*4*5*6...*x
def factorial(x):
    if x<2:
        return 1
    else:
        return x*factorial(x-1)

factorial(5)




#loop with format function
#1
winners = ['Sarkhan','Javid','Elnur']
for index,y in enumerate(winners):
    print('{} - {}'.format(index+1,y))

#2
def guest_list(guests):
	for Name,Age,Profession in guests:
		x = []
		print('{} is {} years old and works as {}'.format(Name,Age,Profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""



#3
a = 'Sarkhan'
b = len(a)*3
print( '{a} wants to travel to {b:>15.2f} number of cities. For example to {c}'.format(a=a,b=b,c='Antalya'))
print( '{} wants to travel to {} number of cities. For example to {}'.format(a,b,'Antalya'))

"""
Sarkhan wants to travel to           21.00 number of cities. For example to Antalya
"""


#4
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {km:.1f} km".format(miles,km=km)
	return result

print(convert_distance(12))     # Should be:    12      miles equals    19.2 km
print(convert_distance(5.5))    # Should be:     5.5    miles equals     8.8 km
print(convert_distance(11))     # Should be:    11      miles equals    17.6 km



#5
def email(names):
    result=[]
    for name,surname in names:
        result.append('{}.{}@gmail.com'.format(name,surname))
    return result

email([('Sarkhan','Shirinov')])




	
#6 Function compares two numbers and returns them in ascending order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

smaller , bigger = order_numbers(100, 99)
print(smaller, bigger)



#enumerate indexing
winners = ['Sarkhan','Javid','Elnur']
for index,y in enumerate(winners):
    print('{} - {}'.format(index+1,y))




# Try Except Exit Finally:

try:
  # Simulate reading a file
  with open("data.txt", "r") as f:
    data = f.read()
    if not data:
      raise ValueError("Empty file")
except FileNotFoundError:
  print("File not found.")
  exit(1)  # Signal "file not found" error
except ValueError:
  print("Invalid file content.")
  exit(2)  # Signal "invalid data" error
finally:
  # Assuming there's a file object, ensure it's closed
  if f:
    f.close()



while True:
    x = input('Done?')
    if x == 'Done':
        break # breaks while loop
    print(x)


# а если continue:
while True:
    x = input('Done?')
    if x == 'Done':
        continue # goes back to while loop
    print(x)














------------------------------------------------------------------------------
df.mean()  #mean for each column
df.sum()   #sum for each column
df.mean(axis=1) # mean for each row

df.round(2) #rounds values of table

df['col1'].value_counts()
'../folder/file.csv' #location of the file

read_csv('filename.csv', 

#if 0 then no index column, default None
index_col = 0 

#reads the column format as date
parse_dates = ['date_column1','date_column2']


)




filename.shape #returns tuple of number of rows and columns
filename.size #returns number of data (rows*columns)
len(filename) #number of rows
filename.dtypes #returns list of columns and its format, format is pandas.series
filename.info() #prints overal info of the table, columns, its format, notnull count
filename.info(memory_usage = 'deep') #prints


filename.index #returns Index; pandas.Index
filename.columns #returns Index; pandas.Index
filename.values #returns Array; numpy.ndarray

filename.setindex('columnname1') #returns dataset

pd.get_option('display.max_columns') #there is more commands, see documentation
pd.set_option('display.max_columns', 22) #it works only for thsi session 

file.index #returns kind of the index


filter = filt1 & filt2      #and, intersect
filter = filt1 | filt2      #or, union
filter = ~(filt1 & filt2)   #not, C

f_list = ['apple','xiaomi']
filt = file['column_name'].isin(f_list)
file[filt]

col = file['column_name_1']
file['column_name_1'].between(0,10) # 0 and 10 inclusive

file['column_name_1'].isna
file['column_name_1'].isnull

min_count = 1000
file.query("not (col1>1000 and col2<50) and col3>@min_count and events in ['snow','rain']")

file.at[a,b]  #return only 1 cell of data, more optimized than loc
file.iat[a,b] #return only 1 cell of data, more optimized than iloc





#working with files:

    #files work as OPEN-USE-CLOSE principle
    file = open('data.txt')
    print(file.readline()) # reads first line
    print(file.readline()) # if you run 2nd time then it reads 2nd line
    print(file.read()) 	   # read the file till the end after where you left
    file.close()

    print(file.readlines()) #reads all lines (format: list)

    # you need to close the file as:
    # 1. you could not modify it while it is open in python
    # 2. using 1st logic other processes could not use it
    # In order to solve it, use with:



    checked_out=["Andrea", "Manuel", "Khalid"]
    temp_list=[] #guests.txt

    with open("guests.txt", 'r') as guests:
        for g in guests:
            temp_list.append(g.strip())

    with open("guests.txt", 'w') as guests:
        for name in temp_list:
            if name not in checked_out:
                guests.write(name + "\n") # writes lines to file



    with open('data.txt') as file:

    open('data.txt', 'r') 
    # r - read only, error if not exists
    # w - immediately overwrite the file or create new if not exists
    # a - append, add new lines to existing file
    # r+ - read and write  





#Regexp
    a. c  - any character
    ^abc -  if  words starts with abc
    abc$ - if word ends with abc
    a?bc - a is optional
    X* - means several repetitions of X characters, even if zero repetition (x is an example)
    X+ -  matches one or more occurrences of X

    [Pp] - upper and lower case 'P'
    [a-z] - only lowercase
    [^a] - except a
    \w* - exists any alpha numerical character
    \d* - digits
    \s* - space,tab.newline
    \b* - word boundaries


    #Patterns
    '^(\w*), (\w*)$'      #'Sarkhan, Shirinov'

    #if we want to add several symbols in groups then:
    '^([\w -\.]*), ([\w -\.]*)$'      #'Sarkhan, Shirinov F.'






result = re.search(pattern,text) #find first pattern in text
re.findall(pattern,text) #find all pattern in text in form of List

result[0] # provide results of the groups (in pattern) in form of Tuples
result[1] # provide FIRST result of the groups (in pattern)
result[2] # provide SECOND result of the groups (in pattern)


