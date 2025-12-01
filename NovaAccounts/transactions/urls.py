from django.urls import path
from .views import AddTransactionView, UserTransactionView

urlpatterns = [
    path("add/", AddTransactionView.as_view()),
    path("", UserTransactionView.as_view())
]