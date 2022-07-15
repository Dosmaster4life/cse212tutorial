# Table of Contents
- [Introduction](#Introduction)
- [Diagrams](#Diagrams)
- [Stack Example Problem](#Stack-Example-Problem)
- [Stack Problem for you to solve](#Stack-Problem-for-you-to-solve)

## What is a Stack
A Stack is a data structure that is Last In First Out. This means whatever is on top of the stack will be the first item removed when pop() is used. ![Code example of a stack](Stack.py)

## Purpose of a Stack

A stack is used whenever the developer wants to always remove the top item first. A stack is common whenever navigating an app or a browser, whenever the back button is pressed the stack pops the current site or page and shows the previous one. Review the code below for an example.
![Code example](stackIntro.py)

## Stack Performance
The time complexty of a stack is O(1) since no loops are used.
- push("value to put on top")
- pop() # removes the top element
- peek() # returns the top element
- isEmpty() # returns true or false

## Problems that can be solved with a Stack
Any problem that uses the Last In First Out principle can be solved using a stack. An example could be a bookstack that requires the first book on top to be removed before the book below it is removed.

## How Stacks are used in Python
Stacks in python typically use a list or other structure since they are not native. Stacks are great to use whenever solving recursive problems that must remove the top item first.

## Common errors in Stacks
Popping a stack that is empty can be a problem, along with adding an item to a stack with a set size. To avoid these problems its reccommended to check the size first.


# Diagrams

As you can see in the images below, the top item always comes out first. If you wanted to break the LIFO rule, you would need to use a different data structure.

![Stack push and pop(https://i.stack.imgur.com/jLlQz.png)](stack.png)

![additional stack example(https://i.stack.imgur.com/bOga5.png)](stack2.png)

# Stack Example Problem
John needs a program that sorts document numbers for his company. Develop a program that sorts the documents numbers and puts the documents back into the stack in descending order.
 Use the [Stack.py](Stack.py) file and implement your solution. ![Code Solution](stackProblem.py)


# Stack Problem for you to solve
Joseph found a stack of his dads documents, and would like to prank him so he can't go on his business trip. Create a program that reverses the stack of documents so his dad can't make his flight. Don't look at the answer key until you finish the problem.  ![Code Solution](stackExample.py)
