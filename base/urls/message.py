from django.urls import path
from base.views import message_views as views

urlpatterns = [

    path('', views.getProducts, name="users"),

    path('create/', views.create, name="new messsages"),
    path('upload/', views.uploadImage, name="image-upload"),

   
]
