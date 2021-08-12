from django.shortcuts import render

# Create your views here.
def vote(request):
    return render(request, 'vote.html')