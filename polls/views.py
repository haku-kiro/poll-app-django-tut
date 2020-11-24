from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
# from django.template import loader

# Making use of the models of the current app
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])

    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}

    # Returns a comma seperated list of the last 5 questions
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    resp = "You're looking at the results of question %s."
    return HttpResponse(resp % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def test(request):
    return HttpResponse("This is a test endpoint")
