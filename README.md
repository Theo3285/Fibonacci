# com.kata.tdd.Fibonacci Sequence Kata

This kata is for practicing TDD triangulation

The algorithm is simple but the goal is to implement it with very small steps

## Requirements
The com.kata.tdd.Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it.
The 2 is found by adding the two numbers before it (1+1)
The 3 is found by adding the two numbers before it (1+2),
And the 5 is (2+3),
and so on!

Example: the next number in the sequence above is 21+34 = 55
It is that simple!

Here is a longer list:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...

## Priority Premise

### The Transformations

* ({}–>nil) no code at all->code that employs nil
* (nil->constant)
* (constant->constant+) a simple constant to a more complex constant
* (constant->scalar) replacing a constant with a variable or an argument
* (statement->statements) adding more unconditional statements.
* (unconditional->if) splitting the execution path
* (scalar->array)
* (array->container)
* (statement->recursion)
* (if->while)
* (expression->function) replacing an expression with a function or algorithm
* (variable->assignment) replacing the value of a variable.

There are likely others.

### The Process

If we accept the Priority Premise, then we should amend the typical red-green-refactor process of TDD with the following provision:

* When passing a test, prefer higher priority transformations.
* When posing a test choose one that can be passed with higher priority transformations.
* When an implementation seems to require a low priority transformation, backtrack to see if there is a simpler test to pass.

Read More about [Priority Premise](https://8thlight.com/blog/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html
)