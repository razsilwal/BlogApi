from django.urls import path 
from .views import RegisterView, PostListCreateView, PostDetailView, EmailTokenObtainPairView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
]