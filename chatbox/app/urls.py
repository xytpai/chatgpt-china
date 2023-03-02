from django.urls import path
from .views import Register, Login, Logout, Index
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('index/', Index.as_view(), name='index'),
    path('', Index.as_view(), name='index'),
]
