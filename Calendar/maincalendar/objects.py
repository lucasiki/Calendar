from datetime import datetime, timedelta

objetos = [
    {
    "id": 1,
    "nome": "Lucas Scandian",
    "email": "lucasscandian@hotmail.com",
    "telefone": '(027) 98829-1539',
    "data": datetime(2022, 6, 10, 10, 10),
    "datainit" :  datetime(2022, 6, 10, 10, 8),
    "pago": False 
        },

        {
    "id": 2,
    "nome": "Kaue Solaris",
    "email": "kaue@hotmail.com",
    "telefone": '(027) 98829-1539',
    "data": datetime(2022, 6, 10, 15, 10),
    "datainit" :  datetime(2022, 6, 10, 9, 8),
    "pago": True 
        },
            {
    "id": 3,
    "nome": "Renato Funari",
    "email": "renato@hotmail.com",
    "telefone": '(027) 98829-1539',
    "data": datetime(2022, 6, 10, 17, 25),
    "datainit" :  datetime(2022, 6, 12, 10, 0),
    "pago": False 
        }
]

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def treatmonth(dayobject, daydata):
    newdate = datetime(dayobject.year, dayobject.month, 1)

    numberofdayweek = int(newdate.strftime('%w'))
    monthobject = []
    for x in range(0,42):
        newday = newdate + timedelta(x - numberofdayweek)
        monthobject.append({
            "id": x,
            "day": newday.day,
            "weekday": daydata['days'][weekdays.index(newday.strftime('%A'))].strip(),
            "month": newday.month,
            "monthname": daydata['months'][months.index(newday.strftime('%B'))].strip(),
            "year": newday.year,
            "weeknumber" : int(newday.strftime('%W')),
        })

 
    monthbigobject = {
        "monthlist": f"{daydata['months'][months.index(newdate.strftime('%B'))].strip()} {newdate.year}",
        "objects": monthobject
    }
    print(monthbigobject)
    return monthbigobject
    

def treatweek(dayobject, daydata):
    numberofdayweek = int(dayobject.strftime('%w'))
    

    weekobject = []
    for x in range(0,7):
        newday = dayobject + timedelta(x - numberofdayweek)
        weekobject.append({
            "id": x,
            "day": newday.day,
            "weekday": daydata['days'][weekdays.index(newday.strftime('%A'))].strip(),
            "month": newday.month,
            "monthname": daydata['months'][months.index(newday.strftime('%B'))].strip(),
            "year": newday.year,
            "weeknumber" : int(newday.strftime('%W')),
        })

    weekname1 = f"{weekobject[0]['monthname']} {weekobject[0]['day']}"
    if weekobject[0]['year'] != weekobject[6]['year']:
        weekname1 = weekname1 +', '+ weekobject[0]['year']

    weekname2 = f"{weekobject[6]['day']}, {weekobject[6]['year']}"
    if weekobject[0]['month'] != weekobject[6]['month']:
        weekname2 = weekobject[0]['monthname'] + ' ' + weekname2
    weekname = f"{weekname1} - {weekname2}"

    weekbigobject = {
        "weeklist" : weekname,
        "objects" : weekobject
    }   
    return weekbigobject


def treatday(dayobject, daydata, texts):
    weekday = dayobject.strftime('%A')
    month = dayobject.strftime('%B')

    #Translate
    weekday = daydata['days'][weekdays.index(weekday)].strip()
    monthname = daydata['months'][months.index(month)].strip()

    #treatweek(dayobject, daydata)

    treatmonth(dayobject, daydata)
    
    #Build Object
    daydict = {
        "day": dayobject.day,
        "weekday": weekday,
        "month": dayobject.month,
        "monthname" : monthname,
        "year": dayobject.year,
        "weeknumber" : int(dayobject.strftime('%W')),
        "listview" : f"{weekday}, {dayobject.day} {texts['txtof'].lower()} {monthname} {texts['txtof'].lower()} {dayobject.year}",
        "dayview": f"{monthname} {dayobject.day}, {dayobject.year}",
    }

    return daydict

def processDaydata(texts):
    
    days = texts['days'].split(',')
    months = texts['months'].split(',')
    years = texts['years'].split(',')
    hours = texts['hours'].split(',')

    daydata = {
        "days":days,
        "months":months,
        "years":years,
        "hours": hours
    }

    return daydata

def processStyle(texts):
    style={
        "font": texts['font'],
        "btnWidth" : texts['btnWidth'],
        "btnHeight": texts['btnHeight'],
        "color1" : texts['themeColor1'],
        "color2" : texts['themeColor2'],
        "color3" : texts['themeColor3'],
        "color4" : texts['themeColor4'],
    }
    return style
     
