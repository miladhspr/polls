from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
# Create your views here.
def index(request):
    questions = Question.objects.order_by('published')[:5]
    context = {'question_list':questions}
    return render(request,'pollster/index.html',context)


def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request,'pollster/detail.html' , {'question':question})


def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'pollster/results.html', {'question': question})


def vote(request,question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError , Choice,DoesNotExist):
        return render(request , 'pollster/detail.html',{
            'question':question,
            'error_message':"You Didnt select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('pollster:results',args=(question.id,)))
