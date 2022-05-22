from django.urls import path
from Home import views
urlpatterns = [path("",views.Home ,name="home"),
                path("about/", views.About, name="about"),
                path("contact/", views.contact, name="contact"),
                path("digitalservice/", views.digitalservice, name="digitalservice"),
                path("socialmediaservice/", views.socialmediaservice, name="socialmediaservice"),
                path("webdesignservice/", views. webdesignservice, name=" webdesignservice"),
                path("contentwritingservice/", views.contentwritingservice, name="contentwritingservice"),
                path("graphicdesignservice/", views.graphicdesignservice, name="graphicdesignservice"),
]
