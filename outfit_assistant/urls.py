from django.urls import path
from . import views

app_name = 'outfit'

urlpatterns = [
    path('', views.outfit_assistant, name='outfit-assistant'),  
]
