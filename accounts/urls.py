
from django.urls import path
from .views import index_view
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', index_view, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup/freelancer/', views.signup_freelancer, name='signup_freelancer'),
    path('signup/client/', views.signup_client, name='signup_client'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
