from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #showchart应用
    url('',include('showchart.urls',namespace='showchart')),

]

