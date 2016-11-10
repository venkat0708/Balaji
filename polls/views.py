from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	
	
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
	
	# def get_queryset(self):
		# """
		# Excludes any questions that aren't published yet.
		# """
		# return Question.objects.filter(pub_date__lte=timezone.now())
	
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})
	
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KEYERROR, Choice.DoesNotExist):
		return render(request, "polls/detail.html",{
			'question':question,
			'error_message': "You didn't select a Choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))