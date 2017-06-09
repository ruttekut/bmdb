from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from account.models import Books


@method_decorator(login_required(login_url='books:login'), name='dispatch')
class IndexView(generic.ListView):
    template_name = 'account/home.html'

    def get_queryset(self):
        return Books.objects.all()


class DetailView(generic.DetailView):
    model = Books
    template_name = 'account/bookdetails.html'
