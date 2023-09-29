from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreatView, UserUpdateDeleteView, UserList, TaskViewSet


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('users/register', UserCreatView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserUpdateDeleteView.as_view(), name='user-update-delete'),
    path('users/', UserList.as_view(), name='user-list'),
    path('', include(router.urls)),  # Include TaskViewSet routes
]
