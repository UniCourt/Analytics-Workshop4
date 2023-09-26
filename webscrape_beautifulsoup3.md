Beautiful Soup provides several methods for parsing and navigating HTML or XML documents. Here are some commonly used methods along with examples for each:

1. find() and find_all(): These methods are used to locate and extract specific elements from the document.

        from bs4 import BeautifulSoup
        
        # Sample HTML
        html_doc = """
        <html>
          <body>
            <p class="first">This is the first paragraph.</p>
            <p class="second">This is the second paragraph.</p>
            <p class="first">This is another first paragraph.</p>
          </body>
        </html>
        """
        
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Find the first <p> tag with class "first"
        first_p = soup.find('p', class_='first')
        print(first_p.text)
        
        # Find all <p> tags with class "first"
        all_first_p = soup.find_all('p', class_='first')
        for p in all_first_p:
            print(p.text)

2. select(): This method allows you to use CSS selectors to find elements.


    Using select to find elements with class "second"
    second_p = soup.select('p.second')
    print(second_p[0].text)

3. parent and parents: These attributes allow you to navigate to the parent element(s) of an element.


    second_p = soup.find('p', class_='second')
    parent_div = second_p.parent
    print(parent_div.name)  # Output: 'body'
    
    Navigate through multiple parents
    grandparent = parent_div.parent
    print(grandparent.name)  

    Output: 'html'

4. next_sibling and previous_sibling: These attributes allow you to navigate to the next and previous siblings of an element.


    second_p = soup.find('p', class_='second')
    next_p = second_p.next_sibling
    print(next_p.text)  

    Output: 'This is another first paragraph.'

5. contents: This attribute returns a list of an element's child nodes.


    body = soup.body
    child_nodes = body.contents
    for node in child_nodes:
        if node.name:
            print(node.name)  
    Output: 'p'

  
 
6. string: This attribute retrieves the text within an element.


    first_p = soup.find('p', class_='first')
    text = first_p.string
    print(text)  

    Output: 'This is the first paragraph.'



7. get(): This method retrieves the value of an attribute.
    
       a_tag = soup.find('a')
       href = a_tag.get('href')
       print(href)  

       Output: 'https://example.com'


[`next`](webscrape_intro_steps.md)