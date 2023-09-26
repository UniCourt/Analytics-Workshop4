## Beautiful Soup - Navigating by Tags

Navigating by tags is a fundamental aspect of using Beautiful Soup. You can use various methods to navigate and manipulate the elements of an HTML or XML document based on their tags.

we shall discuss about Navigating by Tags.

Here's an example of how to navigate by tags using Beautiful Soup:


Let's assume you have an HTML document like this:

    <html>
      <head>
        <title>Sample HTML Document</title>
      </head>
      <body>
        <div id="content">
          <h1>Welcome to Beautiful Soup</h1>
          <p>This is a sample HTML document.</p>
          <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
          </ul>
        </div>
      </body>
    </html>


Now, let's use Beautiful Soup to navigate and extract information from this HTML document:

    from bs4 import BeautifulSoup
    
    # Define the HTML document as a string
    html_doc = """
    <html>
      <head>
        <title>Sample HTML Document</title>
      </head>
      <body>
        <div id="content">
          <h1>Welcome to Beautiful Soup</h1>
          <p>This is a sample HTML document.</p>
          <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
          </ul>
        </div>
      </body>
    </html>
    """
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    # Navigate to the title tag and print its text
    title_tag = soup.title
    print("Title:", title_tag.text)
    
    # Navigate to the div with id="content"
    content_div = soup.find('div', id='content')
    
    # Navigate to the h1 tag inside the div and print its text
    h1_tag = content_div.find('h1')
    print("Heading:", h1_tag.text)
    
    # Navigate to the ul tag and iterate through its li elements
    ul_tag = content_div.find('ul')
    print("List Items:")
    for li_tag in ul_tag.find_all('li'):
        print(li_tag.text)


In this example:

We create a BeautifulSoup object and specify the parser ('html.parser').

We navigate to the title tag using soup.title and print its text.

We find the <div> element with id="content" using soup.find(). Then, within this div, we navigate to the h1 tag and print its text.

We find the <ul> tag within the content_div and iterate through its <li> elements to print each list item's text.


[`next`](webscrape_beautifulsoup3.md)