from django.urls import path
from . import views # . because it is in the same directory

urlpatterns = [
    
    path('', views.homepage, name="todo"), 
    path('del/<str:item_id>', views.remove, name="del"),
]