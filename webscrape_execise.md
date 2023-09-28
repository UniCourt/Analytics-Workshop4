
## Exercise 

* Let us scrap the **imdb.com** website 
 
    In “**imdb.com**” website go to menu and select “**Top 250 movies**” .


* Following data needs to be extracted out of the website.

      Movie details
         Movie Name
         Director Name
         Writers Name
         Description 
         Tag Line
 
      Top cast details
         actor name
         character name
  
      Reviews details
         subject
         review
         

* We will first write a simple python script to extract and print the above mentioned data from the website.

* Follow the given steps in order to achieve that.

Step 1 : If django is not installed , install it by using below command : 
		
    pip install django
    sudo apt install python3-django

Step 2: create project using command : 
		
    django-admin startproject webscraper

Step 3 : Create a python file web_scrapper.py in webscraper project,which will include the script to scrap the website 
		
    cd webscraper 
    python3 manage.py startapp scraper

Step 4 : Create file i,e imdb_extractor.py , which will include the script to scrap the website. Write the below script inside that file

    vi imdb_extractor.py

step 5 : Copy the below code to the imdb_extractor.py file.
  
    import requests
    from bs4 import BeautifulSoup, element
    
    
    def start_extraction():
      print("Extraction started")
  
        #  url to the top 250 movies page
        url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    
        #  headers to the top 250 movies page
        header_dict = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'referer': 'https://www.imdb.com/search/title/?genres=Film-Noir&explore=genres&title_type=movie&ref_=ft_movie_10',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }
    
        #  hitting url with proper headers
        top250_movies_data = requests.get(url, headers=header_dict)
        #  creating soup using beautifulsoup to extract data
        soup = BeautifulSoup(top250_movies_data.text, 'html.parser')
    
        #  get all movies div. type of "movies" will be <class 'bs4.element.ResultSet'>
        movies_div = soup.findAll('div',
                                  class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b51a3d33-7 huNpFl cli-title')
    
        movies_link: list = []
        #  get all the movie links and store in list
        for div_tag in movies_div:
            movies_link.append(div_tag.a['href'])
    
        #  using movies_link list hit the all movies details page and get the required(name and director) from the page
        for movie in movies_link[:10]:
            url = f'https://www.imdb.com/{movie}'
            movie_data = requests.get(url, headers=header_dict)
            movie_soup = BeautifulSoup(movie_data.text, 'html.parser')
    
            #  extracting the data using soup
            movie_name = movie_soup.find('h1').text
            director = movie_soup.find('a',
                                       class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text
    
            #  print the data
            print("Movie Name: ", movie_name)
            print("Director: ", director)
    
            print("\n------------------------------------------------------------------\n")


    if __name__ == "__main__":
        start_extraction()


Step 6 . In order to run this script we need a few python packages running in our environment. So we will add it in the dockerfile. Open the folder dockerfile and edit the file named Dockerfile. You can copy the below content and paste it in Dockerfile.
   
command to create a Dockerfile:         
    
    vi Dockerfile

Code to copy into DockerFile

    FROM python:3.9-alpine3.15
    WORKDIR /workspace/site
    
    RUN apk update && \
    apk --no-cache add --virtual build-deps-alpine build-base && \
    apk --no-cache add --virtual postgresql-deps libpq-dev
    # Install requirements
    RUN pip install --upgrade pip
    RUN pip install Django psycopg2==2.9.3 bs4 html5lib requests
    
    COPY . /workspace/site


Step 7 . Create a docker-compose.yml file , which will have 2 container one for webapp and other one for Postgres DB

Command to create docker compose file : 
      
    vi docker-compose.yaml

Paste the below code in the file :

    version: '3.3'
    services:
      webscrape_db:
        container_name: "webscraper_db"
        image: postgres:14-alpine
        restart: always
        environment:
          POSTGRES_DB: webscraper
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB_PORT: 5432
        volumes:
          - .:/code
          - db:/var/lib/postgresql/data
        stdin_open: true
        ports:
          - "8012:5432"
    
    
      webscrape:
        build:
          context: ./
          dockerfile: ./Dockerfile
        image: webscraper
        environment:
          - IS_LOCAL=True
          - db_name=movies_db
          - user=postgres
          - password=postgres
          - port=5432
          - host=webscrape_db
        container_name: webscraper_app
        expose:
        - "8010"
        ports:
        - "8010:8000"
        volumes:
          - .:/workspace/site
        command: sh -c "python manage.py runserver 0:8010"
        stdin_open: true
        tty: true
        depends_on:
          - webscrape_db
    volumes:
      db:


Step 8 : Once the docker file and docker compose file is updated, Run the below command in the directory where your docker-compose.yml is present to bring containers up
    
    docker-compose up --build -d


Step 9  : Once the docker compose file ran successfully , then run below command , which will give information about the containers, such as their Container ID, Image, Command, Created time, Status, Ports, and Names.
	
    docker ps


Step 10 : Now exec into the webscraper_app container.

    docker exec -it webscraper_app sh


Step 11: Run the below command to run the python script.

    python3  imdb_extractor.py 


Now you should be able to see the extracted data printed on your screen.

[`Next`](webscrape_store_data.md)