from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# from django.http import Http404
# from django.template import loader

# Making use of the models of the current app
from .models import Question, Choice


# Making use of generic views is better the manual views created below
# refer to index, results, and detail
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions.
        Not including those set to be published in the future.
        """

        return Question.objects.filter(pub_date__lte=timezone.now()).\
            order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # get_queryset is a member of generic.DetailView
    # and other views
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# Create your views here.
# Note, this file contains index, detail, and results views - they are however
# old and are just here as an example
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
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': q})


# Does get used
def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {'question': q,
                                                     'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after
        # Successfully dealing with post data
        return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))


def test(request):
    return HttpResponse("This is a test endpoint")
