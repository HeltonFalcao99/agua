from django.urls import path
from aguadisponivel import views


app_name='aguadisponivel'


urlpatterns = [
    path("", views.inicio, name = "inicio" ),
    path("about/", views.about, name ="about"),
    path("explicacao/", views.explicacao, name ="explicacao"),
    path ("PTF/", views.PTFview, name = "PTFview"),
    path ("ptfexcel/", views.excel, name = "excel"),
    path ("PTF./", views.escolha, name = "escolha"),
]



