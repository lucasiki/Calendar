import json
import random
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
import hashlib
from datetime import date, datetime
from .models import *
from django.contrib.sessions.models import Session



# language = default, and try to get stored session language
def initializeTextDB(df,language, session):
    try: 
        language = session['language']
    except:
        pass
    texts = df.filter(['key',language]) ## pt-br deve variar de acordo com a session.
    keys = texts['key'].to_list()
    content = texts[language].to_list()
    newvar = {}
    for x in range(0,len(texts)):
        newvar[keys[x]] = content[x]
    
    return newvar

def processRequest(string):
    try:
        value = json.load(string)
        return (json.loads(value))
    except:
        return ''  



def randomstring(amount):
 
    random_string = ''
    
    for x in range(amount):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    
    return random_string    

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip   



def sendmail(htmlpath, retorno, texts):
    html_message = loader.render_to_string(htmlpath,context ={
        "retorno" : retorno
        ,"texts":texts
    })
    send_mail(
        retorno['subject'],
        html_message,
        settings.ACCOUNT_CREATION_MAIL,
        [retorno['emailtext']],
        fail_silently=False,
        html_message=html_message
    ) 


def isauth(session):
    try:
        if  session['id'] != '':
            return 1
    except:
        pass
    return 0



def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

def parseDay(string):
    dateobject = datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")
    return dateobject