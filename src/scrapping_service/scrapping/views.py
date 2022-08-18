from django.shortcuts import render
from .models import Vacancies
import datetime

# Create your views here.
def home_view(request):
    query_set = Vacancies.objects.all()
    date = datetime.datetime.now().date()
    return render(request, 'home.html', {'object_list' : query_set, 'date': date})