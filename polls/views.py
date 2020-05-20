from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request,'polls/index.html',context)
