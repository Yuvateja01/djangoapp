from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from . models import Question
# Create your views here.
class Index(generic.ListView):
    model = Question
    template_name = 'polls/index.html'

    def  get_queryset(self):
        return Question.objects.all()

class Detail(generic.DetailView):
    model=Question
    template_name = 'polls/details.html'

class Results(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return  render(request,'polls/details.html',{'question':question,'error_message':"someting is wrong"})
    else:
        selected.votes+=1
        selected.save()

        return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))
