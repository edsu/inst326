---
title: Fundamentals
subtitle: Variables, Expressions, Statements, Conditionals
revealjs-url: ../../lib/reveal
theme: inst326
transition: slide
---

# Topic Overview

* basic building blocks of Python programs
* a lot of content, but hopefully familiar already

::: incremental

* Variables
* Expressions
* Statements
* Conditionals

:::

# Variables 

:::

# What are Variables?

* Variables are labels that can be attached to data
* Each piece of data also has a type
* At the most basic level the types are
    - Numbers
    - Strings
    - Booleans (True/False)
* The type can be thought of like a box that contains the data
* Numbers can be further distinguished between
    - Integers
    - Floats (i.e. decimals)
* There are other, more complex data containers (e.g. lists, dictionaries) that will be introduced later

:::

## Working with Variables

* There are two main actions we take with variables:
    - assignment (attach a name to some data)
    - reading/evaluation (lookup the data by its name)

::: 

## Practice with Variables

~~~~ {.python .numberLines}
# here's an example of working with variables

x = "Hello World"   # assignment
print(x)            # reading/evaluation
~~~~

::: 

# Expressions

:::

## What are Expressions?

* Expressions are pieces of python code that get _evaluated_ rather than executed
* Expressions are often created with operators that represent mathematical or logical operations:
    - addition (+)
    - subtraction (-)
    - multiplication (\*)
    - division (/)
    - integer division (//)
    - modulo (%)
    - exponentiation (**)
    - equality (==)
* Operators are applied according to order of operations (PEMDAS)

:::

## Practice with Variables

~~~~ {.python .numberLines}
# examples of working with expressions

x = 2   # assignment
y = 7
x * x
x ** 2
x == y
y - x
y - x + 4
2 + x ** 3
(2 + x) ** 3
y // x
y / x
y % x

~~~~

:::

## Operators and Data Types

* The type of data they are applied to has an impact on meaning
* Specifically, these operators have a different meaning when applied to strings:
    - concatenation (+)
    - repetition (*)

:::

# Statements 

:::

# What are Statements?

* Statements are the most basic units of executable Python code
* On some level, a Python program is a series of statements executed in order
* In practice, it is more complicated than that, of course
* Two very simple but useful statements are print and input
* These are actually built-in functions, but we can use them to do simple input and output

::: 

## Practice with Statements

~~~~ {.python .numberLines}
# examples of simple Python statements

::: incremental
x = "Hello"
print(x)

~~~~

:::

## Practice with Statements

~~~~ {.python .numberLines}
# examples of simple Python statements

::: incremental
username = input('Enter your name: ")
print("Hello", username)

~~~~

:::

# Conditionals 

:::

# What are Conditionals?

* In practice, you often do not want every statement in a program to be executed every time
* Instead, you want to build branching logic that causes different statements to be executed depending on the state of data or input at execution time
* The basic building blocks for this logic are conditionals, which are constructed with the keywords "if", "elif" and "else"

:::

# Structure of Conditionals

* Conditionals are different from statements in that they are multi-statement structures of code
* The fist line of a conditional block begins with one of the if/elif/else keywords followed by an expression
* The first line ends with a colon
* This first line is followed by an indented block of one or more lines of code
* The indented block is only executed if the expression in the first line evaluates as "True"

:::

## Practice with Conditionals

~~~~ {.python .numberLines}
# an example of branching logic

::: incremental

order = input('What can I get you? ")
if order == 'burger':
    side = input('Would you like fries with that?')
elif order == 'salad':
    side = input('What kind of dressing?')
else:
    print('We only sell burgers and salads')
print('You ordered:', order, side)

~~~~

:::
