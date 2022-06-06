from datetime import datetime

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

def processDaydata(texts):
    
    days = texts['days'].split(',')
    print(days)
    months = texts['months'].split(',')
    print(months)
    years = texts['years'].split(',')
    print(years)
    hours = texts['hours'].split(',')

    daydata = {
        "days":days,
        "months":months,
        "years":years,
        "hours": hours
    }

    return daydata
     
