# Communication on the network 

Communication on a network refers to the exchange of data and information between devices or nodes that are connected to the same network. Networks can be of various types, including local area networks (LANs), wide area networks (WANs), the internet, and more. Effective communication on a network is essential for sharing resources, accessing data, and enabling various applications and services. 


![network.png](images%2Fnetwork.png)

Here are some key aspects of communication on a network:

1. **Devices and Nodes**: Devices connected to a network can include computers, smartphones, servers, routers, switches, and more. Each of these devices has a unique identifier, such as an IP address or a MAC address, which is used to route data to the correct destination.

2. **Protocols**: Network communication relies on communication protocols, which are a set of rules and conventions that govern how data is formatted, transmitted, and received. Examples of network protocols include TCP/IP (Transmission Control Protocol/Internet Protocol), HTTP (Hypertext Transfer Protocol), and FTP (File Transfer Protocol).

3. **Data Transmission**: Data can be transmitted on a network in various ways, including wired (e.g., Ethernet) and wireless (e.g., Wi-Fi) connections. The method of transmission depends on the network type and the devices involved.

4. **Addressing**: To send data from one device to another on a network, the sender needs to know the address of the recipient. In IP-based networks, this is typically the IP address, while in Ethernet-based networks, it's the MAC address.

5. **Data Packets**: Data is divided into smaller packets for transmission across a network. Each packet typically includes the source and destination addresses, as well as the actual data. These packets are then sent individually and reassembled at the destination.

6. **Routing**: In larger networks, data may need to traverse multiple devices (routers, switches) to reach its destination. Routing protocols are used to determine the best path for data to follow, ensuring efficient and reliable communication.

7. **Firewalls and Security**: Networks often incorporate security measures, such as firewalls, to protect against unauthorized access and malicious activity. Encryption protocols (e.g., SSL/TLS) are used to secure data in transit.

8. **Latency and Bandwidth**: Network performance is characterized by factors like latency (delay) and bandwidth (data transfer rate). Low latency is crucial for real-time applications, while high bandwidth is necessary for transferring large amounts of data quickly.

9. **Protocols and Services**: Different network protocols and services are used for specific purposes. For instance, SMTP (Simple Mail Transfer Protocol) is used for sending email, while DNS (Domain Name System) is used for translating domain names into IP addresses.

10. **Internet and the World Wide Web**: The internet is a global network of networks, and the World Wide Web (WWW) is a collection of interconnected web pages and resources accessible via web browsers. HTTP is the protocol used for web communication.

Effective communication on a network is vital for businesses, organizations, and individuals to access information, share resources, and collaborate in a digital age. It's essential to understand the underlying technologies and protocols that enable network communication to ensure its reliability and security.


##  How do systems communicate on a network ?
![comm.jpg](images%2Fcomm.jpg)

### web server and client

A web server and a web client are two fundamental components of the World Wide Web and the HTTP (Hypertext Transfer Protocol) communication system. They work together to enable the retrieval and display of web content, such as web pages, images, videos, and other resources. 

Here's an overview of each:

![web_server_client.png](images%2Fweb_server_client.png)

#### 1.Web Server:

A web server is a computer program or software application that serves as a centralized hub for storing, processing, and delivering web content to clients over the internet.
Its primary functions include:

Accepting incoming HTTP requests from clients (typically web browsers).
Processing these requests by interpreting the requested URL and determining the appropriate action (e.g., serving a specific web page or resource).
Retrieving the requested content from its storage or generating it dynamically (e.g., querying a database or running scripts).
Sending the content back to the requesting client in the form of an HTTP response.


Common web server software includes Apache, Nginx, Microsoft Internet Information Services (IIS), and LiteSpeed, among others.



#### 2.Web Client:

A web client is a software application or user agent that initiates requests to web servers and displays the web content to users. The most common web client is a web browser (e.g., Chrome, Firefox, Safari, Edge), but other applications can also act as web clients (e.g., mobile apps, command-line tools).
The web client's primary functions include:

