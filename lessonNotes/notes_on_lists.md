### Lesson 9: Lists

1. In the first video of this lesson, Dr. Chuck discusses two very important concepts: algorithms and data structures. How does he define these two concepts? Which one does he say we have been focusing on until now?\
Dr. Chuck defines algorithms as the steps that are used in order to solve a problem. This is the concept that we've been focusing up until now. However, there's another part of programming which is data structures. Unlike algorithms, data structures focus on creating ways to make the data do what programmers want it to do.

2. Describe in your own words what a collection is.\
As the name indicates, a collection is a group of things. More specifically, it is a group of values. A collection is when programmers assign multiple values to a single variable. A list is an example of a collection because programmers can add in as many values as they want into the list and it will store it in a single variable.

3. Dr. Chuck makes a very important point in the slide labeled Lists and definite loops - best pals about Python and variable names that he has made before, but which bares repeating. What is that point?\
The point he makes again is that Python, as well as every other programming languages, is very literal. In his example, he made the iteration variable, `friend`, and the list variable, `friends`. Even though the latter is just a plural form of the former, Python will not know this and treat it as two different things. Thus, the iteration variable is up to the programmer to call it whatever they want as it will not affect how the loop will iterate through a list.

4. How do we access individual items in a list?\
Similar to how we get individual characters from a string, getting items from a list works the same way. We use square brackets ([]) in order to indicate the index of the item that we want to select. Like a string, the index in a list will start from 0 (the first item will be the 0th index) instead of 1.  

5. What does mutable mean? Provide examples of mutable and immutable data types in Python.\
Mutable means changeable. In Python, an example of a mutable data type is lists and an immutable data type would be strings.

Mutable data:
```
>>> number_list = [8, 9, 24, 57]
>>> print(number_list)
[8, 9, 24, 57]
>>> number_list[1] = 33
>>> print(number_list)
[8, 33, 24, 57]
```
As seen here, the list changes when the number "9" is replaced with "33" due to "33" being assigned to the first index in `number_list`.

Immutable data:
```
>>> fruit = "Orange"
>>> print(fruit)
Orange
>>> fruit.lower()
>>> print(fruit)
Orange
```
As seen here, the initial value of `fruit`, which is "Orange," will not change. In order to actually change it, we would have to assign it to another variable. This is different from the example above as it didn't require us to create another variable in order to make changes.

6. Describe several list operations presented in the lecture.\
Some operations that were introduced in the video included:  concatenation, the in operator, and slicing. Concatenation is basically adding lists onto one another which combines them. For example, if you were to concatenate two separate lists together, using the "+" operator, they will combine to form one list with values from the two lists. Slicing is when you cut off parts of a list that you don't want. The ":" operator is used for this. `in` is used to check if a certain item is in a list. It will return a boolean value.

7. Describe several list methods presented in the lecture.\
Some lists methods in the video include: `append`, `sort`, and `pop`. `append` will add new items to the end of a list. `sort` will sort items in a list in alphabetical order. If the items are numbers, then it will sort them in numerical order. `pop` will remove a specified item from a list by taking an index as an argument. By default, it will remove the last item in a list.

8. Describe several useful functions that take lists as arguments presented in the lecture.\
Some functions that can take lists as arguments include: `len`, `max`, and `min`. `len` will return the number of items in a list. `max` will return the highest numerical value in a number list. `min` will do the opposite by returning the lowest numerical value.

9. The third video describes several methods that allow lists and strings to interoperate in very useful ways. Describe these.\
The method that was introduced in the video was `split`. `split` will separate words or numbers within a string into a list. Whitespace within the string will act as a divider when the string is transformed into a list. Each word or number will be an item within the list. This will be useful if programmers want to select a specific part of a string.

10. What is a guardian pattern? Use at least one specific example in describing this important concept.\
A guardian pattern is a statement placed before a statement that could return an error. It's called a guardian pattern because it helps avoid or "guard" the program from executing the statement that could return an error due to certain circumstances. In the video, the following example is given:

```       
han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    print("Line:", line)
    wds = line.split()
    print("Words:", wds)
    if len(wds) < 1:
        continue
    if wds[0] != "From":
        print("Ignore")
        continue
    print(wds[2)
```
The program here is an example of a guardian pattern because there's a statement that stops the program from returning an error. It makes sure that if the for loop encounters a blank line, it will go back to the top of the for loop and continue running in the next iteration. Without the guardian statement, encountering a blank line would return a error because the program is trying to compare the 0th index of `wds` with `"From"`. This is due to the fact that the list would be empty, meaning an index wouldn't exist for `wds` to select from. 
