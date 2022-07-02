# Table of Contents
-[Introduction](#Introduction)
-[Stack Diagrams](#Diagrams)
-[Stack Example Problem](#Example)
-[Stack Problem](#Problem)

A Stack is a data structure that is Last In First Out. This means whatever is on top of the stack will be the first item removed when pop() is used. 

## Purpose of a Stack

A stack is used whenever the developer wants to always remove the top item first. A stack is common whenever navigating an app or a browser, whenever the back button is pressed the stack pops the current site or page and shows the previous one.

## Stack Performance
The time complexty of a stack is O(1) since no loops are used in the following
**push
**pop
**peek

## Problems that can be solved with a Stack
Any problem that uses the Last In First Out principle can be solved using a stack. An example could be a bookstack that requires the first book on top to be removed before the book below it is removed.

## How Stacks are used in Python
Stacks in python typically use a list or other structure since they are not native. Stacks are great to use whenever solving recursive problems that must remove the top item first.

## Common errors in Stacks
Popping a stack that is empty can be a problem, along with adding an item to a stack with a set size. To avoid these problems its reccommended to check the size first.


# Diagrams