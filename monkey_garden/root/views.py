from django.shortcuts import render


# https://www.youtube.com/watch?v=zZ4n0fI23_g
# www.youtube.com/embed/z7d1fDUyuzQ

def embed(input):
	pass
	
# Create your views here.
def root(request):
	return render(request, 'layout.html', {})

def mypage(request):
	return render(request, 'mypage.html', {})