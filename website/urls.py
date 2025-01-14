from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name=""),
    #path("contact_page/",views.contact_page,name="contact_page"),
]
