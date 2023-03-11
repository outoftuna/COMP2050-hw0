# Part 4: Covid Eradication

## Contents:

- [Part 4: Covid Eradication](#part-4-covid-eradication)
  - [Contents:](#contents)
  - [Classes and Methods](#classes-and-methods)
  - [Inheritance and Polymorphism](#inheritance-and-polymorphism)
  - [Exceptions](#exceptions)
  - [The Structure of Projects and Command Line Arguments](#the-structure-of-projects-and-command-line-arguments)
  - [Exercise 4. Saving Humanity from COVID19 — 50 Marks](#exercise-4-saving-humanity-from-covid19--50-marks)
    - [Part 1: `covid19_scenario.py` — 30 points](#part-1-covid19_scenariopy--30-points)
    - [Part 2: `covid_curing_agents.py` — 20 Marks](#part-2-covid_curing_agentspy--20-marks)
  - [Useful Things](#useful-things)
    - [The itertools Module](#the-itertools-module)
    - [Comprehensions — Or how much can I do in one statement?](#comprehensions--or-how-much-can-i-do-in-one-statement)
    - [Debugging](#debugging)

## Classes and Methods

As we have seen, everything in Python is an object. We can create our own types and instances of these by defining classes.

A class definition looks like this:

```python
class Student(object):
    """A class that represents a student."""
```

Here the class `Student` extends the class `object`. Every class must either extend `object` or another class. Note that if a base class is omitted (e.g. `class Student: …` instead of `class Student(object):`), then Python assumes that the class extends `object`. We describe inheritance in detail in the next section of this assignment.

Like all compound statements, we expect an indented block following a class definition. In the absence of any meaningful code we can use a docstring or the `pass` keyword.

Classes, like functions, are callable, and we instantiate a `Student` object by calling the `Student` class:

```python
>>> s = Student()
>>> type(Student)
<type "type">
>>> type(s)
<class "__main__.Student">
```

An instance of a class may have a set of attributes. These are values that we can refer to from within the instance. To set or access an attribute we use a full stop.

```python
>>> s.last_name = "Kripke"
>>> s.first_name = "Saul"
>>> s.age = 73
>>> s.courses = []
>>> s.courses.append("COMP2050")
>>> print("{0.first_name} {0.last_name}".format(s))
Saul Kripke
>>> print(s.courses)
["COMP2050"]
```

We can add an initialisation method to a class that requires these attributes to be specified when the class is instantiated.

```python
class Student:
    def __init__(self, last_name, first_name, student_number, courses):
        """ (Student, str, str, int, [str]) -> None """
        self.last_name = last_name
        self.first_name = first_name
        self.student_number = student_number
        self.courses = list(courses)
```

The initialisation method is called automatically when the class is called. If no initialisation method is defined in your class, it defaults to an empty initialisation method.

The `self` parameter refers to the `Student` object that will be created. As we will see in a moment, all methods have this as a parameter.

Add the following methods to the previous class description:

```python
def enrol(self, course_name):
     """ Enrol the student in a new course

        (Student, str) -> None
    """
    self.courses.append(course_name)

def full_name(self):
     """ Return the full name of the student

        (Student) -> str
    """
    return "{0.first_name} {0.last_name}".format(self)
```

Lets try this out:

```python
>>> s = Student("Kripke", "Saul", 354)
>>> s.first_name
Saul
>>> s.enrol("COMP2050")
>>> s.courses
["COMP2050"]
>>> s.full_name()
Saul Kripke
```

Python uses a concept called "magic methods" to produce a number of different useful object behaviours. These are simply methods which adhere to certain prototypes.

Here are some important ones which you can implement in your own classes:

- `__init__(self, ...)` — Called when an instance of the class is created.
- `__str__(self)` — Returns a readable string representing the object. Called when the object is converted into a string or printed.
- `__repr__(self)` — Returns an unambiguous string representing the object. Called when the object is printed as part of a collection (list, etc.)
- `__contains__(self, item)` — Used with the in keyword. This should return `True` iff object `item` is "in" `self`, where "in" is whatever makes sense for your class.

In Python, nothing is truly private and it is impossible to hide the inner workings of a class from the users of this class.

Having said that, there is still a way to make methods and attributes private. Simply prefix their names with two underscores.

Python then renames this using a standard scheme. If we know the scheme that it uses to do this renaming, then we can still access these values.

We will leave it as an exercise for interested readers to find out how this works on their own.

## Inheritance and Polymorphism

Python allows for classes to inherit from other classes and override the attributes and methods of the original class. It allows for some complicated things like multiple inheritance, but that is outside the scope of this tutorial.

Lets look at a simple example of how inheritance works.

```python
class A:
    """ Class A inherits from the object class.
        All classes inherit from object by default.
    """

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def __str__(self):
        return "An object with the following attributes: {}, {}" \
            .format(self.attr1, self.attr2)

    def action1(self):
        print("Performing action 1:", self.attr1, self.attr2)

class B(A):
    """ Class B inherits from the A class. """

    def __init__(self, attr1, attr2, attr3):
        super().__init__(attr1, attr2)  # Execute the initialiser from class A
        self.attr3 = attr3

    def __str__(self):
        return "B object with the following attributes: {}, {}, {}" \
           .format(self.attr1, self.attr2, self.attr3)

    def action2(self):
        print("Performing action 2:", self.attr1, self.attr2, self.attr3)
```

In this case `B` overrides the `__init__` and `__str__` methods of `A`, but inherits the method `action1`. It introduces a new method `action2`.

Notice at the start of the `__init__` method in `B` we call the `__init__` method in `A`. This is standard practice and should be used whenever one class inherits from another.

The inheriting classes do not need to be in the same file. `B` could inherit from `A` by importing `A` and then using it.

## Exceptions

Whenever a runtime error occurs, Python creates an exception. The program stops running at this point and Python prints out the execution trace which ends with the exception that occurred.

For example, dividing by zero creates an exception:

```python
>>> print(55 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
```

We can deal with errors without overreacting by using `try` and `except` statements.

We have a `try` block followed by one or more `except` blocks and an (optional) `else` block that is executed if no exceptions were raised in the `try` block.

```python
try:
    # Do things here...
except IndexError:
    print("Our index was invalid.")
except (ValueError, IOError) as e:
    print("Type conversion error or IO error".format(e.message))
else:
    print("Everything was ok.")
```

We can raise our own errors with the raise statement.

```python
raise ValueError("{} is not a valid age".format(age))
```

Exceptions are classes which all inherit from `BaseException`. Catching a parent exception will catch exceptions with classes that inherit from it. The exception hierarchy is described [here](http://docs.python.org/3/library/exceptions.html).

We can define our own exception types be defining classes that inherit from the class `Exception` and then use these are normal.

```python
class GradeError(Exception):
    """ This error is raised when we encounter invalid grades. """
```

## The Structure of Projects and Command Line Arguments

Large Python projects will usually be supplied in multiple files. When a project is run, a file is run by the interpreter which will then import the other files as needed.

It is possible that some files are both intended to be run directly and to be imported, with different behaviours expected in each case. For example, you might make your own maths library which is designed to be imported, but when it is run a set of performance benchmarks are performed.

To achieve this we can take advantage of an attribute that Python gives to files when they are run or imported.

Every file has an attribute `__name__`. When the file is imported `__name__` is set to the name of the module. When the file is run directly, it is set to `"__main__"` This allows the following design pattern:

```python
def main():
    """ do stuff """

if __name__ == "__main__":
    main()
```

By putting your code in main, you avoid polluting the namespace of the module, making it easier to avoid errors.

It is sometimes desirable to package a set of modules together. In Python this is possible by putting them all in a directory together and then placing in it a file called `__init__.py`, which should import all of those things from the modules in the package which are intended to be accessible when using the package.

When we run a Python file, it is possible to supply command line arguments:

```python
python3 test.py arg1 arg2 arg3
```

These can then be accessed as follows:

```python
import sys

print("Number of arguments: {} arguments.".format(len(sys.argv)))
print("Argument List: {}".format(sys.argv))
```

## Exercise 4\. Saving Humanity from COVID19 — 50 Marks

In this exercise you will develop a simple agent to eradicate a highly infectious disease COVID19 that spreads rapidly.

You will model the spread of COVID19 throughout the world, regions by regions.

COVID19 can spread through droplet and it's hard to detect them. If we cannot quarantine the whole region, it will become a major thread to the world.


Your task is to develop an agent that manages the infection and eventually cure it. The real world problem is complicated but we will make it simple here.

The exercise is dived into 2 parts:
1. Write a class that represents the COVID19 infection scenario - 30 points.
2. Write a simple agent which uses this scenario class and attempts to cure the COVID19 infection - 20 points

The following files are supplied for this exercise:

- `covid_simulation.py` - tests `covid19_scenario.py` and runs simulations with your agent;
- `covid_scenario.py` - reads in scenario files and stores the relevant information. Simulates the spread of COVID19 and your agent moving around.
- `covid_curing_agents.py` - describes agents which move around a world described in `covid19_scenario.py` and attempt to eradicate the infestation.

When you submit your assignment, submit the files `covid19_scenario.py` and `covid19_agents.py`. As with the previous exercises, your code should be commented appropriately.

### Part 1: `covid19_scenario.py` — 30 points

As you complete this exercise, you should validate your code by running `covid19_simulation.py` in testing mode. Type `python3 covid19_simulation.py` to get instructions on how to do this.

Ensure that the directory containing the test files `exercise4_maps` is in the directory that you are running `covid19_simulation.py` from.

In the file `covid_scenario.py` make a class called `COVID19Scenario` with the following methods.

**`read_scenario_file(self, path_to_scenario_file)`** This method should read a scenario from the given file and store the relevant information.

- The function has the following type string: `(CoVID19Scenario, str) -> bool`
- The scenario file will be expected to have the following lines, and correctly
  formatted files can be assumed:
  - `threshold x` — where `x` represents the required number of covid patients before
    it starts to spread to other locations. If the number of covid patients at a location
    is at least `x`, it will spread. Store this value in a variable called `threshold`.
  - `growth x` — where `x` represents the growth rate of the covid patients at a
    location. In a scenario with a growth rate of 0.2, 20% more covid patients are added to
    each location at every step. Store this value in a variable called `growth`. Note
    the number of covid patients at a location will always grow in this sense, even when the population is below the threshold.
  - `spread x` — where `x` represents the fraction of covid patients that will
    spread to neighbouring locations at each step, given that the spreading location has a 
    population greater than or equal to `threshold`.
    Store this value in a variable called `spread`.
  - `location loc` — where `loc` is a string representing a location in the
    problem. Store each of these entries in a list called `locations`.
  - `start loc` — where `loc` is a string representing the starting location
    of the curing agent in the problem. Store the starting location in a variable
    called `location`, which will be used to keep track of current location of
    the agent throughout the simulation.
  - `covid loc x` — where `loc` is a string representing a location and `x`
    is the number of the covid patients at that location in the beginning of 
    the scenario. Make a dictionary called `covid` which maps locations to their number of covid patients. **By default, locations should have `0` covid patients**.
  - `conn loc1 loc2` — where `loc1` and `loc2` are strings representing
    locations. This indicates that there is a track between `loc1` and `loc2`.
    Store these tracks in a dictionary called `conn`. This dictionary should
    map each location to a **set** of locations it is connected to. Tracks are
    symmetrical and the `conn` dictionary should reflect that by containing
    links in both directions. Locations which are connected to nothing should
    map to an empty set.
- All of the variables you create should be stored in the current instance of
  the class — i.e. using the `self` parameter of the method.
- The function should return `True` if it was successful, and `False` in the
  case an IOError occurs. Other Exceptions can be ignored.
- In summary, `read_scenario_file` will create the following variables with the
  specified types:
  - `threshold` — `float`;
  - `growth` — `float`;
  - `spread` — `float`;
  - `location` — `str`;
  - `locations` — `[str]`;
  - `covid` — `{ str : float }`;
  - `conn` — `{ str : set([str]) }`.

**`valid_moves(self)`** This method should return a list of valid moves. Each
valid move is either a neighbouring location or the current location of the
agent (which indicates that the agent stays put).

- This method has the type string: `(COVID19Scenario) -> [str]`

**`move(self, loc)`** This method should move the agent to the specified
location and cure the covid patients there — i.e. set covid to `0`. If the
method attempts to move the agent to a location that is invalid given the
current location (i.e. there is no connecting track), the method should raise a
`ValueError`. The agent is allowed to stay where it is (i.e. move to the
current location).

- This method has the type string: `(COVID19Scenario, str) -> None`

**`spread_covid(self)`** This method should spread covid according the
threshold, growth, spread, and connections between locations.

- Covid only spreads to adjacent locations if the spreading location has
  a covid patients greater than or equal to the threshold level. Covid 
  will not spread to a location where the agent is.
- Covid grows and spreads at all locations at the same time. This means that
  a location `loc`, which has `d = covid[loc]` at the start of the method
  call, will have an additional `growth * d` covid, plus contributions from
  its neighbours. It will spread `spread * d` to its neighbours, if
  `d ≥ threshold`. Covid will not grow at the current location of the agent.
- For example, if we have two connected locations `loc1` and `loc2` with
  covid `5` and `10` respectively, and the `threshold` is `6`, `growth` is
  `0.2`, and `spread` is `0.1`, then after growth and spreading `loc1` will
  have `(5 * 1.2) + (10 * 0.1) = 7` covid and `loc2` will have
  `(10 * 1.2) = 12` covid.
- This method has the type string: `(COVID19Scenario) -> None`

These methods can be tested by running `covid_simulation.py` in testing mode as described at the beginning of this exercise.

Your code needs to pass all tests before continuing on to the next part of the assignment.

To help you debug the code, you can turn on the visualisation mode, e.g. `python3 covid_simulation.py --viz`. This will show a graph like below. To manually take a step through the simulation, press `Enter` in the terminal. Note that
if you're not using Anaconda, you first need to install the `networkx` package:
`pip install networkx`.

![graph](graph.jpg)

### Part 2: `covid_curing_agents.py` — 20 Marks

In the file `covid_curing_agents.py` there is a class called `COVID19CuringAgent`. This defines an agent which, very poorly, attempts to control the spread of covid19. In each step of the simulation, it will move to the adjacent location with the most covid patients. If no adjacent locations have any covid patients, it will move randomly.

You should extend `COVID19CuringAgent` with your own agent class called `SmartCOVID19CuringAgent` and implement an appropriate `choose_move` method. Note that your `choose_move` method must have the same parameters as that in `COVID19CuringAgent` (i.e. you cannot add extra parameters)

Feel free to add other helper methods and classes if needed.

Test your agent with the scenarios in the `exercise4_maps` subdirectory.

Whenever the simulator is not run in Testing mode, a file called `XXXX.results.json` is created. It contains a summary of the outcomes of the simulations in a JSON document. For each run of the simulator the final number of covid patients, number of simulation steps and score are stored. You will also see that the average_score is also available.

Run `python3 covid_simulation.py` to find out how to run several simulations. Do not edit or submit the `covid_simulation.py` file.

The number of marks you get in this exercise depends on how good the performance of your agent is compared to that of `COVID19CuringAgent` over the five given scenarios. It is not necessary to cure all covid patients in all places to get full marks. We will use the following parameters to evaluate your agent:

```
-H 100 -n 100
```

that is, over 100 simulation runs, each run with a maximum of 100 steps. The algorithm should run fast. If it takes more than a few seconds to run all simulations, try a simpler approach.

Don't forget that you need to comment your code to explain which algorithm you're using and/or how it works.

## Useful Things

The following sections of this tutorial are non-compulsory, but they introduce some powerful features of Python, which might make your life a lot easier, so it is recommended that you read them some time.

### The itertools Module

The `itertools` module contains a set of powerful functions to deal with iterators. They can save you a lot of time and effort.

A thorough overview of the module can be found [here](https://docs.python.org/3/library/itertools.html).

We will cover just a few examples here.

First, `itertools.chain` provides an easy way to combine multiple iterators into a single iterator:

```python
>>> import itertools
>>> x = range(1, 3)
>>> for item in itertools.chain(range(5, 7), x, range(11, 13)):
        print(item)
5
6
1
2
11
12
```

Next, `itertools.combinations` can generate all (unordered) combinations of a given size from elements in an iterator:

```python
>>> list(itertools.combinations("abcd", 3))
[('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
```

Next, `itertools.product` can generate Cartesian products from a list of iterators:

```python
>>> x = [[True, False]] * 3
>>> x
[[True, False], [True, False], [True, False]]
>>> list(itertools.product(*x))
[(True, True, True),
 (True, True, False),
 (True, False, True),
 (True, False, False),
 (False, True, True),
 (False, True, False),
 (False, False, True),
 (False, False, False)]
```

Here, the `*` before `x` in the call to `itertools.product` unpacks the elements of `x` into the arguments of `itertools.product`. It is equivalent to calling the function with three lists of the form `[True, False]`.

This final call would have been helpful in Exercise 2.

### Comprehensions — Or how much can I do in one statement?

You may have noticed that Python is a very compact language. It is not uncommon to feel a sense of exhilaration when you realise that you can solve problems often with a small fraction of the number of lines of code that would be required in C++ or Java.

Lets take this even further and put a for loop inside the definition of a list.

```python
>>> [x ** 2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

What about making a dictionary which maps the letters of the alphabet to their position in the alphabet?

```python
>>> alph_index = dict([(a,  i) for i, a in enumerate("abcdefghijklmnopqrstuvwxyz")])
>>> alph_index["j"]
10
>>> alph_index["z"]
25
```

We can nest loops and even add conditionals. What if want a list of all coordinate pairs in a grid, except those points on the diagonal?

```python
>>> [(x, y) for x in range(5) for y in range(5) if x != y]
[(0, 1),
 (0, 2),
 (0, 3),
 (0, 4),
 (1, 0),
 (1, 2),
 ...
```

It is easy to go overboard with list comprehensions and make your code hard to read. So keep them simple!

Having said that, it might be a fun exercise at this point to think about how to use a list comprehension to compute all prime numbers up to a given bound.

### Debugging

It is inevitable that you will make mistakes in your code, and then it may take you some time to find where exactly the problem is before you can correct it.

The classic debugging technique of adding print statements can work well for small and simple programs, but there are more elegant and effective tools like `pdb` which can save you a lot of time.

To use pdb you can set a breakpoint in your program by including the line 
```python
  import pdb; pdb.set_trace()
```
where you want execution to halt.
For instance, consider the following code
```python
  x = 2
  y = 3
  import pdb; pdb.set_trace()
  x = x * y
```
If you run this code execution will halt after `y` has its value assigned, and your shell will print out which line it is up to.
At this point the shell allows you to enter text.
We can take a look at the values of variables `x` and `y` by simply typing their names into the shell, e.g.
```python
  >>> x
  2
  >>> y
  3
```
You can even assign variables new values
```python
  >>> x = 4
```
Being able to look at variable values and modify them is already very powerful (and supercedes print statements), but we can also step through the code.
Some useful commands are

- `help` — brings up the help menu
- `step` — execute next line and step into the function if applicable (i.e. if the line is a call to another function we will pause at the first line of that function)
- `next` — execute next line and step over functions (i.e. if there is a call to a function we execute the whole call and pause at the next line after the function)
- `continue` — run the program until the program encounters a breakpoint or terminates
- `list` — shows you which line the program is up to.

Note that with each of these you can type just the first character with the same effect e.g. `h` instead of `help`.

This very brief overview gives you some useful tools, and hopefully convinces you to move away from print statements as the go-to debugging technique! 
We encourage you to look up some tutorials or cheat sheets to get up and running.

And that's the end of Homework 0 :-)
