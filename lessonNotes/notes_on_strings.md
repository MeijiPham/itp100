### Lesson 6 Notes: Strings

1. What does Dr. Chuck say about indexing strings? How does this operation work? Provide a few examples.\
Dr. Chuck says that we can get a single character in a string by using square brackets that specify said character's index.

```
fruit = "apple"
second_index = fruit[2]
third_index = fruit[3]
print(second_index)
print(third_index)

p
l
```
2. Which Python function returns the number or characters in a string? Provide a few examples of it being used.\
The built-in function, `len`, gives us the number of characters in a string.

```
print(len("apple"))
print(len("pear"))

5
4
```
3. Discuss the two ways Dr. Chuck shows to loop over the characters in a string. Provide an example of each.\
Dr. Chuck's first way of looping over characters in a string is to use the while loop, an iteration variable, and the len function.

```
fruit = "apple"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

a
p
p
l
e
```
The second way to do this is to use a for loop.

```
fruit = "apple"
for letter in fruit:
    print(letter)

a
p
p
l
e
```
4. What is slicing? Explain it in your own words and provide several examples of slicing at work. including examples using default values for start and end.\
Slicing is used when programmers want to grab a part of a sub string from the main string. As the name indicates, the string will be sliced based on the parameters (index in this case) it is given.

With 2 parameters:

```
word = "Computer"
print(word[1:5])

ompu
```

With default value at the start:

```
word = "Computer"
print(word[:7])

Compute
```

With default value at the end:

```
word = "Computer"
print(word[4:])

uter
```

5. What is concatenation as it applies to strings. Show an example.\
Concatenation is used to add strings onto one another.

```
first_word = "Hello"
print(first_word + " " + "World")

Hello World
```
6. Dr. Chuck tells us that in can be used as a logical operator. Explain what this means and provide a few examples of its use this way with strings.\
It means that `in` can be used to test the value of a boolean variable to see if a statement is either `True` or `False`.

```
fruit = "apple"
print("p" in fruit)
print("x" in fruit)

True
False
```

7. What happens when you use comparison operators (>, <, >=, <=, ==, !=) with strings?\
The strings that are being compared will be compared alphabetically using characters in each string.

8. What is a method? Which string methods does Dr. Chuck show us? Provide several examples.\
A method is similar to a function but it is used with objects instead of being independent like a normal function. Some string methods include `lower()`, `capitalize()`, `format()`, `upper()`, `replace()`, and `isspace()`.

9. Define white space.\
White space is characters that are used for spacing within a string. Python is very literal so it will count a space, or " ", as an actual character.

10. What is unicode?\
Unicode is where a programming language can understand international character sets. This makes sharing data and code with other countries easier. This is why unicode is one of the major benefits of Python 3.


 
