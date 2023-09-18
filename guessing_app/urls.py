from django.urls import path
from . import views 
urlpatterns = [
    path('home/',views.homepage,name='homepage'),
    path('add/',views.CreateItem,name='create_item'),
    
]
