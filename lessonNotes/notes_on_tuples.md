### Lesson 11: Tuples

1. Dr. Chuck begins this lesson by stating that tuples are really a lot like lists. In what ways are tuples like lists? Do you agree with his statement that they are a lot alike?\
Tuples are similar to lists in that they have indexes and allows programmers to store multiple items in one variable. Programmers can then access items from this variable by giving an index as an argument, just like a list. Yes, I agree with this statement because they behave the same in a lot of ways. The only major difference when identifying one or the other is that tuples use parenthesis instead of brackets.

2. How do tuples essentially differ from lists? Why do you think there is a need for this additional data type if it is similar to a list?\
The difference is that tuples are immutable, meaning that they can not be changed. Like a string, once a tuple is created, programmers can't change the contents within it. Being immutable also means that tuples can't be modified. Functions like `append`, `sort`, or `reverse` won't work because they would be changing the original tuple. Tuples are important in bigger programs due to them requiring less memory. Because most programs won't require programmers to use a list throughout the program, tuples will usually be more efficient since programmers will only interact with them for a few lines. It also lowers the risk of programmers creating bugs because tuples are constant, meaning that they will always remain the same.

3. Dr. Chuck says that tuple assignment is really cool (Your instructor completely agrees with him, btw). Describe what tuple assignment is, showing a few examples of it in use. Do you think it is really cool? Why or why not?\
Tuple assignment allows programmers to assign multiple values into multiple variables at the same time. For example:

```
>>> (age, name) = (17, "Meiji")
>>> print(age)
>>> print(name)
17
Meiji

>>> list = [[1, 2, 3, 4]]
>>> for i in list:
>>>     (a, b, c, d) = i
>>> print(a, b, c, d)
1 2 3 4
```
It is a cool feature of Python because it provides a quicker and more flexible way of assigning variables. Programmers can assign multiple values in just one line of code, which can make code cleaner.

4. Summarize what you learned from the second video in this lesson. Provide example code to make support what you describe.\
In the second video, it showed me ways to manipulate tuples. Because tuples are immutable, they can be a pain to manipulate if programmers ever run into a situation where they need to do something with them. In order to avoid this problem, programmers can combine lists with tuples. Because lists are mutable, programmers can now manipulate tuples by using list methods. For example:

```
>>> capitals = {"New York": "Albany", "Virginia": "Richmond", "Alaska": "Juneau"}
>>> print(capitals.items())
dict_items([("New York", "Albany"), ("Virginia", "Richmond"), ("Alaska", "Juneau")])
>>> print(sorted(capitals.items()))
[("Alaska", "Juneau"), ("New York", "Albany"), ("Virginia", "Richmond")]
```
In the example above, a dictionary, `capitals`, is created that states a state and its capital. We then use the function, `items`, to convert the dictionary into a list of tuples which can be seen when we print it out. Because we converted the dictionary into a list, we can use list methods on it without getting an error. `sorted` is used to sort the tuples within the list in ascending order, or from a-z.

5. In the slide titled Even Shorter Version Dr. Chuck introduces list comprehensions. This is another really cool feature of Python. Did the example make sense to you? Do you think you understand what is going on?\
Yes, the example makes sense to me because I have incorporated it into my own code. The program that Dr. Chuck wrote basically shortens the code down to one line. He changes the syntax of the for loop to make it only one line and puts brackets around it to convert each iteration into an item in the list. The items, in this case, are tuples. The `sorted` function will then sort the list.   