Constructing HTTP requests, specifying the resource's URL, HTTP method (e.g., GET, POST), and additional headers (e.g., User-Agent, Referer).
Sending the HTTP request to the appropriate web server.
Receiving and processing the HTTP response from the server.
Rendering and displaying the web content to the user, including HTML pages, images, CSS stylesheets, JavaScript code, and multimedia files.


Web clients provide an interface for users to navigate and interact with web applications and websites.



The interaction between a web server and a web client follows a request-response model. When a user clicks a link or enters a URL in a web browser, the browser acts as the web client and sends an HTTP request to the specified web server. The server processes the request, generates an HTTP response, and sends it back to the client. The client then renders the received content for the user to view and interact with.
This client-server architecture is fundamental to the functioning of the World Wide Web and underpins most internet-based applications and services.


##  How do Servers and clients communicate? 

A web client is an application that communicates with a web server, using Hypertext Transfer Protocol (HTTP)
Web servers speak the HTTP protocol, so they are often called HTTP servers. These HTTP servers store the Internet’s data and provide the data when it is requested by HTTP clients.

![com_protocol.png](images%2Fcom_protocol.png)

# HTTP

HTTP is a versatile protocol used for various purposes on the web, including fetching web pages, transmitting data between clients and servers, and communicating with APIs. Understanding how HTTP requests and responses work is fundamental to web development and networking.

It is a protocol used by web browsers and web servers to send and receive data. HTTP requests are made by clients (typically web browsers) to request resources from a web server, and HTTP responses are sent by the web server to fulfill those requests

### HTTP Request:

An HTTP request is sent by a client (e.g., a web browser) to request a resource from a web server. It consists of several components:

#### Request Method: 
Specifies the HTTP method to be used for the request. Common methods include:

* GET: Retrieve data from the server.
* POST: Submit data to be processed by the server.
* PUT: Update a resource on the server.
* DELETE: Remove a resource from the server.

#### URL (Uniform Resource Locator): 
The address of the resource being requested.

![url.png](images%2Furl.png)

#### Headers:
Key-value pairs that provide additional information about the request, such as the user agent, accepted content types, and more.

#### Body (optional): 
Data sent with POST or PUT requests, used for submitting form data or sending JSON data, for example.

![http_req.png](images%2Fhttp_req.png)


### HTTP Response:

An HTTP response is sent by a web server in response to an HTTP request. It contains the requested resource (e.g., a web page or data) and consists of several components:

#### Status Line: 
   Contains the HTTP status code and a brief status message.
   Example: HTTP/1.1 200 OK

#### Headers: 
   Similar to request headers, these provide metadata about the response, such as content type, length, and server information.

#### Body: 
   The actual content of the response, which could be HTML for a web page, JSON data, an image, or any other type of data.
   
![http_resp.png](images%2Fhttp_resp.png)


## Http Handshaking

HTTP (Hypertext Transfer Protocol) handshaking refers to the process by which a client (usually a web browser) and a web server establish a connection and negotiate the parameters for exchanging data. This handshake is crucial for initiating communication between the client and server and ensuring that both parties understand how to exchange information effectively. Here's a simplified overview of the HTTP handshaking process:

1. **Client Request**: The process begins when a client (such as a web browser) sends an HTTP request to a web server. This request typically includes the following information:
   - The HTTP method (e.g., GET, POST, PUT) that specifies the desired action.
   - The Uniform Resource Identifier (URI) or URL that identifies the resource the client wants to access.
   - Headers containing additional information about the request, such as the client's user agent, accepted content types, and cookies.

2. **Server Response**: Upon receiving the request, the web server processes it and generates an HTTP response. The response typically includes:
   - A status code indicating the outcome of the request (e.g., 200 OK, 404 Not Found, 500 Internal Server Error).
   - Headers providing metadata about the response, such as the content type, content length, and server information.
   - The actual content (e.g., HTML, JSON, images) that the client requested.

