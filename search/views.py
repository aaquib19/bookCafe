from django.views.generic import ListView
from book.models import Book

class SearchBookView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchBookView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            return Book.objects.search(query)
        return Book.objects.all()

        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''
