from django.urls import path
from app1.views import app1_func
App1_name='app1'
urlpatterns = [
    path('app1_func/',app1_func,name='app1'),
]