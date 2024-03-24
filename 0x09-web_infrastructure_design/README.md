# One Server Web Infrastructure

This project outlines a simple web infrastructure composed of a single server, hosting a website reachable via www.foobar.com.

## Components

- **Server**: A single server with IP address 8.8.8.8.
- **Web Server**: Nginx, which listens for incoming client requests and sends back the appropriate response.
- **Application Server**: Processes requests received from the web server, performs the necessary computations, and sends the response back to the web server.
- **Application Files**: The codebase required for the application to function.
- **Database**: MySQL, used to store, retrieve, and manipulate data.
- **Domain Name**: foobar.com, configured with a 'www' A record that points to the server IP 8.8.8.8.

## How It Works

1. A user types www.foobar.com into their web browser, which sends a request over the internet.
2. The request reaches the server with IP address 8.8.8.8.
3. The Nginx web server receives the request and forwards it to the application server.
4. The application server processes the request using the application files and queries the MySQL database if necessary.
5. The application server sends the response back to the Nginx web server.
6. The Nginx web server sends the response back to the user's web browser over the internet.

## Potential Issues

- **Single Point of Failure (SPOF)**: The entire website becomes unavailable if the server goes down.
- **Downtime During Maintenance**: The website experiences downtime whenever maintenance tasks, such as deploying new code or updating the server, are performed.
- **Cannot Scale If Too Much Incoming Traffic**: The single server may not be able to handle a sudden surge in traffic, leading to slower response times or even server crashes.


