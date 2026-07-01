from django.urls import path
from . import views
urlpatterns = [

path('api-UserList/',views.PassengerList.as_view(),name='passengerList'),
path("api-UserDetail/<int:pk>",views.PassengerDetail.as_view(),name='PassengerDetail' ),
path('api/custom-login/', views.CustomLoginView.as_view()),
path('api/logout/', views.LogoutView.as_view(), name='logout'),


]
