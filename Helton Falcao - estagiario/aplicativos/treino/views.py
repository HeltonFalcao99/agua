from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from treino.forms import LogMessageForm
from treino.models import LogMessage
from django.views.generic import ListView

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

"""def ola(request, name):
    hora = datetime.now()
    hora_formatada = hora.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    limitador = re.match("[a-zA-Z]+", name)

    if limitador:
        nome_limpo = limitador.group(0)
    else:
        nome_limpo = "Friend"

    retorno = "ola, " + nome_limpo + "! It's " + hora_formatada
    return HttpResponse(retorno)
    """

def soma(request, a, b, c):
    try:
        retorno= float(a) + float(b) + float(c)

    except:
        retorno = "ENTRADA INVALIDA!"
    return HttpResponse(retorno)

def ola(request, name):
    return render(
        request,
        'treino/ola.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "treino/about.html")

def contact(request):
    return render(request, "treino/contact.html")

def calculadora(request):
        return render(request, "treino/calculadora.html")
    
def log(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("treino:home")
    else:
        return render(request, "treino/log_message.html", {"form": form})