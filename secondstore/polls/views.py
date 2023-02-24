from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 
                      "polls/detail.html",
                      {'question': question, 
                      'error_message': "You can't vote if you don't select a choice!"
                      })
    else:
        Choice.objects.update(votes=F('votes') +1)
        # removed race condition from tutorial
        # selected_choice.votes += 1
        # selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def secret(request):
    return HttpResponse("Now this is just fun to add, no?")