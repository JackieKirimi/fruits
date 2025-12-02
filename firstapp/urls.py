from django.urls import path
from .import views
#import views
urlpatterns = [
    path('fruits',views.fruitGarden, name='fruitGarden'),
    path('home/', views.home, name='home'),   
    path('create/', views.createFruit, name='create'),
    
    path('fruits',views.fetchAllFruits,name='fetchAll'),
    path('fruit/<int:id>/', views.fruitDetail, name='fruit-detail'),
    path('fruit/<int:id>/update/', views.updateFruit, name='update-fruit'),
    path('fruit/<int:id>/delete/', views.deleteFruit, name='delete-fruit'),
]
