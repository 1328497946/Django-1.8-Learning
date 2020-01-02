from django.urls import path
from .views import *

app_name = "student"
urlpatterns = [
    path('', index),
    path('login/', login, name="login"),
    path('sendE/<int:stu_id>/', sender),
    path('jiaowu/', jiaowu)
]
