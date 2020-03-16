from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'pratica/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
    Return the last five published questions (not including those set to be
    published in the future).
    """
        return Question . objects . filter (
        pub_date__lte = timezone . now ()
    ) . order_by ( '-pub_date' )[: 5 ]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'pratica/detail.html'
    def get_queryset ( self ):
       """
       Excludes any questions that aren't published yet.
       """
       return Question . objects . filter ( pub_date__lte = timezone . now ())
    


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'pratica/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'pratica/vote.html', {
            'question': question,
            'error_message': "voce não selecionou uma escolha.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pratica:results', args=(question.id,)))