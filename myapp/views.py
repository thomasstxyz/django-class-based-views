# views.py
from django.views.generic import ListView
from myapp.models import Publisher

class PublisherListView(ListView):
    model = Publisher