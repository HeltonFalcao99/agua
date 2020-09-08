from django.urls import path
from treino import views
from treino.models import  LogMessage 

home = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="treino/home.html",
)

app_name= 'treino'

urlpatterns = [
    path("", home, name="home"),
    path("ola<name>", views.ola, name="ola"),
    path("soma=<a>+<b>+<c>", views.soma, name="soma"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("calculadora/", views.calculadora, name="calculadora"),
    path( "log/", views.log, name = "log" ),
]


#python manage.py runserver