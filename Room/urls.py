from django.urls import path
from . import views
urlpatterns = [

  path('detail/<int:pk>',views.RoomDetail.as_view(),name='DetailRoom'),
  path('<int:room_id>/upload-images/',views.RoomCreateWithImagesView.as_view(),name='createRoomImage'),
  path('reserve',views.reserveRoom.as_view(),name='ReserveRoom'),
  path('detailReserve',views.detailReserveRoom.as_view(),name='DetailReserve'),
  path('uploadImage',views.uploadImage.as_view(),name='uploadImage'), 
  
]
