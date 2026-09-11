
""" string  """
s = 'the kiran academy'
# print(s.upper())
# print(s.lower())
# print(s.title()) # first letter capital
# print(s.capitalize())
# print(s.isnumeric())
# print(s.isalnum())
# print(s.isalpha()) # if isnumeric, isalnum , isalpha is using then foucus on space.
# print(s.index('z')) # it will give error if value not found 
# print(s.find('z'))   # it will retrun -1
# print(s.count('z'))
# print(s.replace('the','this is the '))
# print(s.split())
# print(sorted(s))

# print(s[0:10])
# print(s[-10:-1:1])
# print(s[10:2:-1])
# print(s[2:10:-1]) # reverse indexing is not possible

""" 1. list = order, mutable , heterogeneous element is present , duplicate are allowed 
"""

l = [34,56,43,28,92,56]
"add method"
# l.append(8)
# l.insert(8,65)
# l.extend({1:3,3:7})    # only accept the list  of element
# print(l)

"udpade method"
# l[3]=00
# print(l)

''' delete method'''
# print(l.remove(0))    # give value error if element is not found
# print(l.pop())        # if index is not give then delete the last element and give the index error
# print(l.pop(9))
# print(l.clear())
# del (l)
''' some other method '''
# l.sort()
# print(l)
# l.reverse()
# print(l)

'2. tuple = ordered , immutable , heteregenous element is present and duplicate are allowed'
'indexing is allowed because ordered '
'we can not add udpdate and delete element into the tuple because of immutable '
t = (2,3,4,5,6,7,9,76)
'but it follow some method'
# print(t.count(0))
# print(t.index(0))       # if not found value then get the value error

'3. set = unordered , mutable , heteregenous collection of immutable element and duplicate are not allowed '
' we can  add int , string , bool , float because this are the immutable element'
'add and delet are only performed , set give different ouput of stored element '
s = {3,66,43,67,89}
' add method '
# s.add(88)
# s.update([7,54,54]) # only accept iterable 
# print(s)

'delete method'
# print(s.remove(89))  # return  key error if elemetn is not found.
# s.pop()              # delete random value for the set & return the number.
# s.discard(0)         # not return none if element not found.
# print(s)


'some other method'
# s1 ={1,2,3,4,5}
# s2 = {4,5,6,7,8,9,0}

# s1.update(s2)
# s=s1.union(s2) # it inclue all element exclude common
# s.intersection(s2) # it give common element from both set
# s.difference(s2)     #all elemnts from your 1st set excluding common and all element from 2nd set
# print(s1)

'4. dict = ordered , mutable, heteregenous collection of element where data is prsent in key and pair'
'not allwed key like list , set dict '
# how to access the element 
d = {1:2 ,4:6,56:43,87:100}
''' access the element '''
# print(d[0])          # give the key error 
# print(d[1])  
# print(d.get(0))
# print(d.get(0,90))


' add the element '
# d[89]=90
# print(d)

'update the element'
# d[90]=800
# d.update({1:4})
# print(d)

'delete'
# print(d.pop(0))    # delete the element and retrun the element
# print(d.popitem()) # return last element in tuple & no argument is accepted
# del d
# d.clear()
# print(d)

# items.insert(2,('c',3)) #[('A', 4), ('B', 2), ('c', 3), ('c', 3), ('C', 3), ('D', 4)]
# items = list(d.items())
# print(items)

' how to acces the element '
# print(d.keys())         #dict_keys([1, 4, 56, 87])
# print(d.values())       # dict_values([2, 6, 43, 100])
# print(d.items())        # dict_items([(1, 2), (4, 6), (56, 43), (87, 100)]) give output in form of tuple
# for i in d:
#     print(i) # print keys
# for i in d:
#     print(d[i]) # print value
# for i in d.keys():
#     print(i)
# for i in d.values():
#     print(i)
# for i in d.items():
#     print(i)          # retrn value in tuple

# print(bool(1)) # true
# print(bool(0)) #false
# print(bool('')) #false
# print(bool(' '))# true
# print(bool('')) #false
# print(bool(None)) #false

'function'
'Parameter = variable in the function definition.'
'Argument = actual value passed to a function.'
# type of function
# 1.  Built in function  ex type , id
# 2. user define function  ex. my_fun(), sun()
# 3. recursive function
# 4. Lambda function or anonymous function  ex.d=lambda x:x*4 d(6)  #A lambda function is a small anonymous function (a function without a name) that is usually used for a simple operation.


# 'Iterable: An object that you can loop over using a for loop.'
# numbers = [1, 2, 3]
# for n in numbers:
#     print(n)

# Iterator: An object that gives you one item at a time using next(). An iterator is created from an iterable using iter().
# numbers = [1, 2, 3]
# it = iter(numbers)

# print(next(it))  # 1
# print(next(it))  # 2

# Generator: A special type of iterator that generates values one at a time, usually using the yield keyword. It is useful for saving memory.
# def numbers():
#     yield 1
#     yield 2
#     yield 3

# for n in numbers():
#     print(n)

# difference 
# 1. to create iterator iter() is used and for generator yield is used
# 2. generator used the yield keyword . it save the local variable
# 3. generator in python helps  us to write fast and compact code.
# 4. python iterator is much more memory efficient.

'decorator = it takes other function as input, add addition functionality and return it'
# it is callable python object which modifies other function/class

