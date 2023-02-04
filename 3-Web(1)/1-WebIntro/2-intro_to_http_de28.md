# An Introduction to HTTP

- HTTP (Hypertext Transfer Protocol) is the primary communications protocol between different computers that live on a network.
- These computers could be your personal PC with a web browser, or web servers with website and data.
- HTTP is the protocol that enables the working of the World Wide Web.

## HTTP Requests and Response

- It works with a Request-Response protocol between server and the client.
  - HTTP requests are messages sent by the client to the server (e.g. for requesting resources or performing some operation) and the server responds to this request.
  - HTTP responses are messages sent by the server to the client, as a reply to its request message. Typically the response will be in HTML, XML (eXtensible Markup Language) or JSON (JavaScript Object Notation).

## Types of HTTP Requests

- GET: used to request data from a resource
- POST: used to send data to a server
- PUT: same as POST request, except that PUT is idempotent
- DELETE: used to delete data from a server

> Side note on idempotency: Idempotent means the same action has the same result
>
> - Multiple POST requests to create a resource will result in multiple copies of the resource.
> - Multiple PUT request to create a resource will only create a single resource.

CRUD refers to the major operations that are necessary to support persistent data storage i.e. databases.

- (C)reate - POST (/PUT)
- (R)ead - GET
- (U)pdate - PUT (/POST)
- (D)elete - DELETE

As you can see, HTTP request methods are CRUD compliant, so HTTP can be used to maintain a database.

There are many [methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), but these 4 are the main ones.

## Types of HTTP Response Codes

- 200s: Everything went okay
- 300s: Redirection
- 400s: Client side error (bad request) e.g. 404 error: page not found
- 500s: Server side error

For a comprehensive list of HTTP response codes, see this [wikipedia article](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).
