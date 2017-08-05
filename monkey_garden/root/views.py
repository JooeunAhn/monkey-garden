from django.shortcuts import render

from garden.models import MessageHistory


def root(request):
    return render(request, 'layout.html', {})


def mypage(request):
    message_histories = MessageHistory.objects.filter(user=request.user).order_by("-craeted_at")
    return render(request, 'mypage.html',
               {"message_histories": message_histories})