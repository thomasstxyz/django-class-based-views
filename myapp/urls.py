# urls.py
from django.urls import path
from myapp.views import PublisherListView

app_name = 'myapp'
urlpatterns = [
    path('', PublisherListView.as_view()),
]