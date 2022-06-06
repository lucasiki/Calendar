from django.shortcuts import render
from django.views import View
from pandas import read_excel
from django.utils.timezone import now
from django.core.paginator import Paginator
from .functions import *
from .objects import *

# Create your views here.


df = read_excel('maincalendar/static/maincalendar/textdb.xlsx') ## Initialize wordsdb
language = 'pt-br'
paginatorDefault = 10




class indexView(View):
    def get(self,request):
        texts = initializeTextDB(df,language,request.session)
        objects = objetos

        paginator = Paginator(objects,paginatorDefault)
        objects = paginator.get_page(1)

        context = {
            "texts": texts,
            "session": request.session,
            "objects": objects
        }
        return render(request, 'maincalendar/index.html', context)



class dayView(View):
    def get(self, request):
        texts = initializeTextDB(df,language,request.session)
        daydata = processDaydata(texts)
        objects = objetos
        print(daydata['hours'])

        context = {
            "texts": texts,
            "session": request.session,
            "objects": objects,
            "daydata": daydata
        }
        return render(request, 'maincalendar/dayview.html', context)