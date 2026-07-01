from django.urls import path
from . import views
urlpatterns = [
  path('listPayment/',views.ListPayment.as_view(),name='listPayment'),
  path('detailPayment/<str:passenger>/',views.DetailPayment.as_view(),name='detailPayment'),
  path('listRecord',views.ListRecord.as_view(),name='listRecord'),
  path('detailRecord',views.DetailRecord.as_view(),name='detailRecord')

]
