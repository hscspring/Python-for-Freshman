from django.urls import path
from authenticate import views

from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('users/', views.ListUserView.as_view(), name='user_index'),
    path('users/<int:pk>/', views.DetailUserView.as_view(), name='user_detail'),
    # we close csrf golbal setting on sign_up api, because you are signing up, do not sign in.
    path('sign_up/', csrf_exempt(views.SignUpView.as_view()), name='sign_up'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]