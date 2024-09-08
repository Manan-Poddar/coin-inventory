from django.urls import path
from . import views

urlpatterns = [
    path('chats/<int:request_user_id>/', views.chat_view, name='chat-view'),
    path('load_more_messages/', views.load_more_messages, name='load-more-messages'),
]
