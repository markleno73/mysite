from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question
from .forms import myform
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def formy(request):
    # if this is a post request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with the data from the request
        form = myform(request.POST)
        # check wether or not its valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a different url
            return HttpResponseRedirect('/thanks/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = myform()
    return render(request, 'polls/formy.html', {'form': form})

