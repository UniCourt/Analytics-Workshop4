## Status code:

When you perform web scraping or make HTTP requests to websites, the server responds with an HTTP status code, which indicates the outcome of the request. These status codes provide information about whether the request was successful, encountered an error, or requires further action. 

Here are some of the common HTTP status codes you might encounter while scraping a website:

1. 200 OK: This status code indicates that the request was successful, and the server has returned the requested content. It's the standard response for successful HTTP requests.


2. 400 Bad Request: This code is returned when the server cannot understand or process the client's request due to malformed syntax or invalid parameters.


3. 401 Unauthorized: It means that the request lacks valid authentication credentials or the provided credentials are invalid. Typically, you need to provide proper authentication to access the resource.


4. 403 Forbidden: This status code indicates that the server has understood the request, but it refuses to fulfill it. You may not have the necessary permissions to access the resource.


5. 404 Not Found: This code signifies that the requested resource does not exist on the server. It's a common error when you try to access a page or resource that is not available.


6. 429 Too Many Requests: This status code is used when the client has exceeded the rate limits set by the server. It's often encountered when web scraping too aggressively, and it's a signal to slow down the requests.


7. 500 Internal Server Error: This code indicates that there was an unexpected error on the server's side, and the request could not be fulfilled. It's a generic server error.


8. 503 Service Unavailable: This status code indicates that the server is temporarily unable to handle the request, possibly due to maintenance or overload. It's a temporary error.


9. 504 Gateway Timeout: This code occurs when a server acting as a gateway or proxy did not receive a timely response from the upstream server or endpoint.


These are just a few of the common HTTP status codes you might encounter while scraping a website. It's essential to handle these status codes appropriately in your web scraping code to ensure robustness and graceful error handling. You can use conditional statements to handle different status codes and take appropriate actions, such as retrying requests, logging errors, or skipping problematic URLs.


![status_code.png](images%2Fstatus_code.png)



[`next`](webscrape_intro_beautifulsoup.md)