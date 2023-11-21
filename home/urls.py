from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addstudent',views.addstudent),
    path('showstudent',views.showstudent),
    path('login',views.login_page)
]