# def decor(f):
#   def inner():
#     f()                # exixting function
#     print('welcom')    # add new function
#   return inner

# def printer():
#   print('welcom')
#   print('welcome')

# decor(printer)


# def decor(printer):
#   def inner():
#     printer()                # exixting function
#     print('welcom')    # add new function
#   return inner
# @decor
# def printer():
#   print('welcom')
#   print('welcome')

# printer()


# def dec(ad):
#   def inner():
#     result = ad()
#     c = eval(input ('enter 3 no: '))
#     result = c + result
#     return result
#   return inner

# @ dec
# def ad():
#     a= eval(input('enter 1st no: '))
#     b= eval(input('enter 2st no: '))
#     result = a+b
#     return result

# print(ad()) # this print is import to display the output


""" ------------------------------ practice  content -----------------------------------------------"""

"q) how to add list in dict"
l1 = ['A','B','C','D']
# l2 = [1,2,3]
# my_dict1 = dict(zip(l1,l2))
# print(my_dict1)

"Q) how to add dict in list"
d ={'A': 1, 'B': 2, 'C': 3, 'D': 4}
# l=[]
# for i,k in d.items():
#   l.append(i)
#   l.append(k)
# print(l)

# for i in d.items():
#   for d in i:
#     l.append(d)
# print(l)

# l = [x for pair in d.items() for x in pair]
# print(l)

"Q) how to find the factorial"
# def factorial(n):
#   if n==1:
#     return 1
#   else:
#     return (n*factorial(n-1))

" Q) just for the remember"
# def add(x,y):
#   return x+y
# def apply_operation(a,b,c):
#   return a(b,c)     #add(21,22)

" Q) print the fibnachi series"
# def fib():
#   n = int(input('Enter the number'))
#   l = [0,1]
#   for i in range(2,n):
#       next_item = l[-1]+l[-2]
#       l.append(next_item)
#   print(l)
# fib()
'Q) ? How to find square root of a number'
# x = 2
# for i in range(1,x):
#     r =i * i
#     if r == x:
#        print('this is the squre root of x',i)
#        break
# else:
#     print('not found')
"Q)? How to find area of triangle ? How to check leap year "
# b = 10
# h = 87
# print('area of trignage',1/2*(b*h))

# def t(b,h):
#     return 1/2*(b*h)

# area =t(54,43)  # if you are returning something the you have to create variable to catch that return
# print(area)
'leap year'
# def l(n):
#     if n%4 == 0:
#      print('this is the leap year')
#     else:
#        print('not')
# l(6000)


"Q) how to generate random no " 
# import random

# x = random.random()
# print(x)

# x = random.randint(1, 10)
# print(x)

# numbers = [10, 20, 30, 40, 50]
# x = random.choice(numbers)
# print(x)

'? How to generate all the numbers from 0 to 100 | even numbers | odd numbers | '
# for i in range(1,101):
#     if i%2 == 0:
#       print(i)

# for i in range(1,101):
#     if i%2 != 0:
#       print(i)

'? Find even(/odd) numbers from a list and store them only even numbers into a list '
# a=[54,43,78,90,23,56,75,12,78]
# l=[]
# for i in a:
#     if i%2 == 0:
#         l.append(i)
# print(l)
'check the no is prime is not'
# n= 12
# h=0
# for i in range(2,n):
#     if n%i == 0:
#         h=1
#         break
# if h == 1: 
#  print('not prine')
# else: 
#    print('is prime')

'? How to print prime numbers from 0 to 20 and store them into a list '
# l=[]
# for i in range(2,21):
#     p=0
#     for r in range(1,i+1):
#         if i%r==0 :
#             p+=1
#     if p == 2:
#         l.append(i)
# print(l)
" check factorial "
# n = 5
# fact = 1

# for i in range(1, n + 1):
#     fact = fact * i

# print(fact)
' Check whether a number is Armstrong or not'


'? Find sum of natural numbers'
# sum =0 
# for i in range(1,20):
#     sum = sum +i
# print(sum)

'? Write a Fibonacci series program ? Write a palindrome '

# l =[0,1]
# a, b = 0,1
# while a<=20:
#     c = a+b
#     l.append(c)
#     a= b 
#     b =c
# print(l)

'? Write a program to reverse the string'
# s = 'saksdhie'
# a=''
# for i in s:
#     a = i+a
# print(a)

'? Write a program to remove space from a string '
# s = 'a ld kei'
# a=''
# for i in s:
#     if i == ' ':
#         continue
#     a = a+i
# print(a)
'? Convert string to a list or vice versa '
# s = 'ldkoen'
# l=[]
# for i in s:
#     l.append(i)
# print(l)
# l = ['l', 'd', 'k', 'o', 'e', 'n']
# s =''
# for i in l:
#     s = s+i
# print(s)

'find the substring'
# s = "hello world"

# if "world" in s:
#     print("Substring found")
# else:
#     print("Substring not found")

'? Find the frequency of word appearing in a string '
# s = 'aldkieanalda'
# print(s.count('ea'))

'? How to check if a word is a valid keyword or not in python '
# import keyword

# word = input("Enter a word: ")

# if word in keyword.kwlist:
#     print("Valid Python keyword")
# else:
#     print("Not a Python keyword")

'? How to check the URL in a string by using python '
# import re

# s = input("Enter a string: ")

# pattern = r"https?://\S+"

# if re.search(pattern, s):
#     print("URL found")
# else:
#     print("URL not found")












        


