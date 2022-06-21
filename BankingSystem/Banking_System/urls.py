from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('customers',views.customers,name='customers'),
    path('transfer/<int:id>',views.transfer,name='transfer'),
    path('transfer/transfer-complete',views.submission,name='transfer-complete'),
]