from django.urls import  path

from . import views

from . views import FileList, FileDetail, FileCreate, FileUpdate, FileDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import  LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', FileList.as_view(), name="files"),
    path('about/', views.about, name="about"),
    path('file/<int:pk>/', FileDetail.as_view(), name="file"),
    path('file-create/', FileCreate.as_view(), name="file-create"),
    path('file-update/<int:pk>/', FileUpdate.as_view(), name="file-update"),
    path('file-delete/<int:pk>/', FileDelete.as_view(), name="file-delete"),
    
]