from django.urls import path
from . import views

urlpatterns = [
    path('garden/', views.fruitGarden, name='fruitGarden'),

    path('', views.fetchAllFruits, name='fetchAll'),  # Home page
    path('home/', views.fetchAllFruits, name='home'),  # Optional alias

    path('create/', views.createFruit, name='create-fruit'),
    
    path('fruit/<int:id>/', views.fruitDetail, name='fruit-detail'),
    path('fruit/<int:id>/update/', views.updateFruit, name='update-fruit'),
    path('fruit/<int:id>/delete/', views.deleteFruit, name='delete-fruit'),
]