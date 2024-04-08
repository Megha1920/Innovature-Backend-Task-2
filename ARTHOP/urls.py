from django.urls import path
from .views import AdditionView, SubtractionView, MultiplicationView, DivisionView

urlpatterns = [
    path('add/', AdditionView.as_view(), name='addition'),
    path('subtract/', SubtractionView.as_view(), name='subtraction'),
    path('multiply/', MultiplicationView.as_view(), name='multiplication'),
    path('divide/', DivisionView.as_view(), name='division'),
]