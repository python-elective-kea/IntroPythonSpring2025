# Introduction to Python 
## You have prepared at home
* Done the installations  tutorial
  * Github Codespaces 

## Development Environment
* Show workflow
  * Github Repo -> Open CodeSpace -> Create a branch -> push / pull etc ...

* 3 "user interfaces" we will use, good for different stuff.
  1. The interpretor
  2. The code editor (.py)
  3. Python notebook (.ipynb)

### 1. The interpretor
In the terminal type: "python"
```
$ python
Python 3.10.8 (main, Oct 17 2023, 22:43:19) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```
After the **>>>** you can type in python code and execute it by pressing **enter**
 
### 2. The code editor
In VSCode, we will create text files with a **.py** extension and write code in the file and the execute it in the terminal (or by pressing the Arrow Button)

### 3. Python Notebook files
* A text file with the **.ipynb** extension. 

## Language Introduction

* Python is an Old Language, created in 1990, Guido van Russum, Works at Google, later developed as a open source project.
* Resen years bacame more and more popular. Majority of Universities in US have it as the starting language. DTU also seem to have it as a beginning language.
* Almost all AI, Machine Learning, Data Sience are using python as its "interface".
* Python is a quick and light languges. A little task fast development, python seems to be good for this. It is frictionless. 
* Scripting language, simular to PERL, RUBY, Javascript. It does not make it inferrior, just different than compiled languages. No heavy type system. 
* Good at a quick turnaround. Not a big compile stack, you just type it and then you run it. 
* Good for small projects, prototyping, solving small coding problems.  
* Python is an interpreted (bytecode-compiled) language
  * Program called Python that reads the code and executes it emidialy. No compilor as you know it.
  * See it as a runtime compilor.
  * It is actually not so far from how java runs. also compiles into bytecode. 

## The interpretor
Type:  

````
$ python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>>
````
This opens the interpretor

This is a fantastic way to try out if and how your code works.

````
  >>> a = 12
  >>> a
  12
````
Interpretor does a Read-eval-print loop  
I type, hit return, prompt me something, and waits for my next move.

* By assigning a value to a it exists
  * Type declarations, but no keyword in front of

I can change its type:

````python    
  >>> a = 12
  >>> a
  12
  >>> type(a)
  <class 'int'>
  >>> a = 'hi'
  >>> a
  'hi'
  >>> type(a)
  <class 'str'>
````   
* No compile time type. 'a' points to whatever it points to

* Dynamically typed language
  * Not statically typed like Java
  * Change 'a' along the way
* Strongly typed
  * Like Java

## Build in functions - len()
Build in function called len

````
  >>> a = 'hello'
  >>> len(a)
  5
  >>>
````

Case sensitive

````
>>> A
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'A' is not defined
````
If python comes by a name or symbol that has not previously been defined it raises an error.

In some languages this is possible, 
* PHP5 & PERL
  * Assigned to nothing when it appears

So this is a good thing. you can debug it.

## Interpretor
The Interpretor is a good way to test if somethong works. Can i add a string and an int?

````python    
  >>> a
  'hi'
  >>> a + 1
  Traceback (most recent call last):
    File "<pyshell#62>", line 1, in <module>
      a + 1
  TypeError: can only concatenate str (not "int") to str
  >>> 
````
In java you can do this.

You can type cast it to a string (use the build in function str())

````
  >>> 'hi' + str(2)
  'hi2'
  >>>
````
## Quit
````
  >>> quit
  Use quit() or Ctrl-D (i.e. EOF) to exit
  >>> ^D
````

# Hello.py file

Create together whit me a hello.py file

LIVECODE follow.


````python

def message():
  print('Hello ')

message()

````
### args
```
def message(name):
  print('Hello ' + name)

message('Claus')

```
### return
```
def message(name):
  return 'Hello ' + name

message('Claus')
```


## Syntax

### Indentations
* no curly brace {}
  * reason: as simple as possible
    * 2 sets of brain cells
* 2, 4 spaces or tab (whole file should do the same)

````python

  def hello(name):
    if name == 'Alice' or name == 'Jens':
      name = name + '?????'
    else:
      print('Else')
  
  .....

````
### If statement
* == 
  * not like in java, here it is it
* () optional
* or, and spelled out , not signs && ||


## How python works (errors)
* Python checks a line, when it runs that line.

````python

  def hello(name):
    if name == 'Alice' or name == 'Jens':
      name = name + '?????'
    else:
      does_not_exist(names)
  
  .....

````
# Strings

## Quotes
````
  >>> a = 'Hello'
  >>> a = "Isen't"  
  >>> "I \"Love\" this exercise"
  'I "Love" this exercise'
````

## Imutable

````
  >>> a + ' it'
  "Isen't it"
  >>> a
  "Isen't"
  >>> 
````
Creating new string, original unchanged

## String methods

### getting help
```
>>> type("")
>>> help(str)
>>> dir(str)
```

````
  >>> a.lower()
  "isen't"
````
Method vs function len(a) a.lower()

Returning a new string (Imutable)
````
  >>> a.lower()
  "isen't"
  >>> a
  "Isen't"
````
Many methods

**find()**

````
  >>> a = 'hello'
  >>> a.find('e')
  1
````
**index()**
````
  >>> a = 'hello'
  >>> a.index(1)
  e
````
**count()**
````
  >>> a = 'hello'
  >>> a.count('l')
  2
````

**in**
````
  >>> a = 'hello'
  >>> e in a
  True
````

Dosins and you will have to use them soon. Type help or google



# Strings are indexed
## Look inside of a string
````
  >>> a[0]
  'h'
````
**Out of bounce**
````
  >>> a[100]
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  IndexError: string index out of range

````
**String are list of strings**
````
  >>> type(a[0])
  <class 'str'>
````

## String formating
https://realpython.com/python-f-strings/

### The intuitive way
````
  >>> a = 1
  >>> b = 'hello'
  >>> str(1) + b
  '1hello'
````

### 1. The old way
````
  >>> name = 'Claus'
  >>> age = 74
  >>> 'Hello %s, you are %s years old' %(name, age)
  'Hello Claus, you are 74 years old'
````
### 2. Str.format
````
  >>> "Hello, {}. You are {}.".format(name, age)
  'Hello, Claus. You are 74.'
````

### 3. The new way (f-strings)
````
  >>> f'Hello, {name}. You are {age}.'
  'Hello, Claus. You are 74.'

````

## Slicing

````
> s = 'Hello'
> s[1:4]

````

first including, last upto but not including    


empty means start or end

````

> s[:5]
Hello

> s[0:]
Hello

````

### Step

````
> s[0:5:2]
Hlo

> s[-1:-5:-2
ol]

````
 
 H  e  l  l  o
 0  1  2  3  4
-5 -4 -3 -2 -1


## Python source code
* Python source files use the ".py" extension and are called "modules."

To run a Python program the direct and earsiest way is:

````    
  python hello.py
````
It calls the Python interpreter to execute the code

It is like: 

````    
  javac hello.java
  java hello
````







==========

A compiler converts the source code into machine code, which can be run directly by the operating system as an executable program. Interpreters bypass the compilation process and execute the code directly. If something goes wrong it raises a flag, or "raises" a runtime error.

---

