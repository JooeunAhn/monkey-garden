from django.shortcuts import render

# Create your views here.
def root(request):
	return render(request, 'layout.html', {})


def mypage(request):
	return render(request, 'mypage.html', {})