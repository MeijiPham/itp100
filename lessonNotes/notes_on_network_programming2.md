### Lesson 13: Network Programming Pt 2

1. What is an application protocol? List examples of specific application protocols listed in the lecture. Can you think of one besides HTTP that we have been using in our class regularly since the beginning of the year?\
An application protocol is how different applications, like servers, running on two different systems communicate with each other by following set of rules. Some examples are HTTP and WWW. This year, we have been using the ICT application protocol.

2. Name the three parts of a URL. What does each part specify?\
The 3 parts include the protocol, the host, and the document. The protocol specifies the application protocol that is being used. The host identifies the name of the host that is holding the resource. The document specifies the document within the host that the user wants to grab ahold of.

3. What is the request/response cycle? What example does Dr. Chuck use to illustrate it and describe how it works?\
The cycle is basically how you can access a URL. When a user clicks on a link, it will send a request to that web server. The web server will then run its code and send a response back to you, like another web page. Dr. Chuck illustrated the cycle with two web browsers. On one web browser, it has a link to another browser. Once the link is clicked on, the first browser will send a request to the server. The server will then read the code of the second browser and send a response back. In this case, the response is a web page that allows the user to go back to the first page.

4. What is the IETF? What is an RFC?\
The IETF is the Internet Engineering Task Force. It provides the standard for all internet protocols. These standards are called RFC, which stands for Request for Comments. It is a publication written by engineers and computer scientists that can be reviewed by others. Through evaluation, this can improve the internet and develop it further. 

5. In the video titled Worked Example: Sockets, Dr. Chuck tells us where to download a large collection of sample programs he has available associated with the course. Where do we find these examples?\
We can find this under "materials" in the Python for Everybody website. There is a link to download all the sample files.

6. Try the telnet example that Dr. Chuck shows us in the Worked Example: Sockets video. Can you retrieve the document using telnet? (NOTE: examples in the previous videos no longer work. I suspect this is because HTTP/1.0 is no longer supported by the webserver).\
Yes, I did.
