from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('results/<int:instance_id>/', views.results, name="results"),
    path('history', views.history, name="history"),
]