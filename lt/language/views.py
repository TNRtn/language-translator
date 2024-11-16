from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest, HttpResponseServerError,JsonResponse
from .models import signup,login,transalate,translation,audio,quotesg,feedback,superuser,superuserlogin
from .forms import signupform,loginform,review,Audioform,quotesform,superusersignupform,superuserloginform
from django.db.models import F
from googletrans import Translator
import json
# Create your views here.
def sample(s):
	return HttpResponse("srm")

def signupc(request):
	if request.method=="POST":
		g=signupform(request.POST)
		if g.is_valid():
			g.save()
			return redirect('login')
	else:
		g=signupform()
	return render(request,"signup.html",{'k':g})

def loginc(request):
	if request.method=="POST":
		b=loginform(request.POST)
		if b.is_valid():
			b.save()
			username=b.cleaned_data['username']
			return redirect('main',username)
	else:
		b=loginform()
	return render(request,"login.html",{'a':b})

def main(request,s):
	b=signup.objects.get(username=s)
	return render(request,"main.html",{'a':b})

def sortbyusername(k):
	return k.username
def sortbyemail(k):
	return k.email
def sortbydate(k):
	return k.registerdate

def userlist(request):
	sortfields=request.GET.getlist('sort')
	ordering=[]
	for i in sortfields:
		if i=='username':
			ordering.append(F('username'))
		elif i=="email":
			ordering.append(F('email'))
		elif i=="registerdate":
			ordering.append(F('registerdate'))
	b=signup.objects.all().order_by(*ordering)
	return render(request,"userinfo.html",{'e':b})

def userdel(request,k):
	a=signup.objects.get(userid=k)
	if request.method=="POST":
		a.delete()
		return redirect('userlist')
	return render(request,"userdelete.html",{'z':a})

def info(request,a):
	b=login.objects.filter(username=a)
	c=signup.objects.get(username=a)
	return render(request,"info.html",{'k':b,'d':c,'l':a})
def translationa(request,p):
	return render(request,"translator.html",{'a':p})

def translated(request):
    # Extract parameters from the request
    text = request.GET.get('text', '').strip()
    lang = request.GET.get('lang', '').strip()
    
    # Check if text or lang is missing
    if not text:
        return JsonResponse({"error": "Text parameter is required."}, status=400)
    if not lang:
        return JsonResponse({"error": "Language parameter is required."}, status=400)

    # Define the language mapping
    lang_mapping = {
        'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic',
        'hy': 'Armenian', 'as': 'Assamese', 'ay': 'Aymara', 'az': 'Azerbaijani',
        'bm': 'Bambara', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali',
        'bho': 'Bhojpuri', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan',
        'ceb': 'Cebuano', 'zh-CN': 'Chinese', 'co': 'Corsican', 'hr': 'Croatian',
        'cs': 'Czech', 'da': 'Danish', 'dv': 'Dhivehi', 'doi': 'Dogri',
        'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian',
        'ee': 'Ewe', 'fil': 'Filipino', 'fi': 'Finnish', 'fr': 'French',
        'fv': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German',
        'el': 'Greek', 'gn': 'Guarani', 'gu': 'Gujarati', 'ht': 'Haitian Creole',
        'ha': 'Hausa', 'haw': 'Hawaiian', 'he': 'Hebrew', 'hi': 'Hindi',
        'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo',
        'ilo': 'Ilocano', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian',
        'ja': 'Japanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer',
        'rw': 'Kinyarwanda', 'gom': 'Konkani', 'ko': 'Korean', 'kri': 'Krio',
        'ku': 'Kurdish', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin',
        'lv': 'Latvian', 'ln': 'Lingala', 'lt': 'Lithuanian', 'lg': 'Luganda',
        'lb': 'Luxembourgish', 'mk': 'Macedonian', 'mai': 'Maithili', 'mg': 'Malagasy',
        'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori',
        'mr': 'Marathi', 'mni-Mtei': 'Meiteilon', 'lus': 'Mizo', 'mn': 'Mongolian',
        'my': 'Myanmar', 'ne': 'Nepali', 'no': 'Norwegian', 'ny': 'Nyanja',
        'or': 'Odia', 'om': 'Oromo', 'ps': 'Pashto', 'fa': 'Persian',
        'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'qu': 'Quechua',
        'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'sa': 'Sanskrit',
        'gd': 'Scots Gaelic', 'nso': 'Sepedi', 'sr': 'Serbian', 'st': 'Sesotho',
        'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak',
        'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish', 'su': 'Sundanese',
        'sw': 'Swahili', 'sv': 'Swedish', 'tl': 'Tagalog', 'tg': 'Tajik',
        'ta': 'Tamil', 'tt': 'Tatar', 'te': 'Telugu', 'th': 'Thai',
        'ti': 'Tigrinya', 'ts': 'Tsonga', 'tr': 'Turkish', 'tk': 'Turkmen',
        'ak': 'Twi', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur',
        'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa',
        'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'
    }

    # Translator initialization
    translator = Translator()

    try:
        # Detect the source language of the text
        detected_lang = translator.detect(text).lang
        from_lang = lang_mapping.get(detected_lang, 'Unknown Language')

        # Get the target language full name
        to_lang = lang_mapping.get(lang, 'Unknown Language')

        # Handle unsupported target languages
        if to_lang == 'Unknown Language':
            return JsonResponse({"error": f"Unsupported target language code: {lang}"}, status=400)

        # Translate the text
        translated_text = translator.translate(text, dest=lang).text

        # Save translation (assuming a model called 'translation' exists)
        # Comment this out if the model doesn't exist
        """
        new_translation = translation(
            fromlang=from_lang,
            tolang=to_lang,
            fromtext=text,
            totext=translated_text
        )
        new_translation.save()
        """

        # Render the translated page
        return render(request, "translated.html", {
            'translated': translated_text,
            'flang': from_lang,
            'tlang': to_lang,
            'text': text
        })

    except Exception as e:
        # Handle unexpected errors
        return JsonResponse({"error": str(e)}, status=500)

