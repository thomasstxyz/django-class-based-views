# views.py
from django.views.generic import DetailView, ListView
from myapp.models import Book, Publisher
from django.shortcuts import get_object_or_404

class PublisherListView(ListView):
    model = Publisher
    context_object_name: 'my_favorite_publishers'

class PublisherDetailView(DetailView):

    context_object_name = 'publisher'
    queryset = Publisher.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

class BookListView(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'

class AcmeBookListView(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'myapp/acme_list.html'

class PublisherBookListView(ListView):

    template_name = 'myapp/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context