3. **Client Acknowledgment**: The client receives the server's response and processes it. If the response contains content, the client renders or displays it to the user. The client may also process and store any cookies or other data provided by the server for future interactions.

This basic exchange between client and server represents the core of HTTP handshaking. However, modern web applications often involve more complex interactions, including multiple requests and responses to fetch additional resources (e.g., CSS, JavaScript files, images) and potentially using secure connections (HTTPS) to protect data in transit.

Additionally, the HTTP/1.1 and HTTP/2 protocols have introduced optimizations to reduce latency and improve performance. For example, HTTP/2 allows multiple requests and responses to be multiplexed over a single connection, reducing the need for repeated handshakes.

Overall, HTTP handshaking is a fundamental process in web communication, allowing clients and servers to exchange data and fulfill requests efficiently and securely.


## OSI(Open Systems Interconnection)  Model

The OSI model,  is a reference framework that explains the process of transmitting data between computers. It is divided into seven layers that work together to carry out specialised network functions, allowing for a more systematic approach to networking.


![OSI_model.png](images%2FOSI_model.png)


1. **Physical Layer (Layer 1)**:
   - This is the lowest layer and deals with the physical medium and hardware connections.
   - It defines how data is transmitted over the physical network medium, including specifications for cables, connectors, and electrical signaling.
   - Examples: Ethernet cables, fiber optics, voltage levels, and bit timing.

2. **Data Link Layer (Layer 2)**:
   - This layer is responsible for creating a reliable link between two directly connected nodes on the network.
   - It handles error detection and correction and controls access to the physical medium (media access control or MAC layer).
   - Examples: Ethernet switches, MAC addresses, and frame synchronization.

3. **Network Layer (Layer 3)**:
   - The network layer is responsible for routing packets of data between different networks or subnets.
   - It determines the optimal path for data to travel from the source to the destination.
   - Examples: Routers, IP (Internet Protocol), and routing algorithms.

4. **Transport Layer (Layer 4)**:
   - This layer ensures end-to-end communication and manages data flow between two devices.
   - It handles error detection and recovery and provides mechanisms for reliable data delivery.
   - Examples: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

5. **Session Layer (Layer 5)**:
   - The session layer establishes, manages, and terminates communication sessions between devices.
   - It provides synchronization points in the data stream to allow for orderly data exchange.
   - Examples: NetBIOS, RPC (Remote Procedure Call).

6. **Presentation Layer (Layer 6)**:
   - This layer is responsible for data translation, encryption, and compression.
   - It ensures that data sent from the sender is in a format that the receiver can understand.
   - Examples: SSL/TLS encryption, data compression algorithms.

7. **Application Layer (Layer 7)**:
   - The top layer, which interacts directly with the end-user or application.
   - It provides a platform-independent interface for applications to access network services.
   - Examples: Web browsers, email clients, and file transfer protocols (FTP, HTTP).



#### Which layer does HTTP work on?

HTTP works on the application layer of the Open Systems Interconnection (OSI) model. The application layer is the topmost layer of the OSI model and is responsible for providing services to end-user applications. Other protocols that work on the application layer include FTP, SMTP, and DNS.

The application layer is responsible for a number of tasks, including:

* Identifying and establishing communication between applications
* Providing a common interface for applications to communicate with each other
* Managing the flow of data between applications
* Ensuring the integrity and security of data

HTTP is a request-response protocol, which means that a client application sends a request to a server application, and the server application sends back a response. HTTP requests can be used to retrieve resources from a server, such as HTML pages, images, and CSS files. HTTP requests can also be used to submit data to a server, such as when filling out a web form.


HTTP is a foundational protocol of the World Wide Web and is used by billions of people around the world every day to access and publish information.


[`next`](html_intro.md)