from django.urls import path
from . import views # . because it is in the same directory

urlpatterns = [
    
    path('', views.todo, name=""), 
    path('/del/<str:item_id>', views.remove, name="del"), 
]