from django.urls import path
from chat.views import home,room,checkview,send,getMessages


urlpatterns = [
    path('',home,name="home"),
    path('<str:pk>/',room,name='room'),
    path('checkview',checkview,name='checkview'),
    path('send',send,name='send'),
    path('getMessages/<str:pks>/',getMessages,name="getMessages"),
]

