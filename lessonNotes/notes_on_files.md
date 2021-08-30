### Lesson 8: Files

1. What function does Python use for accessing files? What arguments does it need? What does it return?\
To access files, we have to call the function, `open()`. The parameters for the function are the filename, which is required, and mode (read or write a file), which is optional. Both arguments are written as strings. It returns a file handle.

2. What is a file handle? Explain how it relates to a file? Where is the data stored?\
The file handle allows you to get to the file. It is not the file itself. It relates to a file because even though it's not where the data is being stored, it acts as a guide that allows programmers to choose how they want to reach the file. The data is stored in the actual file. This is where all the code is.

3. What is '\n'?\
This is a newline character. As the name indicates, it adds a newline to the string we are typing. For example,
```
simple_string = "Hello\nthere"
print(simple_string)

Hello
there
```

4. What does Dr. Chuck say is the most common way to treat a file when reading it?\
He says that the most common way to read a file is by a sequence of lines. Basically, we can read the file like a book, going from top to bottom and line after line.

5. In Searching Through a File (fixed) example, Dr. Chuck talks about the problem of the extra newline character that appears when we print out each line. He resolves this problem by using line.rstrip(), invoking Python's built-in rstrip method of strings. Could we also use a slice here, and write line[:-1] instead? Explain your answer.\
Yes, we can. This is because both of these commands will do the same thing, which is removing the newline character. `rstrip()` will remove whitespace, which is the `\n`, and `line[:-1]` will removing the last character of a string, which in this case is `\n`.

6. The second video presents three different ways, or patterns for selecting lines that start with 'From:'. Compare these three patterns, providing examples of each.\
Using `startswith()` first way:
```
fhand = open("file.txt")
for i in fhand:
    i = i.rstrip()
    if not i.startswith("From:"):
        continue
    print(i)
```
This way will tell the computer to loop through each line within the file and if the line doesn't start with "From:", then ignore it and advance to the next variable in the iteration process. If it does start with "From:", then print out the line.

7. A new Python construct is introduced at the end of the second video to deal with the situation when the program attempts to open a file that isn't there. Describe this new construct and the two new keywords that pair to make it.\
This new construct is basically created when the programmer knows that something could go wrong with the program. In this case, the user input could mess up the program. By using `try` and `except` in this scenario, the program will see if the user input will work. If it does, then `except` will be skipped and the program will continue running. If the user input returns an error however, then the code under `except` will run, which is an error message created by the programmer in this case. 

  
