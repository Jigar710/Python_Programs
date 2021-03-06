from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import loader
# Create your views here.

def index(request):
    return HttpResponse("This is index url.")

def pollsindex(request):
    return HttpResponse("This is polls index url.")

def pollsindex2(request):
    return HttpResponse("This is polls index url2.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def display(requst):
    lst = Question.objects.all()
    return HttpResponse(lst)

'''
def dis(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''

def dis(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)