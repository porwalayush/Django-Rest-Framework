from django.urls import path
from cookies import views
urlpatterns = [
    path('setcookie/', views.setcookie, name= 'setcookie'),
    path('getcookie/', views.showcookie, name='showcookie'),
    path('delete_co/', views.delete_co, name='showcookie'),
]