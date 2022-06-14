# urls.py
from django.urls import path
from myapp.views import PublisherBookListView, PublisherListView

app_name = 'myapp'
urlpatterns = [
    path('', PublisherListView.as_view()),
    path('<publisher>/', PublisherBookListView.as_view()),
]
