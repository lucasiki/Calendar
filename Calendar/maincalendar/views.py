from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from pandas import read_excel
from django.utils.timezone import now
from django.core.paginator import Paginator
from .functions import *
from .objects import *
from dateutil.relativedelta import relativedelta
from Calendar import settings
from django.contrib.contenttypes.models import ContentType


# Create your views here.


df = read_excel('maincalendar/static/maincalendar/textdb.xlsx') ## Initialize wordsdb
language = 'pt-br'
paginatorDefault = 10



def handle_uploaded_file(f):
    with open(settings.MEDIA_ROOT / str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class testView(View):
    def get(self,request):
        

        return render(request, 'maincalendar/test.html')
    def post(self,request):
        print(request.FILES)
        print(request.FILES['file'])
        print(request.POST)
        handle_uploaded_file(request.FILES['file'])

    


        return JsonResponse({})

def convertHour(string):
    return datetime.strptime(string, "%H:%M")


class hourWidgetView(View):
    def get(self,request):

        hourslist = sorted([
            '15:00',
            '16:00',
            '16:30',
            '17:00',
            '13:00',
        ])
        print(hourslist)

        context={"hourslist": hourslist}

        resposta = render(request, 'maincalendar/widgets/hourwidget.html', context)
        resposta['Content-Security-Policy'] = "frame-ancestors 'self' "
        return resposta

class widgetView(View):
    def get(self,request):
        texts = initializeTextDB(df,language,request.session)
        daydata = processDaydata(texts)
        defaultday = treatmonth(datetime.today(), daydata) 
        request.session['DaySession'] = str(datetime.today())

        #print(defaultday)
        ##Devemos retornar também os dias válidos

        context = {
            "texts": texts,
            "daydata": daydata,
            "defaultday" : defaultday,
        }
        resposta = render(request, 'maincalendar/widgets/calendarwidget.html', context)
        resposta['Content-Security-Policy'] = "frame-ancestors 'self'"
        return resposta

    def post(self,request):
        texts = initializeTextDB(df,language,request.session)
        daydata = processDaydata(texts)
        ret = processRequest(request)        
        daysession = parseDay(request.session['DaySession'])

        ##Devemos retornar também os dias válidos

        mod = 0
        if ret['key'] == 'decrease':
            mod = -1
        elif ret['key'] == 'increase':
            mod = 1
        elif ret['key'] == 'today':    
            daysession = datetime.today()

        increase = mod*1
        newdate = daysession + relativedelta(months=increase)
        request.session['DaySession'] = str(newdate)
        defaultday = treatmonth(newdate, daydata)
        context = {
            "daydata": daydata,
            "defaultday" : defaultday,
        }
        #print(defaultday)
        resposta = render(request, 'maincalendar/widgets/calendarwidget.html', context)
        resposta['Content-Security-Policy'] = "frame-ancestors 'self' "
        return resposta


class indexView(View):
    def get(self,request):
        texts = initializeTextDB(df,language,request.session)
        daydata = processDaydata(texts)
        style = processStyle(texts)
        objects = objetos

        paginator = Paginator(objects,paginatorDefault)
        objects = paginator.get_page(1)

        defaultday = treatday(datetime.today(), daydata, texts) 

        request.session['DaySession'] = str(datetime.today())

        request.session['selectedView'] = urlreverse['list']
        
        context = {
            "texts": texts,
            "session": request.session,
            "objects": objects,
            "daydata": daydata,
            "style" : style,
            "defaultday" : defaultday,
            "rendername": defaultday['listview']
        }
        response = render(request, 'maincalendar/index.html', context)
        response ['Content-Security-Policy'] = "frame-ancestors 'self' http://127.0.0.1:8000/"
        return response


class processView(View):
    def post(self, request):
        texts = initializeTextDB(df,language,request.session)
        daydata = processDaydata(texts)
        style = processStyle(texts)
        ret = processRequest(request)
        daysession = parseDay(request.session['DaySession'])
        selectedview = request.session['selectedView']
        objects = objetos

        paginatorpage = 1
        paginatorDefault = 10
        if ret['key'] == 'paginate':
            paginatorDefault = ret['amount']
            paginatorpage = ret['data']

        paginator = Paginator(objects,paginatorDefault)
        objects = paginator.get_page(paginatorpage)


        mod = 0
        if ret['key'] == 'decrease':
            mod = -1
        elif ret['key'] == 'increase':
            mod = 1
        elif ret['key'] == 'today':    
            daysession = datetime.today()
        elif ret['key'] == 'list':
            selectedview = urlreverse['list']
        elif ret['key'] == 'day':
            selectedview = urlreverse['day']
        elif ret['key'] == 'week':
            selectedview = urlreverse['week']
        elif ret['key'] == 'month':
            selectedview = urlreverse['month']

        request.session['selectedView'] = selectedview

        increase = 0
        if selectedview == urlreverse['list']:
            increase = mod
            newdate = daysession + timedelta(increase)
            request.session['DaySession'] = str(newdate)    
            defaultday = treatday(newdate, daydata, texts)
            rendername = defaultday['listview']

        elif selectedview == urlreverse['day']:
            increase = mod
            newdate = daysession + timedelta(increase)
            request.session['DaySession'] = str(newdate)
            defaultday = treatday(newdate, daydata, texts)
            rendername = defaultday['dayview']

        elif selectedview == urlreverse['week']:
            increase = mod*7
            newdate = daysession + timedelta(increase)
            request.session['DaySession'] = str(newdate)
            defaultday = treatweek(newdate, daydata)
            rendername = defaultday['weeklist']

        elif selectedview == urlreverse['month']:
            increase = mod*1
            newdate = daysession + relativedelta(months=increase)
            request.session['DaySession'] = str(newdate)
            defaultday = treatmonth(newdate, daydata)
            rendername = defaultday['monthlist']


        print(defaultday)
        context = {
            "texts": texts,
            "session": request.session,
            "objects": objects,
            "daydata": daydata,
            "style" : style,
            "defaultday" : defaultday,
            "rendername": rendername,
            "paginatorDefault": paginatorDefault
        }

        return render(request, selectedview, context)


