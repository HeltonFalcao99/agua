from django.urls import path
from aguadisponivel import views


app_name='aguadisponivel'


urlpatterns = [
    path("", views.inicio, name = "inicio" ),
    path ("PTF/", views.PTFview, name = "PTFview"),
    path ("ptfexcel/", views.excel, name = "excel"),
]


