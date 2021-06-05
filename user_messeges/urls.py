from django.urls import path
from user_messeges.views import messeges_view, messege_processed

urlpatterns = [
    path('view', messeges_view),
    path('processed/<int:pk>',messege_processed)
]
