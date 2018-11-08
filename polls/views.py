# from django.shortcuts import render, get_object_or_404
# # from django.http import HttpResponse, Http404, HttpResponseRedirect
# # from django.template import loader
# from django.urls import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Deprecated in favor of generic views
"""
def index(request):
    # import pdb; pdb.set_trace()
    # return HttpResponse("Hello, world. You're at the polls index.")

    latest_question_list = Question.objects.order_by('-pub_date')[:5]

     # output = ', '.join([q.question_text for q in latest_question_list])
     # return HttpResponse(output)

    context = {
        'latest_question_list': latest_question_list,
    }

    ### Manual Rendering ###
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))    

    ### Shortcut Rendering ###
    return render(request, 'polls/index.html', context)
    

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)

    ### Manual 404'ing ###
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    ### Shortcut 404'ing ###
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

"""

