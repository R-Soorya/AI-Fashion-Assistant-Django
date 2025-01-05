from django.urls import path
from . import views

app_name = 'wardrobe'

urlpatterns = [
    path('', views.wardrobe_assistant, name='wardrobe-assistant'),
    # path('collections', views.collections, name='collections'),
    path('generate', views.generate, name='generate'),
    path('wardrobe-and-collections/', views.wardrobe_and_collections, name='wardrobe_and_collections'),
    path('delete-outfit/<int:outfit_id>/', views.delete_outfit, name='delete-outfit'),
    path('plan-your-outfit/', views.plan_your_outfit, name='plan-your-outfit')

]

