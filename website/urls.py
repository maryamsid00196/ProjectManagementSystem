import statistics
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from website import views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    #path('', views.index, name="firstpage"),
    path('', views.index, name='index'),
    path('allenteries/PHpage/projectPH', views.projectPH, name='projectPH'),
    path('allenteries/PHlogin/PHpage', views.PHpage, name='PHpage'),
    path('allenteries', views.allenteries, name='allenteries'),
    path('allenteries/PHlogin/Project_Head', views.Project_Head, name='Project_Head'),
    path('allenteries/PHlogin', views.PHlogin, name='PHlogin'),

    path('allenteries/Clogin', views.Clogin, name='Clogin'),
    path('allenteries/Alogin/Assigner', views.Assigner, name='Assigner'),
    path('allenteries/Alogin', views.Alogin, name='Alogin'),
    path('allenteries/allenteries/Assignee/developer', views.developer, name='developer'),
    path('allenteries/allenteries/Assignee/manager', views.manager, name='manager'),
    path('allenteries/allenteries/Assignee/designer', views.designer, name='designer'),
    path('allenteries/allenteries/Assignee/tester', views.tester, name='tester'),
    path('allenteries/Assignee', views.Assignee, name='Assignee'),
    path('allenteries/Clogin/client', views.client, name='client')]