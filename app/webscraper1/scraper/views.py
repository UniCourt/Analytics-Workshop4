from django.http import JsonResponse
from . import apps

# Create your views here.
def python_movie_scrap(request):

   apps.start_extraction()
   return JsonResponse({'status': 'success', "message" : "Extracted and populated the table."}, status=200)
