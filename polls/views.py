from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    # import pdb; pdb.set_trace()
    # return HttpResponse("Hello, world. You're at the polls index.")

    latest_question_list = Question.objects.order_by('-pub_date')[:5]

     # output = ', '.join([q.question_text for q in latest_question_list])
     # return HttpResponse(output)

    context = {
        'latest_question_list': latest_question_list,
    }

    """ Manual Rendering """
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))    

    """ Shortcut Rendering """
    return render(request, 'polls/index.html', context)
    

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)

    """ Manual 404'ing """
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    """ Shortcut 404'ing """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)