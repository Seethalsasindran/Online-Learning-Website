from django.urls import path

from . import views

urlpatterns=[
    path('',views.myfunc,name='myfunc'),
    path('register',views.myfunc1,name='myfunc1'),
    path('login',views.myfunc2,name='myfunc2'),
    path('about',views.myfunc3,name='myfunc3'),
    path('contact',views.myfunc4,name='myfunc4'),
    path('topics',views.myfunc5,name='myfunc5'),
    path('topics_detail/<int:Subjects_id>/',views.myfunc6,name='myfunc6'),
    
]