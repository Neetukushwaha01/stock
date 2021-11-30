from django.urls import path
from . import views


urlpatterns = [
     path('signup/', views.signup_view,name='signup'),
     path('login/', views.login_view,name='login'),
     path('logout/', views.logout_view,name='logout'),
     path('', views.home_view,name='home'),
     path('view/<slug>/', views.view_page, name='view'),


]
