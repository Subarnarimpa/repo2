from django.urls import path
from app2.views import app2_func
APP_NAME='app2'
urlpatterns = [
    path('app2_func/',app2_func,name='app2'),
]