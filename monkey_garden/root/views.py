from django.shortcuts import render

from garden.models import MessageHistory
from accounts.models import Profile
import random


def root(request):
    return render(request, 'layout.html', {})


def mypage(request):
	message_histories = MessageHistory.objects.exclude(message__url="")
	message_histories = message_histories.filter(user=request.user).order_by("-created_at")
	profile = Profile.objects.all()
	randomList=["KKIIII", "KKKKUUUU", "KKIK", "KKAK", "KKKKKIIII", "KKKIIIIUUUI"]

	for mh in message_histories:
		if mh.message.text == "":
			mh.message.text = random.choice(randomList)
			mh.save()

	return render(request, 'mypage.html',
	{
		"message_histories": message_histories,
		"profile": profile,
	})