def history(request):
	k=translation.objects.all()
	return render(request,"history.html",{'a':k})

def hisdelete(request,c):
	l=translation.objects.get(date=c)
	if request.method=="POST":
		l.delete()
		return redirect('history')
	return render(request,"historydelete.html",{'z':l})

def languageinfo(request,j):
	l=translation.objects.get(date=j)
	return render(request,"languageinfo.html",{'z':l})

def reviewform(request,a2):
	if request.method=="POST":
		a=request.POST.get('comment')
		b=request.POST.get('query')
		c=request.POST.get('rating')
		newreview=feedback(
			comment=a,
			query=b,
			rating=c,
			)

		newreview.save()
		return redirect('main',a2)
	else:
		k=review()
		return render(request,"feedback.html",{'g':k,'a2':a2})

def dictionary(request):
	return render(request,"Dictapp.html")

def fun(request):
	return render(request,"new.html")

def quotes(request,p2):
	if request.method=="POST":
		g=quotesform(request.POST,request.FILES)
		if g.is_valid():
			g.save()
			return redirect('list',username=p2)
		else:
			print(g.errors)
	else:
		g=quotesform()
		return render(request,'quotes.html',{'k':g,'k3':p2})

def quotelist(request,p):
	a=quotesg.objects.all()
	return render(request,"quotelist.html",{'k':a,'k2':p})
def quoteinfo(request, b):
	if request.method=="POST":
		data=json.loads(request.body)
		text=data.get("text","")
		translat=Translator()
		th=translat.translate(text,dest="hi").text
		tr=translat.translate(text,dest="te").text
		return JsonResponse({
			'hindi':th,
			'telugu':tr,
			})
	else:
		k = quotesg.objects.get(name=b)
		return render(request, "quoteinfo.html", {"a": k})


def deleteuser(request,b2):
	a=signup.objects.get(userid=b2)
	if request.method=="POST":
		a.delete()
		return redirect('signup')
	return render(request,"deleteaccount.html",{'z':a})

def superusersignupc(request):
	if request.method=="POST":
		g=superusersignupform(request.POST)
		if g.is_valid():
			g.save()
			return redirect('login')
	else:
		g=superusersignupform()
	return render(request,"superusersignup.html",{'k':g})

def superuserloginc(request):
	if request.method=="POST":
		b=superuserloginform(request.POST)
		if b.is_valid():
			b.save()
			username=b.cleaned_data['username']
			return redirect('main2',username)
	else:
		b=superuserloginform()
	return render(request,"superuserlogin.html",{'a':b})

def main2(request,e):
	b=superuser.objects.get(username=e)
	return render(request,"main2.html",{'a':b})

def viewfeedback(request):
	a=feedback.objects.all()
	print(a)
	return render(request,"viewfeedback.html",{'k':a})

def index(request):
	return render(request,"index.html")
