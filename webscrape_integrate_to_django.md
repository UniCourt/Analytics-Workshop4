# Integrate the Script with Django Admin.

* Let us view the scraped data in the Django-admin. Follow the below steps to achieve that.


Step 1. Open the admin.py file which is present in the same path as that of models.py. Currently it will include the Student model.
	
    vi admin.py

Step 2. Add the below class to admin.py

    from django.contrib import admin
    from .models import Movies,Reviews,TopCast
    
    
    # Register your models here.
    class MovieAdmin(admin.ModelAdmin):
        list_display = ("movie_name", "director_name", "writers_name", "description", "tagline",'created_date')
        list_filter = ("movie_name",)
    
    
    class TopCastAdmin(admin.ModelAdmin):
        list_display = ('movie_name', 'actor_name', 'character_name')
        list_filter = ("movie_name",)
    
    
    class ReviewAdmin(admin.ModelAdmin):
        list_display = ('movie_name', 'subject', 'reviews')
    
Step 3. Register all models in the admin.py 
   
    admin.site.register(Movies, MovieAdmin)
    admin.site.register(TopCast, TopCastAdmin)
    admin.site.register(Reviews, ReviewAdmin)


After modifying the admin.py file will look like this

    from django.contrib import admin
    from .models import Movies,Reviews,TopCast
    
    
    # Register your models here.
    class MovieAdmin(admin.ModelAdmin):
        list_display = ("movie_name", "director_name", "writers_name", "description", "tagline",'created_date')
        list_filter = ("movie_name",)
    
    
    class TopCastAdmin(admin.ModelAdmin):
        list_display = ('movie_name', 'actor_name', 'character_name')
        list_filter = ("movie_name",)
    
    
    class ReviewAdmin(admin.ModelAdmin):
        list_display = ('movie_name', 'subject', 'reviews')
    
    
    admin.site.register(Movies, MovieAdmin)
    admin.site.register(TopCast, TopCastAdmin)
    admin.site.register(Reviews, ReviewAdmin)


Step 4. In order to view the data in the admin, let us run the server. For that go to the tab where webscraper_app is running and run the below command

    python manage.py runserver 0:8010

Step 5. Now open the webpage and check if you can view the data

    http://0.0.0.0:8010/admin/

Step 6. To login into django-admin create a superuser using below steps :   
    
In the webapp container run the command :

    python manage.py createsuperuser --username admin    

give below inputs on successfully run of above command.
Email address (press enter)
Password : admin123
Password(again) : admin123


Now add the credentials in the django-admin page and refresh.

Now you will be able to see all the scraped data from the Postgres DB

Step 7. Open the apps.py file present in the same path where admin.py and models.py is present. And copy below code (same imdb_extractor.py script) Do not delete the existing contents and this is how it will look,

    from django.apps import AppConfig
    
    
    class ScraperConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'scraper'
    
    
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
    
    # This will create the connection the to Postgres database.
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
        movies_div = soup.findAll('div',
                                    class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b51a3d33-7 huNpFl cli-title')
    
        movies_link: list = []
        #  get all the movie links and store in list
        for div_tag in movies_div:
            movies_link.append(div_tag.a['href'])
    
        #  using movies_link list hit the all movies details page and get the required(name and director) from the page
        for movie in movies_link[:2]:
    
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


Step 8. Now let us modify the views.py file to include the view to scrap the data. Open the views.py file present inside the same folder as that of models.py and add the below function at the bottom of the file (Do not delete the existing contents)

    from django.http import JsonResponse
    from . import apps
    
    # Create your views here.
    def python_movie_scrap(request):
    
    apps.start_extraction()
    return JsonResponse({'status': 'success', "message" : "Extracted and populated the table."}, status=200)


Step 9.  Add below code in webscraper/urls.py , which will register path 

    path('scraper/', include('scraper.urls')),

webscraper/urls.py  file will look like,

    from django.contrib import admin
    from django.urls import path,include
    
    urlpatterns = [
        path('scraper/', include('scraper.urls')),
        path('admin/', admin.site.urls),
    ]


Step 10. And also add a url path to scraper/urls.py file
    
    path('start_python_movie_scraping', views.python_movie_scrap)

scraper/urls.py file will look like,

    from django.urls import path
    from . import views
    
    urlpatterns = [

    path('start_python_movie_scraping', views.python_movie_scrap)
         ]


Step 11. Now let us run this view. Make sure your server is running in webscraper_app. If not, run the server

    python manage.py runserver 0:8010

Now copy the below url in webpage.

    http://0.0.0.0:8010/scraper/start_python_movie_scraping


If your script ran fine, you should get a message in the browser

    {
        "status": "sucess",
        "message": "Extracted and populated the table."
    }

To verify if the extractions had happened fine, you may open the admin page and check the data.

    http://0.0.0.0:8010/admin/

Check for the created_date of the entries in the table. If the script ran fine, the entries will have the latest date as created_Date

[Next](python_debug.md)