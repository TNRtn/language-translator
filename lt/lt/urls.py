"""lt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from language import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tnr/',views.sample),
    path('signup/',views.signupc,name='signup'),
    path('captcha/',include('captcha.urls')),
    path('login/',views.loginc,name='login'),
    path('main/<str:s>/',views.main,name='main'),
    path('users/',views.userlist,name="userlist"),
    path('delete/<int:k>',views.userdel,name="userdel"),
    path('info/<str:a>',views.info,name="info"),
    path('trans/<str:p>',views.translationa,name="translate"),
    path('t/',views.translated,name="translated"),
    path('his/',views.history,name="history"),
    path('hisdel/<str:c>',views.hisdelete,name="hisdel"),
    path('linfo/<str:j>',views.languageinfo,name="linfo"),
    path('feedback/<str:a2>',views.reviewform,name="feedback"),
    path('dictionary/',views.dictionary,name="dictionary"),
    path('fun/',views.fun,name="fun"),
    path('quotes/<str:p2>',views.quotes,name="quotes"),
    path('list/<str:p>',views.quotelist,name="list"),
    path('qinfo/<str:b>',views.quoteinfo,name="qinfo"),
    path('deleteuser/<str:b2>',views.deleteuser,name="deleteuser"),
    path('superuser/',views.superusersignupc,name="superuser"),
    path('superlogin/',views.superuserloginc,name="superlogin"),
    path('main2/<str:e>',views.main2,name="main2"),
    path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('index/',views.index,name="index"),
    #path('record/',views.record,name="record"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

