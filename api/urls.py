from django.urls import path,include

urlpatterns = [
    path('account/',include('ACCOUNTS.urls')),
    path('arthop/',include('ARTHOP.urls')),
]