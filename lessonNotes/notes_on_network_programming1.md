### Lesson 13: Network Programming

1. Dr. Chuck mentions the architecture that runs our network. What is the name of this architecture?\
He calls it the Transport Control Protocol (TCP) architecture.

2. Take a close look at the slide labelled Stack Connections. Which layer does Dr. Chuck say we will be looking at, assuming that one end of this layer can make a phone call to the corresponding layer on the other end? What are the names of the two lower level layers that we will be abstracting away?\
We will be focusing on the transport layer. The two lower level layers that we're going to be ignoring for right now include the internet and link.

3. We will be assuming that there is a ____________ that goes from point A to point B. There is a ______________ running at each end of the connection. Fill in the blanks.\
We will be assuming that there is a pipe that goes from point A to point B. There is a process running at each end of the connection.

4. Define Internet socket as discussed in the video.\
An Internet socket is the connection between two servers that's established when a server at one end makes a request to another server at the other end. Dr. Chuck compares this to a phone call. The socket would be the call itself that's connecting the phones on each end.

5. Define TCP port as discussed in the video.\
TCP ports are numbers assigned to a user and a server in an IP network. Port numbers basically identify the server application that the user is using. For example, port number 80 is directed to a web server and 25 is directed to incoming emails. On some occasions, a port number will be included in the url if the server is running on an unusual port.

6. At which network layer do sockets exist?\
Sockets exist at the transport layer.

7. Which network protocol is used by the World Wide Web? At which network layer does it operate?\
HTTP is used by the World Wide Web. It operates in the application layer.
