from django.urls import path
from .views import Stock_api

urlpatterns = [
    path('api/', Stock_api.as_view()),

]
