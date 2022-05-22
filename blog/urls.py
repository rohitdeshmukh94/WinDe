from django.urls import path
from blog import views

urlpatterns = [
 path("home/", views.home, name="home"),
path("search/",views.search, name='search'),
path("signup/",views.signup, name='signup'),
path("loginblog/",views.loginblog, name='loginblog'),
path("logoutblog/",views.logoutblog, name='logoutblog'),
path('<str:slug>/',views.blog_post, name='blogpost'),


]