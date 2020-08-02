from django.shortcuts import render
from django.shortcuts import redirect
###  从models取数据传给template  ###
from .models import Tb2

# Create your views here.
def movies(request):
    ###  从models取数据传给template  ###
    n = Tb2.objects.all()
    return render(request, 'movieslist.html', locals())