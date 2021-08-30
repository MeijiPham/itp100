### Lesson 13: Network Programming Pt 3

1. What is ASCII? What are its limitations and why do we need to move beyond it?\
It is the latin character set for programming that represents the characters as numbers. Due to it being limited to only the latin character set, this posed problems for other languages such as Russian or Chinese, languages that don't use the latin alphabet. It needed to be improved to unicode in order store more data on different character sets as well as differentiating punctuations such as an apostrophe and single quotes.

2. Which function in Python will give you the numeric value of a character (and thus its order in the list of characters)?\
The `ord()` function can give the numeric value of a character. It takes a character as an argument.

3. Dr. Chuck says we move from a simple character set to a super complex character set. What is this super complex character set called?\
It is called unicode which can hold more complex characters due to the wide range of data it can hold.

4. Describe bytes in Python 3 as presented in the video. Do a little web searching to find out more about Python bytes. Share something interesting that you find.\
In the video, Dr. Chuck says that bytes are sent to external resources like network sockets when we want to interact with it. To do this, we can encode strings into bytes using `encode()`. If we wanted to convert a byte into a string, then we would use `decode()` to decode the byte. 