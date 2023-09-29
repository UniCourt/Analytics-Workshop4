
# Save the scraped data to Postgres Database

* Now let us save the data that we have extracted into a postgres database.
* Let us create new database i,e movies_db in webscraper_db container  
* Follow the below step to create the database.

step 1. Open a new tab in your terminal and exec into the webscraper_db container. Since you have run the docker-compose up command before, both webscraper_app and webscraper_db containers should be up. So we need not bring the container up. We can directly run the below command to exec into the container

    docker exec -it webscraper_db sh


Please note that webscraper_app and webscraper_db are the container_name that you have mentioned in the docker-compose.yml file. If the names you have specified are different, use that.

step 2. Now run the below commands to login to psql.
        
    psql -U postgres

step 3. Now create the database by running below command.

    CREATE DATABASE movies_db;


Since the database is ready, let us create the required tables and columns to that database using the Django models. Keep the database container running in this tab and you may continue the development in a new tab.


Follow the below steps:

step 1. Open the models.py file which is present in the members folder.

File path : webscraper/scraper/models.py

Command :

        vi models.py 

step 2. Currently we do not have anything in this file. Let us add one model called Movie into the file. For that copy the below code to that file

        from django.db import models
        # Create your models here.
        class Movies(models.Model):
            movie_name = models.CharField(max_length=200)
            director_name = models.CharField(max_length=200)
            writers_name = models.CharField(max_length=250)
            description = models.TextField
            tagline = models.CharField(max_length=350)
            created_date = models.TimeField()


            def __str__(self):
                return self.movie_name


            class Meta:
                unique_together = (('movie_name'),)

Also create 2 more models that are Review model and TopCast model and add it here. Copy the code below to the same file.

        class Reviews(models.Model):
            movie_name = models.CharField(max_length=200)
            subject = models.TextField()
            reviews = models.CharField(max_length=350)

            def __str__(self):
                return self.movie_name


        class TopCast(models.Model):
            movie_name = models.CharField(max_length=200)
            actor_name = models.CharField(max_length=200)
            character_name = models.CharField(max_length=200)

            def __str__(self):
                return self.movie_name

Each class represents a model which will in turn represent a table in the database and each property of that class refers to each column in that table.


step 3.  Let us alter  database  settings in settings.py

Path : webscraper/webscraper/settings.py

Code : 

Remove the existing Database settings i,e 
            
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

and add the below code 

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'movies_db',  # Or path to database file1 if using sqlite3.
            'USER': 'postgres',  # Not used with sqlite3.
            'PASSWORD': 'postgres',  # Not used with sqlite3.
            'HOST': 'webscrape_db',  # Set to empty string for localhost.
            # Not used with sqlite3.
            'PORT': '5432',
            # Set to empty string for default. Not used with sqlite3.
        }
    }

And also add 'scraper.apps.ScraperConfig' to INSTALLED_APPS list in settings.py
And add the below in the same file 

    ‘ALLOWED_HOSTS = ['*', ]’ 


step 4. Let us run makemigrations to create the database table using the models. For that first open the tab where webscraper_app is running. If it is not running anywhere, open a new tab and run the below command to run the container

    docker exec -it webscraper_app sh

Once you get inside webscraper_app, run the below commands

    python manage.py makemigrations
 	python manage.py migrate


step 5. Now go to the webscraper_db (database container) and run below commands to ensure that the new table members_blog is created.

    postgres=# \c movies_db
 	You are now connected to the database "movies_db" as user "postgres".
 	member_db=# \dt

* The above command should list down all the tables in the movies_db and there should be scraper_movies,scraper_reviews and scraper_topcast present.
    
        \d scraper_movies
  
This command should describe the scarper_movies table and show all the columns present.


step 5. Now let us modify our script so that it will start saving the extracted data into the created table.

Open the imdb_extractor.py file present in the webscraper folder and replace the script with the one given below.

