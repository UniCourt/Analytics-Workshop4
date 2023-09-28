# Web Scrapping Using Python

## Introduction


Web scraping is the process of extracting data from websites and store it in database as structured data. It is a subset of data mining, It's a valuable skill in the world of data analysis, research, and automation. Python is a popular language for web scraping due to its rich ecosystem of libraries and tools. In this introduction, I'll outline the basics of web scraping using Python.

![webscrape.png](images%2Fwebscrape.png)


### Importance of Web Scraping

* Market research: Web scraping can be used to collect data on competitors, product trends, and customer sentiment. This data can be used to make informed business decisions about pricing, marketing, and product development.
* Lead generation: Web scraping can be used to collect contact information from potential customers. This information can be used to create targeted sales and marketing campaigns.
* Price monitoring: Web scraping can be used to track the prices of products and services on different websites. This information can be used to find the best deals and to ensure that prices are competitive.
* Content aggregation: Web scraping can be used to collect content from different websites and to aggregate it into a single location. This can be used to create news feeds, product directories, and other types of websites.
* Machine learning: Web scraped data can be used to train machine learning models. These models can be used for a variety of tasks, such as product recommendation, fraud detection, and sentiment analysis.


Example:

Website : https://www.worldometers.info/coronavirus/


![covid_stats.png](images%2Fcovid_stats.png)

Structured Covid19 Stats

![structured_covid19_stats.png](images%2Fstructured_covid19_stats.png)



### Prerequisites:
* Python installed
* Code editor (e.g., Visual Studio Code, PyCharm)
* Python libraries (`requests` and `BeautifulSoup`)

### What is Requests?
The `requests` library in Python is a popular and versatile library used for making HTTP requests to interact with web services, retrieve data from websites, or interact with APIs (Application Programming Interfaces). It simplifies the process of sending HTTP requests and handling responses, making it a valuable tool for tasks like web scraping, data retrieval, and web service integration.

Key features and functionalities of the `requests` library include:

1. HTTP (Hypertext Transfer Protocol) Methods: `requests` supports various HTTP methods, such as GET, POST, PUT, DELETE, and more, allowing you to perform different types of requests based on your needs.
    
    GET: Retrieve data from the server.

    Example:

            import requests
            response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
            print(response.text)

    POST: Submit data to the server to create a new resource.

    Example: 
            
            import requests
            import json
            
            data = {'title': 'foo', 'body': 'bar', 'userId': 1}
            headers = {'Content-type': 'application/json; charset=UTF-8'}
            
            response = requests.post('https://jsonplaceholder.typicode.com/posts', data=json.dumps(data), headers=headers)
            print(response.text)

    
2. URL  (Uniform Resource Locator) Handling: It provides a straightforward way to construct URLs and handle query parameters and path components.

    Example:
            
            
            import requests
            url = "https://www.example.com/api/protected_resource"
            headers = {"Authorization": "Bearer your_access_token"}
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                print("Request was successful!")
                print(response.text)
            else:
                print(f"Request failed with status code: {response.status_code}")


3. Headers:  You can easily add custom headers to your requests, which is useful when working with APIs that require specific authentication or request headers.

   Example:
            
         import requests

         # Define custom headers as a dictionary
         headers = {
             'User-Agent': 'My Python App',
             'Authorization': 'Bearer your_access_token',
             'Content-Type': 'application/json',
         }
         
         # URL to send the GET request
         url = 'https://api.example.com/resource'
         
         # Send a GET request with custom headers
         response = requests.get(url, headers=headers)
         
         # Check the response status code
         if response.status_code == 200:
             print('Request was successful!')
             print('Response content:', response.text)
         else:
             print(f'Request failed with status code: {response.status_code}')


4. Session Management: `requests` supports session objects that allow you to persist certain parameters across multiple requests, such as cookies and authentication credentials.

      Example:
               
         import requests

         # Create a session object
         session = requests.Session()
         
         # Define custom headers if needed
         headers = {
             'User-Agent': 'My Python App',
             'Authorization': 'Bearer your_access_token',
             'Content-Type': 'application/json',
         }
         
         # Optional: Set headers that will be included in all requests made with this session
         session.headers.update(headers)
         
         # Define a URL for the login page (replace with your login URL)
         login_url = 'https://example.com/login'
         
         # Create a dictionary with login credentials
         login_data = {
             'username': 'your_username',
             'password': 'your_password',
         }
         
         # Perform a POST request to log in
         login_response = session.post(login_url, data=login_data)
         
         # Check if the login was successful
         if login_response.status_code == 200:
             print('Login successful!')
         else:
             print(f'Login failed with status code: {login_response.status_code}')
             exit()  # Exit if the login failed
         
         # Now, you can use the same session for subsequent requests, and it will maintain the session state, including cookies
         
         # Example: Make a GET request to an authenticated resource
         resource_url = 'https://example.com/protected_resource'
         resource_response = session.get(resource_url)
         
         if resource_response.status_code == 200:
             print('Request to protected resource was successful!')
             print('Response content:', resource_response.text)
         else:
             print(f'Request to protected resource failed with status code: {resource_response.status_code}')
         
         # Don't forget to close the session when done
         session.close()


5. Response Handling: You can access and manipulate the response data, including status codes, headers, and content, with ease.

      Example:

            import requests

            # Define the URL you want to make a GET request to
            url = 'https://jsonplaceholder.typicode.com/posts/1'
            
            # Send a GET request to the URL
            response = requests.get(url)
            
            # Check the response status code
            if response.status_code == 200:
                print('Request was successful!')
            
                # Access response headers
                headers = response.headers
                print('Response Headers:')
                for header, value in headers.items():
                    print(f'{header}: {value}')
            
                # Access and print response content
                content = response.text
                print('Response Content:')
                print(content)
            
                # You can also access the response JSON content (if applicable)
                json_data = response.json()
                print('Response JSON Data:')
                print(json_data)
            
            else:
                print(f'Request failed with status code: {response.status_code}')


The `requests` library is widely used in web development, data science, and web scraping due to its simplicity and reliability. It is typically installed using pip with the following command:

```
pip install requests
```

Once installed, you can easily incorporate it into your Python projects to interact with web services and retrieve data from the web.




[`Next`](webscrape_intro_status_code.md)