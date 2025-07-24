from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.



from rest_framework.response import Response

def index_view(request):
        return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')  # A page with two buttons: Freelancer or Client

def signup_freelancer(request):
    return render(request, 'signup_freelancer.html')

def signup_client(request):
    return render(request, 'signup_client.html')