code:

    import re
    
    import psycopg2
    import requests
    from bs4 import BeautifulSoup, element

    # For the credentials mentioned below, you may refer the docker-compose.yml present in myworld .
    db_name = 'movies_db'
    db_user = 'postgres'
    db_pass = 'postgres'
    db_host = 'webscrape_db'
    db_port = '5432'

    # This will create the connection the to postgres database.
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)
    
    
    def add_row_to_movies(movie_name, director_name, writers_name, description, tagline):
        # This function will add the entry to database
        sql = """INSERT INTO scraper_movies (movie_name, director_name, writers_name, description,tagline, created_date) VALUES (%s, %s, %s, %s, %s, NOW())"""
    
        with conn:
            with conn.cursor() as curs:
                curs.execute(sql, (movie_name, director_name, writers_name, description, tagline))
    
    
    def add_row_to_top_cast(movie_name, actor_name,character_name):
        # This function will add the entry to database
        sql = """INSERT INTO scraper_topcast (movie_name, actor_name,character_name) VALUES (%s, %s, %s)"""
    
        with conn:
            with conn.cursor() as curs:
                curs.execute(sql, (movie_name, actor_name, character_name))
    
    
    def add_row_to_reviews(movie_name, reviews,subject):
        # This function will add the entry to database
        sql = """INSERT INTO scraper_reviews (movie_name, reviews,subject) VALUES (%s, %s, %s)"""
    
        with conn:
            with conn.cursor() as curs:
                curs.execute(sql, (movie_name, reviews, subject))
    
    
    def truncate_table():
        # This function will delete the existing entries from the database.
        with conn:
            with conn.cursor() as curs:
                curs.execute("TRUNCATE scraper_movies CASCADE;")
                curs.execute("TRUNCATE scraper_topcast CASCADE;")
                curs.execute("TRUNCATE scraper_reviews CASCADE;")
    
    
    def start_extraction():
        print("Extraction started")
    
        # Each time when we add new entry we delete the existing entries.
        truncate_table()
    
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
        movie_links = soup.findAll('a', class_="ipc-title-link-wrapper")
    
        movie_link_list: list = []
        #  get all the movie links and store in list
        for movie_link in movie_links:
            if 'href' in movie_link.attrs and re.search(r'title', movie_link['href']):
                movie_link_list.append(movie_link['href'])
    
        #  using movies_link list hit the all movies details page and get the required(name and director) from the page
        for movie in movie_link_list[:10]:
            url = f'https://www.imdb.com/{movie}'
            movie_data = requests.get(url, headers=header_dict)
            movie_soup = BeautifulSoup(movie_data.text, 'html.parser')
    
            #  extracting the data using soup
            movie_name = movie_soup.find('h1').text
            data_list = movie_soup.findAll('a',
                                           class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
            director_name_list = []
            writers_name_list = []
            for data in data_list:
                if re.search(r'_dr$', data['href']) and data.text not in director_name_list:
                    director_name_list.append(data.text)
                elif re.search(r'_wr$', data['href']) and data.text not in writers_name_list:
                    writers_name_list.append(data.text)
    
    
    
            director_name = ','.join(director_name_list)
            writers_name = ','.join(writers_name_list)
            description = ''
            tagline = ''
    
            # Inserting data into database
            add_row_to_movies(movie_name, director_name, writers_name, description, tagline)
    
            # ----------------------------------------Top cast details-----------------------------------------------------
    
            character_name_list = []
            character_list = movie_soup.findAll("li", class_='ipc-inline-list__item', role='presentation')
    
            for character_name in character_list:
                if character_name.a and re.search(r'/characters/', character_name.a['href']):
                    character_name_list.append(character_name.a.text)
    
            topcast_name_list = []
            topcast_list = movie_soup.findAll("a", class_="sc-bfec09a1-1 fUguci")
    
            for topcast_name in topcast_list:
                if re.search(r'/name/', topcast_name['href']):
                    topcast_name_list.append(topcast_name.text)
    
            if len(topcast_name_list) == len(character_name_list):
                for i in range(len(topcast_name_list)):
                    add_row_to_top_cast(movie_name, topcast_name_list[i],character_name_list[i])
    
    
            # # ---------------------------------------review details---------------------------------------------------
            review_url_id = re.search(r'/title/(?P<id>.+?)/', movie).group('id')
            review_url = f'https://www.imdb.com/title/{review_url_id}/reviews?ref_=tt_urv'
            review_data = requests.get(review_url)
            review_soup = BeautifulSoup(review_data.text, 'html.parser')
    
            subject_list = review_soup.findAll("a", class_="title")
            review_list = review_soup.findAll('div', class_="text show-more__control")
    
            subject_data_list = []
            review_data_list = []
            for subject in subject_list:
                subject_data_list.append(subject.text)
    
            for review in review_list:
                review_data_list.append(review.text)
    
            for i in range(2):
                pagination_key = review_soup.find('div', class_='load-more-data').get('data-key')
                load_more_url = f'https://www.imdb.com/title/{review_url_id}/reviews/_ajax?ref_=undefined&paginationKey={pagination_key}'
                review_data = requests.get(load_more_url)
                review_soup = BeautifulSoup(review_data.text, 'html.parser')
    
                subject_list = review_soup.findAll("a", class_="title")
                review_list = review_soup.findAll('div', class_="text show-more__control")
    
                for subject in subject_list:
                    subject_data_list.append(subject.text)
    
                for review in review_list:
                    review_data_list.append(review.text)
    
            if len(subject_data_list) == len(review_data_list):
                for i in range(len(subject_data_list)):
                    add_row_to_reviews(movie_name, subject_data_list[i], review_data_list[i])
    
            print(f"Movie {movie_name} is added successfully\n")
    
    
    if __name__ == "__main__":
        start_extraction()


step 6. Now go to webscraper_app container and run the script
	
    python3 imdb_extractor.py

Once the script run completes, go to the database container and run the below sql query to check if the data is populated or not.
		
    select * from scraper_movies;
    select * from scraper_reviews;
    select * from scraper_topcast;

