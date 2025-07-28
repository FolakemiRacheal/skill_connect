from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User

def index_view(request):
        return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')  # A page with two buttons: Freelancer or Client

def signup_freelancer(request):
    return render(request, 'signup_freelancer.html')

def signup_client(request):
    return render(request, 'signup_client.html')



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
    })
