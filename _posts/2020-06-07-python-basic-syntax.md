---
title: 'Python: Basic Syntax'
date: 2020-06-07T14:00:43-05:00
author: gerryw13189
layout: single
classes: wide
permalink: 2020/06/python-basic-syntax
categories:
  - Linux
tags:
  - Scripting-Python
---
<!--more-->

### Top

- [Top](#top)
- [Version](#version)
- [Naming](#naming)
- [Modules](#modules)
- [Variables and Comments and Inspections](#variables-and-comments-and-inspections)
- [Functions](#functions)
- [Strings](#strings)
- [Conditionals](#conditionals)
- [Loops](#loops)
- [Collections and Arrays](#collections-and-arrays)
- [Dictionaries](#dictionaries)
- [Date and Time](#date-and-time)
- [Misc](#misc)

### Version

I usually assume v3.5 so I will put this after import statements:

```python
import sys
# require Python interpreter > v.3.5
assert sys.version_info >= (3, 5)
```

- [Back to top](#top)

### Naming

If you get the error `module $module has no $method attribute`, for example: `module csv has no reader attribute` when [it clearly does](https://docs.python.org/3/library/csv.html) then this is because I named my file `csv.py`. Once renamed to `monitorcsv.py`, everything worked. Had the same thing happen with `email.py`.

- [Back to top](#top)

### Modules

- See [docs](https://docs.python.org/3/reference/import.html)

   ```python
   # Placed at top of file under the shebang
   import os
   from random import shuffle # from module import submodule
   ```

- [Back to top](#top)

### Variables and Comments and Inspections

   ```python
   ################
   # Variables
   # Declare a variable and initialize it, data types are not strong
   >>> f = 0
   >>> g = "0"
   >>> type(f)
   <class 'int'>
   >>> type(g)
   <class 'str'>
   >>> 

   # ERROR: variables of different types cannot be combined
   >>> print("this is a string " + 123 )
   Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   TypeError: Can't convert 'int' object to str implicitly

   # Proper way to do  this 
   >>> print("This is a string " + str(123) )
   This is a string 123
   >>> 

   # one to many var
   >>> a = b = c = 3
   >>> print(a)
   3
   >>> print(b)
   3
   >>> print(c)
   3
   >>> 
   
   # many to many
   >>> a, b, c = 1, 4, 'gerry'
   >>> print(a)
   1
   >>> print(b)
   4
   >>> print(c)
   gerry
   >>> 

   # read input
   >>> name = input("Enter your name: ")
   Enter your name: bob
   >>> print("your name is",name)
   your name is bob
   >>> 
   ################
   # Similar to get-member in pwsh
   dir(f) # see methods and properties
   type(f) # gives you the data type so you can google it to find methods and parameters

   # another way
   >>> import inspect
   >>> a = inspect.getmembers(name, predicate=inspect.isbuiltin)
   >>> type(a)
   <class 'list'>
   >>> for item in a:
   ...     print(item)
   ... 
   ('__dir__', <built-in method __dir__ of str object at 0x7faf534653018>)
   ('__format__', <built-in method __format__ of str object at 0x7faf534653018>)
   # more stuff
   >>>

   ################
   # Comment block (single line)

   '''
   multi line
   commment block
   '''

   ################
   # Data type casting
   # float to int
   >>> int(3.14159)
   3
   # string to collection
   >>> list('gerry')
   ['g', 'e', 'r', 'r', 'y']
   # int to string
   >>> chr(97)
   'a'
   # int to boolean
   >>> bool(1)
   True
   >>> bool(0)
   False
   # boolean to int
   >>> int(True)
   1
   >>> int(False)
   0
   # string to int
   >>> int('100')
   100
   # int to hex
   >>> hex(397312)
   '0x61000'
   >>>
   ```

- [Back to top](#top)

### Functions

   ```python
   ################
   # Default function stuff
   
   >>> def print_args(arg1,arg2):
   ...     print(arg1,arg2)
   ... 
   >>> print_args("Hello my name is","Gerry.")
   Hello my name is Gerry.
   >>> 

   # function that returns a value
   >>> def cube(x):
   ...     return x*x*x
   ... 
   >>> cube(9)
   729
   >>>

   # function with default value for an argument
   >>> def power(num, x=1):
   ...     result = 1
   ...     for i in range(x):
   ...             result = result * num
   ...     return result
   ... 
   # here x=1(default value) and 2^1 is printed
   >>> power(2)
   2
   # here x=3 and 2^3 is printed
   >>> power(2,3)
   18
   # python can determine arguments by name
   >>> power(x=3,num=2)
   18
   >>> 

   # function with variable number of arguments
   >>> def multi_add(*args): 
   ...     result = 0
   ...     for x in args:
   ...             result = result + x
   ...     return result
   ... 
   >>> multi_add(2,4,6,7,3)
   22
   >>> 


   ################
   # Script Arguments
   # sys.argv is list of arguments passed to the script
   # sys.argv[0] is by default the path of script
   # and user defined arguments start with index 1

   # example, type `vi max.py` and paste in
   #!/usr/bin/python
   
   import sys
   
   # Print total number of arguments
   print ('Total number of arguments:', format(len(sys.argv)))
   
   # Print all arguments
   print ('Argument List:', str(sys.argv))
   
   # Print arguments one by one
   print ('First argument:',  str(sys.argv[0]))
   print ('Second argument:',  str(sys.argv[1]))
   print ('Third argument:',  str(sys.argv[2]))
   # save and exit
   # now type `chmod +x ./max.py` and `python3 ./max.py 13 23 57`
   $ python3 ./max.py 13 418 72
   Total number of arguments: 4
   Argument List: ['./max.py', '13', '418', '72']
   First argument: ./max.py
   Second argument: 13
   Third argument: 418
   $ 
   
   ```

- [Back to top](#top)

### Strings

   ```python
   # mostly copied from https://ridicurious.com/20118/03/30/powershell-scripting-guide-to-python-part1/, posting here in case he removes his post for some reason

   # send text to var
   >>> hello = "this is text"
   >>> print(hello)
   this is text
   >>> 

   # check var value
   varGerry = 'gerry'
   >>> if varGerry == 'gerry':
   ...     print("hello gerry")
   ... 
   hello gerry
   >>> 

   # split method
   >>> name = 'Gerry LastName'
   >>> first, last = name.split(' ')
   >>> print(first)
   Gerry
   >>> print(last)
   LastName

   # variable expansion in strings
   >>> name = 'Gerry'
   >>> adjective = 'funny'
   >>> noun = 'person'
   >>> verb = 'runs'
   >>> print(name,'is a',adjective,noun,'that',verb)
   Gerry is a funny person that runs
   >>> 

   # Preferred:
   >>>print('{} is a {} {} that {}'.format(name, adjective,noun,verb))
   Gerry is a funny person that runs
   >>> 

   # use numbers in braces to define sequence of arguments consumed by the string
   >>> 'a:{0} b:{2} c:{1}'.format('red','green','blue')
   'a:red b:blue c:green'
   >>> 

   # adding zeros
   >>> '{0:03d}'.format(5)
   '005'
   >>>

   # using dictionaries  for formatting
   >>> coor = {'latitude': '31.24E', 'longitude': '-125.181N'}
   >>> 'Coordinates: {latitude}, {longitude}'.format(**coor)
   'Coordinates: 31.24E, -125.181N'
   >>> 

   #################
   # escape characters in string
   # represented by a backslash '\'
   # interpreted in a single and double quoted strings.
   >>> print("\\")
   \
   >>> print('\'')
   '
   >>> print("\"")
   "
   >>> print("Hello\nWorld!")
   Hello
   World!
   >>> print("Hello\tWorld!")
   Hello   World!

   # you can escape double within single but it's not required
   >>> bob = '\"bob\"'
   >>> print(bob)
   "bob"
   # same as
   >>> bob = '"bob"'
   >>> print(bob)
   "bob"
   >>> 

   ###############
   # common string operators
   >>> string = 'Gerry'
   # concatenation
   >>> string +' LastName'
   'Gerry LastName'
   # repetition
   >>> string*5
   'GerryGerryGerryGerryGerry'
   # access character at index
   >>> string[1]
   'e'
   >>> 

   # built-in string methods
   len('python') # length of string
   'python'.index('o') # find characters at an index

   # changing the case
   print('hello world'.capitalize())  # capitalize 1st char of the string
   print('hello world'.title())  # all words to title case

   # splitting a string .split()
   print(string.split(' '))  # splitting the string by white space
   print(string.split('my'))  # splitting the string by a word, eq. 'my'
   print(string.split('\n'))  # splitting by newline character

   # joining string .join()
   print(' '.join('Gerry'))  # Joining each char with a space
   print('*'.join('Gerry'))  # Joining each char with a '*'

   # reversing a string reversed()
   print(''.join(reversed('python')))  # reversing a string
   print(''.join(list('python')[::-1]))  # reversing a string / print(‘Python'[::-1]) is much more elegant and easy to remember

   # strip/trim a string .strip() , .lstrip() , .rstrip()
   print('   Hey there      '.strip())  # stripping white spaces from both ends of the string
   print('   Hey there      '.lstrip())  # stripping white spaces from left end of the string
   print('   Hey there      '.rstrip())  # stripping white spaces from right end of the string

   # string padding .rjust() .ljust(), .center()
   print('Hello'.rjust(30))
   print('Hello'.ljust(30, '-'))
   print('Hello'.rjust(30, '*'))
   print('Hello'.center(30, '_'))
   ```

- [Back to top](#top)

### Conditionals

   ```python
   ## Conditionals ## 
   print("\n\nConditional:")
   x, y = 100, 100

   # conditional flow uses if, elif, else  
   if(x < y):
      st = "x is less than y"
   elif(x == y):
      st = "x is the same as y"
   else:
      st ="x is greater than y"
   print(st)

   # python doesn't have switch cases, I pretty much just use if, elif, else instead
   ```

- [Back to top](#top)

### Loops

   ```python
     ## Loops ##
   print("\n\nLoops")
   # python only has for and while loop

   # define a while loop
   x = 0
   while(x <5):
      print(x)
      x+=1  # there is no x++ operater in python

   # define a for loop
   for x in range(5,10):
      print(x)

   # use the break and continue statements
   for x in range(5,30):
      #if (x == 7): break  # when x ==7 loop will end and next block of code will execute 
      if (x %2 == 0) : continue # when x == even number, loop will go back to start and run again ignoring the even numbers and only printing odd numbers
      print(x)

   #using the enumerate() function to get index 
   days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

   for i,d in enumerate(days):
      print(i,d)

   # for loop
   primes = [2, 3, 5, 7]
   for prime in primes:
      print(prime)

   # while
   # Prints out 0,1,2,3,4

   count = 0
   while count < 5:
      print(count)
      count += 1  # This is the same as count = count + 1

   # break and continue
   # Prints out 0,1,2,3,4

   count = 0
   while True:
      print(count)
      count += 1
      if count >= 5:
         break

   # Prints out only odd numbers - 1,3,5,7,9
   for x in range(10):
      # Check if x is even
      if x % 2 == 0:
         continue
      print(x)

   # else clause
   # Prints out 0,1,2,3,4 and then it prints "count value reached 5"

   count=0
   while(count<5):
      print(count)
      count +=1
   else:
      print("count value reached %d" %(count))

   # Prints out 1,2,3,4
   for i in range(1, 10):
      if(i%5==0):
         break
      print(i)
   else:
      print("this is not printed because for loop is terminated because of break but not due to fail in condition")

   ## another for loop
   #!/usr/bin/python
   # A list of shuttles 
   shuttles = ['columbia', 'endeavour', 'challenger', 'discovery', 'atlantis', 'enterprise', 'pathfinder' ]
   
   ## Read shuttles list and enumerate into index and value 
   for index, value in enumerate(shuttles):
         print index, value

   '''
   prints:
   0 columbia
   1 endeavour
   2 challenger
   3 discovery
   4 atlantis
   5 enterprise
   6 pathfinde
   '''


   ## Iterate through dictionary
   dnsservers = {}
   dnsservers = {"us":"ns1.cyberciti.com", "uk":"ns2.cyberciti.biz", "asia":"ns3.cyberciti.org"  }

   # Python for loop for key,value using dict data type
   for location, server in dnsservers.items():
      print( server, "dns server is located in" , location)

   '''
   returns:
   ns1.cyberciti.com dns server is located in us
   ns2.cyberciti.biz dns server is located in uk
   ns3.cyberciti.org dns server is located in asia
   '''
   ```

- [Back to top](#top)

### Collections and Arrays

   ```python
   print("\n\nArrays")
   days = ["Mon","Tue","Wed","Thu","Fri","Sat"]
   print(days)  # this will print arrays in array format

   #printing all elements of an array
   for d in days: 
      print(d)

   ################################################################################
   # import the module, since Array is not a native data structure
   #2020-03-21-23-20-59.png

   import array
   a = array.array("I",[1,2,3,4,5]) # homogeneous, strong typed array
   type(a) # get data type of the array
   # not implicitly typecasted, you've to explicitly typecast elements with the array data type
   a = array.array("I",[1,2,3,int(4.3),5]) 
   # throws error 'TypeError: integer argument expected, got float'
   a = array.array("I",[1,2,3,4.3,5]) 

   # operations on array
   a.insert(1,7) # inserting elements
   a.pop(3) # delete and return an element
   a.reverse() # reverse the array

   # access elements
   a[0] # list first element
   a[-1] # list last element

   import array as arr

   numbers_list = [2, 5, 62, 5, 42, 52, 418, 5]
   numbers_array = arr.array('i', numbers_list)

   print(numbers_array[2:5]) # 3rd to 5th
   print(numbers_array[:-5]) # beginning to 4th
   print(numbers_array[5:])  # 6th to end
   print(numbers_array[:])   # beginning to end

   # see https://www.programiz.com/python-programming/array
   # Unless you don't really need arrays (array module may be needed to interface with C code), their use is not highly recommended.

   ##############

   # lists
   # creating empty lists
   fruits = []
   fruits = list()

   # adding elements to list
   fruits.append('apple')
   fruits.append('banana')
   fruits.append('orange')


   '''
   >>> cars.append("ford")  
   >>> print(cars)
   ['ford']
   >>> cars.append("chevy") 
   >>> print(cars)
   ['ford', 'chevy']
   >>> print(cars[0]) 
   ford
   >>> print(cars[1]) 
   chevy
   >>>print(len(cars))
   2
   '''

   # change value
   ## >>> cars[-1] = 'kia'
   ## >>> print(cars)
   ##['ford', 'kia']
   ##>>>

   # insert at element number:
   vowel.insert(3, 'u')  # .insert(index, element)

   '''
   # to reverse a list
   >>> array = list('spongebob') 
   >>> reversed(array) # doesn't work
   <list_reverseiterator object at 0x035D2790>
   >>> list(reversed(array))
   ['b', 'o', 'b', 'e', 'g', 'n', 'o', 'p', 's']
   >>>
   '''


   # assigning list elements to multiple variables
   array = [1,2,3,4,5]
   a,b,c,d,e = array
   # this will assign a the value of 1, b the value of 2 and so on...

   '''
   example
   >>> array = [2,4,6,18]
   >>> gerry, bob, tim, jim = array
   >>> gerry
   2   
   >>> time
   Traceback (most recent call last):   
   File "<stdin>", line 1, in <module>
   NameError: name 'time' is not defined
   >>> time
   Traceback (most recent call last):   
   File "<stdin>", line 1, in <module>
   NameError: name 'time' is not defined
   >>> tim
   6   
   '''

   # delete elements of an array using del, remove() and pop()
   colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
   # deleting by index
   del colors[4]
   # deleting by value
   colors.remove("blue") # removes only the first occurrence
   colors.pop(3) # .pop(index) deletes and returns the element
   print(colors)

   # slicing lists
   # array[startindex:end:step]
   animal = ["dog", "cat", "cow", "pig", "giraffe"]
   print(animal[1:4]) # animal[start:end] items start through end-1
   print(animal[-3:-1])
   print(animal[2:]) # animal[start:] items start through the rest of the array
   print(animal[-4:])
   print(animal[:3]) # animal[:end] items from the beginning through end-1
   print(animal[:]) # copy of the whole array
   print(animal[1:4:2]) # animal[start:end:step]  start through not past end, by step

   # two dimensional lists

   # creating 2D lists
   array = [1, 2, [3.1, 3.2, 3.3], 4]
   array[2][1] # fetching values
   array[2][2]
   array[2][0] = 5 # assigning values
   print(array)

   # tuples cannot be modified, read only  - no add, delete
   tuple = (5, 6, 7, 18) # () parenthesis to create tuples
   print('Tuple:', tuple)
   print("Tuple index 1:", tuple[1])  # number in square bracket is index of element you want to access

   # define sets
   x = set('python')
   y = set('powershell')

   print(x - y) # All the elements in x but not in y
   # union
   print(x | y) # Unique elements in x or y or both
   # intersection
   print(x & y) # Elements in both x and y
   print(x ^ y) # Elements in x or y but not in both
   ```

- [Back to top](#top)

### Dictionaries

   ```python
   #######################################################
   # hastables/dictionary
   # note a comma (,) after each key-value pair
   # and colon (:) between the Key-value pair instead of 'equals to' (=) used in PowerShell
   table = {} # empty hashtable
   table = dict()  # alternative way to create empty hastable

   # hashtable with integer keys
   table = {
      1 : 'one',
      2 : 'two',
      3 : 'three'
   }

   # hashtable is a data stucture that has key-value pair as a element
   table = {
      'firstname' : 'prateek', # in powershell single/double quotes around 'string keys' are optional, but not in python
      'lastname' : 'singh'
   }

   # adding key-value pairs or replace any existing key
   age = {}
   age['prateek']=27
   age['sam']=31
   age['susan']=25

   # get dictionary keys or values
   age.keys()
   age.values()

   # returns a boolean true/false if key matches
   age.__contains__('sam')

   # iterating through key-value pairs
   for key, value in age.items():
      "key: {0}, value: {1}".format(key, value)


   # created nested dictionary
   employee = {
      'name': {
         'firstname': 'prateek',
         'lastname': 'singh'
      },
      'dateofjoining': {
         'day': 1,
         'month': 5,
         'year': 2017
      }
   }

   age
   { 'gerry': 31, 'sam': 29, 'billy':10, 'sally': 18}
   # Deleting a key-value pair
   age.__delitem__('gerry')

   # accessing nested dictionary items
   print(table['name']['firstname'])
   print(table['dateofjoining']['year'])

   '''
   >>> age = {}                                                         
   >>> age['gerry'] = 31
   >>> age['sam'] = 29
   >>> age['billy']=10
   >>> age['sally']=18
   >>> age
   {'gerry': 31, 'sam': 29, 'billy': 10, 'sally': 18}
   >>> age.__delitem__('gerry')
   >>> age
   {'sam': 29, 'billy': 10, 'sally': 18}
   >>> age.pop('sam') # deletes, the key-value pair but returns the value
   29
   >>> age
   {'billy': 10, 'sally': 18}
   >>> age.popitem()
   ('sally', 18)
   >>> age
   {'billy': 10}
   >>>
   '''

   # sorting a dictionary
   numbers = {
      5 : 'five',
      3 : 'three',
      1 : 'one',
      2 : 'two',
      4 : 'four'
   }

   dict(sorted(numbers.items())) # ascending order
   dict(sorted(numbers.items(),reverse=True)) # descending order
   ```

- [Back to top](#top)

### Date and Time

   ```python
   ######
   # date and time
   import time
   from datetime import datetime
   time.localtime(time.time()) # local time
   time.asctime(time.localtime(time.time()))
   time.gmtime(time.time()) # time in UTC
   #alternatively
   str(datetime.now())

   #import time
   time.localtime()
   print('Day:',time.localtime().tm_mday) # output: Day: 6
   print('Hour:',time.localtime().tm_hour) # output: Hour: 21
   print('Minute:',time.localtime().tm_min) # output: Minute: 13
   print('Second:',time.localtime().tm_sec) # output: Second: 11

   rightnow = time.asctime(time.localtime()) # local time
   print(rightnow) # Sat Mar 21 22:56:53 2020
   # time.gmtime(time.localtime()) # time in UTC

   # formatting date time
   from datetime import datetime
   '{:%d-%b-%Y %I:%M:%S %p}'.format(datetime.now())
   # output: '06-Apr-20118 09:39:10 PM'

   '{:%d/%m/%Y %H:%M:%S}'.format(datetime.now())
   # output: '06/04/20118 21:39:25'

   # time delta
   from datetime import datetime, timedelta

   # timedelta and future/past dates
   futuredate = datetime.now() + timedelta(days=365, hours=4, minutes=2)
   pastdate = datetime.now() + timedelta(days=-365,  hours=4, minutes=2)

   '{:%d-%b-%Y %I:%M:%S %p}'.format(futuredate)

   '{:%d-%b-%Y %I:%M:%S %p}'.format(pastdate)
   ```

- [Back to top](#top)

### Misc

- Sleep

   ```python
   import time
   time.sleep(2) # sleeps for 2 seconds
   ```

- Do nothing

   ```python
   pass
   ```

- [Back to top](#top)
