---
title: Iteration
subtitle: Programming Repeated Steps
revealjs-url: ../../lib/reveal
theme: inst326
transition: slide
---

#

::: left

### **it•er•a•tion** *(ˌɪt əˈreɪ ʃən)*

*n.*

1. the act of **repeating**; a repetition.
2. a problem-solving or computational method in which a succession of
   approximations, each building on the one preceding, is used to achieve a
   desired degree of accuracy.

:::

# Loops

::: left

You often here iteration referred to as a **loop** because of the way it
modifies the behavior of your program:

:::

<img src="images/loop.jpg">


# Why Iteration?

::: left

Imagine you want to print all the positive integers less than 10. You wouldn't really want to do this:

:::

``` {.python .numberLines}
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
```

# While Loop

::: left

Instead you could use a **while loop** with a **variable** counter. This is very
useful if you want to print all the positive integers less than 1 million...

:::

``` {.python .numberLines}
i = 0
while i < 1000000:
    i += 1
    print(i)
```

# For loop

# Break

# Continue

# Iteration and Functions

